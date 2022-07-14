# -*-coding: UTF-8 -*-
"""
Auther:Zhou Qinzhi
Date: 2022.07.10
"""
from django import forms

class UploadFileForm(forms.Form):
    title = forms.CharField(max_length=50)
    file = forms.FileField