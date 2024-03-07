from django import forms
from django.core.exceptions import ValidationError
from .models import InterviewDocument


class InterviewDocumentForm(forms.ModelForm):
    class Meta:
        model = InterviewDocument
        fields = ['language', 'cv', 'job_description']
    
    def clean_cv(self):
        cv = self.cleaned_data.get('cv')
        if not cv.name.endswith('.pdf'):
            raise ValidationError("Invalid file type for CV. PDF required.")
        if cv.size > 1024*1024*5: # 5MB limit
            raise ValidationError("CV file too large. Size should not exceed 5MB.")
        return cv

    def clean_job_description(self):
        job_description = self.cleaned_data.get('job_description')
        if not job_description.name.endswith('.pdf'):
            raise ValidationError("Invalid file type for job description. PDF required.")
        if job_description.size > 1024*1024*5: # 5MB limit
            raise ValidationError("Job description file too large. Size should not exceed 5MB.")
        return job_description