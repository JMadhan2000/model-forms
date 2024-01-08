from django import forms
from app.models import *

class TopicForm(forms.ModelForm):
    class Meta():
        model = Topic
        fields= '__all__'


class WebPageForm(forms.ModelForm):
    class Meta():
        model = WebPage
        fields='__all__'
        #fields=['Name','Url','Email']
        #exclude=['Name','Url']
        #labels={'Name':'Na','Url':'U'}
        #widgets={'Url':forms.PasswordInput}    #url will show the data as pass while writing
        



class AccessRecordForm(forms.ModelForm):
    class Meta():
        model = AccessRecord
        fields='__all__'