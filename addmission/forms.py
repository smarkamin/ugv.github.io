from email.policy import default
from logging import PlaceHolder
from django.forms import ModelForm
from django import forms
from .models import personalInfo



class pForm(ModelForm):
    class Meta:
        model = personalInfo
        fields = (
            "inProgram",
            "shift",
            "session",
            "section",
            "sName",
            "cNum",
            "email",
            "gender",
            "bCert",
            "image",
            "religion",
            "doBirth",
            "pAds",
            "bGroup",
            "nationality",
            "quota",
            #family
            "fName",
            "fcNum",
            "fOccu",
            "fEmail",
            "mName",
            "mcNum",
            "mOccu",
            "mEmail",
            #ed1
            "eTitle1",
            "board1",
            "eGroup1",
            "bRoll1",
            "eResult1",
            "pYear1",
            "insName1",
            #edu2
            "eTitle2",
            "board2",
            "eGroup2",
            "bRoll2",
            "eResult2",
            "pYear2",
            "insName2",
            #d1
            "dName1",
            "uBoard1",
            "mGroup1",
            "bRoll3",
            "eResult3",
            "pYear3",
            "insName3",
            #d2
            "dName2",
            "uBoard2",
            "mGroup2",
            "eResult4",
            "pYear4",
            "insName4",
        )
        widgets = {
          "fName": forms.TextInput(
                attrs={"class": "form-control", "placeholder": "Father's Name"}
            ),
            "fcNum": forms.TextInput(
                attrs={"class": "form-control", "placeholder": "Father Contract"}
            ),
            "fOccu": forms.TextInput(
                attrs={"class": "form-control", "placeholder": "Father Occupation"}
            ),
            "fEmail": forms.EmailInput(
                attrs={"class": "form-control", "placeholder": "Father Email"}
            ),
            "mName": forms.TextInput(
                attrs={"class": "form-control", "placeholder": "Mother Name"}
            ),
            "mcNum": forms.TextInput(
                attrs={"class": "form-control", "placeholder": "MOther Contract Number"}
            ),
            "mOccu": forms.TextInput(
                attrs={"class": "form-control", "placeholder": "Mother Occupation"}
            ),
            "mEmail": forms.EmailInput(
                attrs={"class": "form-control", "placeholder": "Mother Email"}
            ),
            "inProgram": forms.Select(
                attrs={"class": "form-select", "placeholder": "Select One"}
            ),
            "shift": forms.Select(
                attrs={"class": "form-select", "placeholder": "Select One"}
            ),
            "session": forms.Select(
                attrs={"class": ".form-select", "placeholder": "Select One"}
            ),
            "sName": forms.TextInput(
                attrs={"class": "form-control", "placeholder": "Student Name"}
            ),
            "cNum": forms.TextInput(
                attrs={"class": "form-control", "placeholder": "Contract Number"}
            ),
            "email": forms.EmailInput(
                attrs={"class": "form-control", "placeholder": "Email"}
            ),
            "gender": forms.Select(
                attrs={"class": "form-control", "placeholder": "Select One"}
            ),
            "bCert": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Birth Certificate Number",
                }
            ),
            "religion": forms.Select(
                attrs={"class": "form-select", "placeholder": "Select One"}
            ),
            "doBirth": forms.TextInput(
                attrs={"class": "form-control", "placeholder": "DD/MM/YY"}
            ),
            "pAds": forms.TextInput(
                attrs={"class": "form-control", "placeholder": "Present address"}
            ),
            "bGroup": forms.Select(
                attrs={"class": "form-select", "placeholder": "Select One"}
            ),
            "nationality": forms.TextInput(
                attrs={"class": "form-control", "placeholder": "Nationality"},
            ),
            "quota": forms.Select(
                attrs={"class": "form-select", "placeholder": "Select One"}
            ),
            "eTitle1": forms.Select(
                attrs={
                    "class": "form-select",
                    "placeholder": "Select One",
                }
            ),
            "board1": forms.Select(
                attrs={"class": "form-select", "placeholder": "Select One"}
            ),
            "eGroup1": forms.TextInput(
                attrs={"class": "form-control", "placeholder": "Group"}
            ),
            "bRoll1": forms.TextInput(
                attrs={"class": "form-control", "placeholder": "Board Roll"}
            ),
            "eResult1": forms.TextInput(
                attrs={"class": "form-control", "placeholder": "Result"}
            ),
            "pYear1": forms.TextInput(
                attrs={"class": "form-control", "placeholder": "Pass Year"}
            ),
            "insName1": forms.TextInput(
                attrs={"class": "form-control", "placeholder": "Institute Name"}
            ),
            "eTitle2": forms.Select(
                attrs={"class": "form-control", "placeholder": "Select One"}
            ),
            "board2": forms.Select(
                attrs={"class": "form-control", "placeholder": "Select One"}
            ),
            "eGroup2": forms.TextInput(
                attrs={"class": "form-control", "placeholder": "Group"}
            ),
            "bRoll2": forms.TextInput(
                attrs={"class": "form-control", "placeholder": "Board Roll"}
            ),
            "eResult2": forms.TextInput(
                attrs={"class": "form-control", "placeholder": "Result"}
            ),
            "pYear2": forms.TextInput(
                attrs={"class": "form-control", "placeholder": "Pass Year"}
            ),
            "insName1": forms.TextInput(
                attrs={"class": "form-control", "placeholder": "Institute Name"}
            ),
            "dName1": forms.TextInput(
                attrs={"class": "form-control", "placeholder": "Degree Title"}
            ),
            "uBoard1": forms.TextInput(
                attrs={"class": "form-control", "placeholder": "Board/Unversity"}
            ),
            "mGroup1": forms.TextInput(
                attrs={"class": "form-control", "placeholder": "Group"}
            ),
            "bRoll3": forms.TextInput(
                attrs={"class": "form-control", "placeholder": "Board Roll"}
            ),
            "eResult3": forms.TextInput(
                attrs={"class": "form-control", "placeholder": "Result"}
            ),
            "pYear3": forms.TextInput(
                attrs={"class": "form-control", "placeholder": "Pass Year"}
            ),
            "insName3": forms.TextInput(
                attrs={"class": "form-control", "placeholder": "Institute Name"}
            ),
            "dName2": forms.TextInput(
                attrs={"class": "form-control", "placeholder": "Degree Title"}
            ),
            "uBoard2": forms.TextInput(
                attrs={"class": "form-control", "placeholder": "Board/University"}
            ),
            "mGroup2": forms.TextInput(
                attrs={"class": "form-control", "placeholder": "Group"}
            ),
            "eResult4": forms.TextInput(
                attrs={"class": "form-control", "placeholder": "Result"}
            ),
            "pYear4": forms.TextInput(
                attrs={"class": "form-control", "placeholder": "Pass Year"}
            ),
            "insName4": forms.TextInput(
                attrs={"class": "form-control", "placeholder": "Institute Name"}
            ),
        }


