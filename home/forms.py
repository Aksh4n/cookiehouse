from django import forms
from .models import  *
import datetime

class CustomOrderForm(forms.ModelForm):
	class Meta:
		model = Order
		exclude = ()
		feilds = ['phone', 'name', 'email', 'message','image']