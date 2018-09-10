from django import forms

from .models import Comment

# class CommentForm(forms.Form):
#   comment_text = forms.CharField(label="comment_text", max_length=200)

class CommentForm(forms.ModelForm):
  
  class Meta:
    model = Comment
    exclude = ('comment_date', 'sender_ip')