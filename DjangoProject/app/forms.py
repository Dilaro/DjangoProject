"""
Definition of forms.
"""

from django.db import models
from .models import Comment
from django import forms
from django.contrib.auth.forms import AuthenticationForm
#from django.forms.models import _Labels
from django import forms
from django.utils.translation import ugettext_lazy as _
from .models import Blog

class BootstrapAuthenticationForm(AuthenticationForm):
    """Authentication form which uses boostrap CSS."""
    username = forms.CharField(max_length=254,
                               widget=forms.TextInput({
                                   'class': 'form-control',
                                   'placeholder': 'Имя пользователя'}))
    password = forms.CharField(label=_("Password"),
                               widget=forms.PasswordInput({
                                   'class': 'form-control',
                                   'placeholder':'Пароль'}))

class PoolForm(forms.Form):
    name = forms.CharField(label='Ваше имя', min_length=2, max_length=100)
    
    city = forms.CharField(label='Ваш город', min_length=2, max_length=100)
    job = forms.CharField(label='Ваш род занятий', min_length=2, max_length=100)
    choice = forms.ChoiceField(label='Вам понравился наш сайт?',
                               choices=[('1', 'Да'), ('2', 'Нет'),
                                        ('3', 'В основном да, но есть, что добавить')],
                               widget=forms.RadioSelect, initial=1)
    internet = forms.ChoiceField(label='Вы пользуетесь интернетом',
                                 choices=(('1', 'Каждый день'),
                                          ('2', 'Несколько раз в день'),
                                          ('3', 'Несколько раз в неделю'),
                                          ('4', 'Несколько раз в месяц')), initial=1)
    notice = forms.BooleanField(label='Получать новости сайта на e-mail?',
                                required=False)
    email = forms.EmailField(label='Ваш e-mail', min_length=7)
    message = forms.CharField(label='''Напишите здесь, 
                              что можно было бы улучшить 
                              в работе сайта''',
                             widget=forms.Textarea(attrs={'rows': 18, 'cols': 50}))

class CommentForm (forms.ModelForm):
    class Meta:
        model = Comment # используемая модель
        fields = ('text',) # требуется заполнить только поле text
        labels = {'text': "Комментарий"} # метка к полю формы text

class BlogForm(forms.ModelForm):
    class Meta:
        model = Blog
        fields = ('title', 'description', 'content', 'image')
        labels = {'title': "Заголовок", 'description': "Краткое содержание", 'content': "Полное содержание", 'image': "Картинка"}