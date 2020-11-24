from .models import CommentB, Post
from django import forms


class CommentForm(forms.ModelForm):
    class Meta:
        model = CommentB
        fields = ('body',)

