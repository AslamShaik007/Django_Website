
from captcha.fields import CaptchaField
from django import forms

class CaptchaForm(forms.Form):
    captcha = CaptchaField()
    # captcha = CaptchaField(widget=forms.TextInput(attrs={'class': 'captcha'}))
