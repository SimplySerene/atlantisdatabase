from django import forms
from django.db import models
from .models import Elective, Review
from django.forms import ModelForm

class user_review_form(forms.ModelForm):
    class Meta: 
        model = Review
        fields = [
            'elective',
            'reviewerName',
            'reviewerEmail',
            'overallScore',
            'reviewerATLASSemester',
            'overallScore',
            'overallScoreExplanation',
            'prerequisiteKnowledge',
            'challengingScore',
            'challengingScoreExplanation',
            'workloadScore',
            'workloadScoreExplanation',
            'additionalComments'
        ]

