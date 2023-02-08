from django import forms
from .models import Post
from .models import Tag


class ContactForm(forms.Form):
    name = forms.CharField(label='Название')
    email = forms.EmailField(label='Email')
    message = forms.CharField(label='Сообщение')


class PostForm(forms.ModelForm):
    # name = forms.CharField(label='Название поста',widget=forms.Textarea())
    name = forms.CharField(label='Название поста',
                           widget=forms.TextInput(attrs={'placeholder': 'Name', 'class': 'form-control'}))
    # чек боксы
    tags = forms.ModelMultipleChoiceField(queryset=Tag.objects.all(),
                                          widget=forms.CheckboxSelectMultiple())

    class Meta:
        model = Post
        fields = '__all__'
        # fields = ('name', 'category')
        # скрыть поле
        # exclude = ('tags',)
