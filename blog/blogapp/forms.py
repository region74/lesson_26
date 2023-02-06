from django import forms


class ContactForm(forms.Form):
    name = forms.CharField(label='Название')
    email = forms.EmailField(label='Email')
    message = forms.CharField(label='Сообщение')
