from django.urls import path
from . import views


urlpatterns = [
    path("", views.home, name="home"),
    path("<int:year>/<str:month>/", views.home, name="home"),
    path("addmission", views.addmission, name="addmission"),
    path("submission", views.submission, name="submission"),
    path("pdf", views.render_pdf_view, name="pdf"),
]
