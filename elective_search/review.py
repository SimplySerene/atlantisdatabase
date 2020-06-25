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
        labels = {
            'elective':'What elective do you want to review?',
            'reviewerName' :'What is your name?',
            'reviewerEmail' : 'What is your email address?',
            'reviewerATLASSemester': 'In what semester did you take the course?',
            'overallScore' : 'On a scale from 1 (really bad) to 10 (amazing) how did you like the course over all?',
            'overallScoreExplanation' : 'Please explain  why you graded the course as you did',
            'prerequisiteKnowledge': 'What did you have to know before entering this course',
            'challengingScore' : 'On a scale 1 (super easy) to 10 (super challenging) how challenging was this course?',
            'challengingScoreExplanation' : 'Please explain why you thought the course was this challenging',
            'workloadScore': 'On a scale 1 (little time) to 10 (a lot of time) how was the workload of this course?',
            'workloadScoreExplanation' : 'Please explain why you experienced the workload to be of this level',
            'additionalComments': 'do you have any additional comments to make?'

        }
