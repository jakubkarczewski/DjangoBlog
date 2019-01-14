from django import forms

from .models import Post, Comment
from django.utils.translation import ugettext_lazy as _


class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ('title', 'text',)
        labels = {
        	'title': _('Tytuł'),
        	'text': _('Tekst')
        }


class CommentForm(forms.ModelForm):

    class Meta:
        model = Comment
        fields = ('author', 'text',)
        labels = {
        	'author': _('Autor'),
        	'text': _('Tekst')
        }