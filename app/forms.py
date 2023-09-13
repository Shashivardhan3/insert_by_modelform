from django import forms

from app.models import *


class TopicForm(forms.ModelForm):
    class Meta:
        model=Topic
        fields='__all__'



class WebpageForm(forms.ModelForm):
    class Meta:
        model=Webpage
        fields='__all__'
        fields=['topic_name','name','email']
        exclude=['name']
        help_texts={'topic_name':'should not start with integer,numbers','name':'Only Alphabets'}
        labels={'topic_name':"TN",'name':'N'}
        widgets={'email':forms.PasswordInput,'name':forms.Textarea}
