from django import forms
from models import Comment

class CommentForm(forms.ModelForm):
    parent = forms.IntegerField(widget=forms.HiddenInput)

    class Meta:
        model = Comment
        fields = ['content']
# place form definition here

