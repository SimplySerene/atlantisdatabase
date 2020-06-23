from django.db import models

# Models for the elective database

from django.db import models
from django.forms import ModelForm


def search(title='', ec='', utblock='', language='', electivetype='', osiriscode='', keywords=''):
    """
    Returns a queryset containing electives that meet the search requirements. `keywords` searches for
    the given keywords in the elective description.
    """
    electives = Elective.objects.all()
    if title != '':
        electives = electives.filter(title__icontains=title)
    if ec != '':
        electives = electives.filter(numberOfECs__exact=ec)
    if utblock != '':
        electives = electives.filter(utBlock__exact=utblock)
    if language != '':
        electives = electives.filter(language__exact=language)
    if electivetype != '':
        electives = electives.filter(electiveType__exact=electivetype)
    if osiriscode != '':
        electives = electives.filter(osirisCode__iexact=osiriscode)
    if keywords != '':
        for word in keywords.split():
            electives = electives.filter(courseDescription__icontains=word)

    return electives


class Elective(models.Model):
    # Entry fields:
    # Title of the elective
    title = models.CharField(max_length=100)
    # OSIRIS Code used to identify the elective on osiris.utwente.nl
    osirisCode = models.IntegerField()
    # Number of credits gained from the course
    numberOfECs = models.DecimalField(max_digits=3, decimal_places=1)
    # Elective type
    ELECTIVE_TYPE_CHOICES = [
        ('UT', 'Course at the UT'),
        ('MODULE', 'Full module at the UT'),
        ('ONLINE', 'Online Course'),
        ('OTHER', 'Other')
    ]
    electiveType = models.CharField(choices=ELECTIVE_TYPE_CHOICES, max_length=6)
    LANGUAGE_CHOICES = [
        ('NL', 'Dutch'),
        ('EN', 'English'),
    ]
    # Language in which the course is given
    language = models.CharField(choices=LANGUAGE_CHOICES, max_length=2)
    UT_BLOCK_CHOICES = [
        ('1A', 'Quartile 1'),
        ('1B', 'Quartile 2'),
        ('2A', 'Quartile 3'),
        ('2B', 'Quartile 4'),
    ]
    # Quartile in which the course is given
    utBlock = models.CharField(choices=UT_BLOCK_CHOICES, max_length=2)
    # Course Description
    courseDescription = models.TextField()
    # Entry requirements
    entryRequirements = models.TextField()
    # Name of the contact person
    contactPersonName = models.CharField(max_length=35)
    # E-mail of the contact person
    contactPersonEmail = models.EmailField()

    def __str__(self):
        return self.title


# Model for a review related to an elective
class Review(models.Model):
    # Specify relationship with the elective this review is for. If the elective is deleted,
    # so are all reviews.
    elective = models.ForeignKey(Elective, on_delete=models.CASCADE)
    # Choices from 1 to 10.
    SCORE_CHOICES_1_TO_10 = [(a, a) for a in range(1, 11)]

    # Entry fields:
    # Name of the reviewer
    reviewerName = models.CharField(max_length=35)
    # Email address of reviewer
    reviewerEmail = models.EmailField()
    # What ATLAS semester was the reviewer in when taking this course
    SEMESTER_CHOICES = [(str(a), "Semester " + str(a)) for a in range(1, 7)]
    reviewerATLASSemester = models.CharField(choices=SEMESTER_CHOICES, max_length=1)
    # Overall score given for the course and explanation for the score.
    overallScore = models.IntegerField(choices=SCORE_CHOICES_1_TO_10)
    overallScoreExplanation = models.TextField(max_length=250)
    # What pre-knowledge was needed.
    prerequisiteKnowledge = models.TextField(max_length=250)
    # How challenging the course was
    challengingScore = models.IntegerField(choices=SCORE_CHOICES_1_TO_10)
    challengingScoreExplanation = models.TextField(max_length=250)
    # How the work load was for the course
    workloadScore = models.IntegerField(choices=SCORE_CHOICES_1_TO_10)
    workloadScoreExplanation = models.TextField(max_length=250)
    # Additional Comments
    additionalComments = models.TextField(max_length=250)
    def __str__(self):
        return self.reviewerName
