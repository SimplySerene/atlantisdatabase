# Generated by Django 3.0.6 on 2020-06-24 09:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('elective_search', '0004_auto_20200623_1835'),
    ]

    operations = [
        migrations.AlterField(
            model_name='review',
            name='additionalComments',
            field=models.TextField(max_length=250),
        ),
        migrations.AlterField(
            model_name='review',
            name='challengingScoreExplanation',
            field=models.TextField(max_length=250),
        ),
        migrations.AlterField(
            model_name='review',
            name='overallScoreExplanation',
            field=models.TextField(max_length=250),
        ),
        migrations.AlterField(
            model_name='review',
            name='prerequisiteKnowledge',
            field=models.TextField(max_length=250),
        ),
        migrations.AlterField(
            model_name='review',
            name='workloadScoreExplanation',
            field=models.TextField(max_length=250),
        ),
    ]
