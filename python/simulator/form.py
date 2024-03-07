from django import forms
from .models import InterviewDocument


class InterviewDocumentForm(forms.ModelForm):
    class Meta:
        model = InterviewDocument
        fields = ['language', 'cv', 'job_description']
