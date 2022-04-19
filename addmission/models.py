from distutils.command.upload import upload
from random import choices
from django.conf import settings
from django.db import models
from django import forms
from datetime import datetime, date
import qrcode
from io import BytesIO
from django.core.files import File
from PIL import Image, ImageDraw


from django.forms import DateInput

# Create your models here.
class personalInfo(models.Model):
    proChoice = (
        ("", "Select One"),
        ("cse", "CSE"),
        ("eee", "EEE"),
        ("civil", "Civil"),
        ("english", "English"),
        ("buisness", "Buisness"),
        ("mechanical", "Mechanical"),
    )
    shiftChoice = (
        ("", "Select One"),
        ("morning", "Morning"),
        ("evening", "Evening"),
    )

    sesChoice = (("sumer_2024", "Summer 2024"),)
    sectionChoice = (
        ("", "Select One"),
        ("a", "A"),
        ("b", "B"),
    )
    genderChoice = (
        ("", "Select One"),
        ("male", "Male"),
        ("female", "Female"),
    )
    reChoice = (
        ("", "Select One"),
        ("islam", "Islam"),
        ("cristian", "Cristian"),
        ("hindu", "Hindu"),
    )
    quoraChoice = (
        ("", "Select One"),
        ("none", "None"),
        ("disabled", "Disablied"),
        ("freedom", "Freedom Fighter"),
    )
    bgChoice = (
        ("", "Select One"),
        ("a+", "A+"),
        ("a-", "A-"),
        ("b+", "B+"),
        ("b-", "B-"),
        ("o+", "O+"),
        ("o-", "O-"),
        ("ab+", "AB+"),
        ("ab-", "AB-"),
    )

    inProgram = models.CharField(
        "Program", choices=proChoice, max_length=50, default=""
    )
    shift = models.CharField("Shift", choices=shiftChoice, max_length=50)
    session = models.CharField(
        "Session", choices=sesChoice, default="summer_2024", max_length=50
    )
    section = models.CharField(
        "Section", choices=sectionChoice, max_length=50, default=""
    )
    sName = models.CharField("Student Name", max_length=50)
    cNum = models.CharField("Contract NBumber", max_length=50)
    email = models.EmailField("Email")
    gender = models.CharField("Gender", choices=genderChoice, max_length=50, default="")
    bCert = models.CharField("Birth Certificate/NID number", max_length=50)
    image = models.ImageField("Student photo", null=True, upload_to="images/")
    religion = models.CharField("Religion", choices=reChoice, max_length=50, default="")
    doBirth = models.CharField("Date of Birth", max_length=50)
    pAds = models.CharField("Present address", max_length=50)
    bGroup = models.CharField(
        "Blood Group", choices=bgChoice, max_length=50, default=""
    )
    nationality = models.CharField(
        "Nationality",
        max_length=50,
    )
    quota = models.CharField("Quota", choices=quoraChoice, max_length=50, default="")

    # Family Background

    fName = models.CharField("Father Name", max_length=50)
    fcNum = models.CharField("Father phone no.", max_length=50)
    fOccu = models.CharField("Father occupation", max_length=50)
    fEmail = models.EmailField("Father Email", blank=True)
    mName = models.CharField("Mother Name", max_length=50)
    mcNum = models.CharField("Mother phone no.", max_length=50)
    mOccu = models.CharField("Mother occupation", max_length=50)
    mEmail = models.EmailField("Mother Email", blank=True)

    # educational Background

    # exam1
    e1Choice = (
        ("", "Select One"),
        ("ssc", "SSC"),
        ("dakhil", "Dakhil"),
        ("vocational", "Vocational"),
    )
    board1Choice = (
        ("", "Select One"),
        ("dhaka", "Dhaka"),
        ("cumilla", "Cumilla"),
        ("barishal", "Barishal"),
        ("madrasha", "Madrasha"),
        ("bteb", "BTEB"),
    )
    eTitle1 = models.CharField(
        "Exam Title", choices=e1Choice, max_length=50, default=""
    )
    board1 = models.CharField("Board", choices=board1Choice, max_length=50, default="")
    eGroup1 = models.CharField("Group", max_length=50)
    bRoll1 = models.CharField("Board Roll", max_length=50, default="")
    eResult1 = models.CharField("Result", max_length=50)
    pYear1 = models.CharField("Pass Year", max_length=50, default="")
    insName1 = models.CharField("Institute Name", max_length=50)

    # exam2
    e2Choice = (
        ("", "Select One"),
        ("hsc", "HSC"),
        ("alim", "Almin"),
        ("diploma", "Diploma"),
    )
    board2Choice = (
        ("", "Select One"),
        ("dhaka", "Dhaka"),
        ("cumilla", "Cumilla"),
        ("barishal", "Barishal"),
        ("madrasha", "Madrasha"),
        ("bteb", "BTEB"),
    )
    eTitle2 = models.CharField(
        "Exam Title", choices=e2Choice, max_length=50, default=""
    )
    board2 = models.CharField(
        "Board",
        choices=board2Choice,
        max_length=50,
    )
    eGroup2 = models.CharField("Group", max_length=50)
    bRoll2 = models.CharField("Board Roll", max_length=50, default="")
    eResult2 = models.CharField("Result", max_length=50)
    pYear2 = models.CharField("Pass Year", max_length=50, default="")
    insName2 = models.CharField("Institute Name", max_length=50, blank=True)

    # degree1
    dName1 = models.CharField("Degree Name", max_length=50, blank=True)
    uBoard1 = models.CharField("Board/University", max_length=50, blank=True)
    mGroup1 = models.CharField("Institute Name", max_length=50, blank=True)
    bRoll3 = models.CharField("Board Roll", blank=True, max_length=50, default="")
    eResult3 = models.CharField("Result", max_length=50, blank=True)
    pYear3 = models.CharField("Passing Year", blank=True, max_length=50, default="")
    insName3 = models.CharField("Institute Name", max_length=50, blank=True)

    # degree1
    dName2 = models.CharField("Degree Name", max_length=50, blank=True)
    uBoard2 = models.CharField("Board/University", max_length=50, blank=True)
    mGroup2 = models.CharField("Institute Name", max_length=50, blank=True)
    eResult4 = models.CharField("Result", max_length=50, blank=True)
    pYear4 = models.CharField("Passing Year", blank=True, max_length=50, default="")
    insName4 = models.CharField("Institute Name", max_length=50, blank=True)
    qr_code=models.ImageField(upload_to='images/', blank=True)
    def __str__(self):
        return self.sName

    def save(self, *args, **kwargs):
        qrcode_img = qrcode.make(self.sName)
        canvas = Image.new('RGB', (290, 290), 'white')
        canvas.paste(qrcode_img)
        fname = f'qr_code-{self.sName}.png'
        buffer = BytesIO()
        canvas.save(buffer,'PNG')
        self.qr_code.save(fname, File(buffer), save=False)
        canvas.close()
        super().save(*args, **kwargs)