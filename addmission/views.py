import calendar
from calendar import HTMLCalendar, month_name
from datetime import datetime
from django.shortcuts import render
from django.urls import is_valid_path
from .forms import pForm
from .models import personalInfo
from django.http import HttpResponseRedirect
from django.http import HttpResponse
from xhtml2pdf import pisa   
from django.template.loader import get_template
name = "johm"
now = datetime.now()


def home(request, year=now.year, month=now.strftime("%B")):
    month = month.capitalize()
    month_num = list(calendar.month_name).index(month)
    month_num = int(month_num)
    test = calendar.month_name
    cal = HTMLCalendar().formatmonth(year, month_num)

    return render(
        request,
        "home.html",
        {
            "name": name,
            "month": month,
            "year": year,
            "month_num": month_num,
            "test": test,
            "cal": cal,
        },
    )

def submission(request):
    date=datetime.now().strftime("%d %m %y")
    sub_list=personalInfo.objects.all()
    last=sub_list.last()
    return render(
        request,
        "submission.html",
        {
            "sub_list": sub_list,
            "last": last,
            "date": date,

        },
    )


def addmission(request):
    submitted = False
    if request.method == "POST":
        form = pForm(request.POST, request.FILES)

        if (
            form.is_valid()

        ):
            form.save()


            return HttpResponseRedirect("/addmission?submitted=True")
    else:
        form = pForm

        if "submitted" in request.GET:
            submitted = True

    return render(
        request,
        "addmission.html",
        {
            "form": form,

            "submitted": submitted,
        },
    )

def render_pdf_view(request):
    sub_list=personalInfo.objects.all()
    last=sub_list.last()
    template_path = 'submission.html'
    context = {'last': last}
    # Create a Django response object, and specify content_type as pdf
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="report.pdf"'
    # find the template and render it.
    template = get_template(template_path)
    html = template.render(context)

    # create a pdf
    pisa_status = pisa.CreatePDF(
       html, dest=response)
    # if error then show some funy view
    if pisa_status.err:
       return HttpResponse('We had some errors <pre>' + html + '</pre>')
    return response