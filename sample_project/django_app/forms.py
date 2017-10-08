#-*- coding: utf-8 -*-
from django import forms

class profileforms(forms.Form):
   first_name = forms.CharField(max_length=30)
   last_name  = forms.CharField(max_length=30)
   city       = forms.CharField(max_length=30)
   taluka     = forms.CharField(max_length=30)
   district   = forms.CharField(max_length=30)
   message    = forms.CharField()
   picture    = forms.ImageField()
   mobile_no  = forms.CharField()
   email      = forms.EmailField()
