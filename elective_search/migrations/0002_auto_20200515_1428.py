# Generated by Django 3.0.5 on 2020-05-15 12:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('elective_search', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='elective',
            name='courseDescription',
            field=models.TextField(default=''),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='elective',
            name='electiveType',
            field=models.CharField(choices=[('UT', 'Course at the UT'), ('MOD', 'Full module at the UT'), ('ONLINE', 'Online Course'), ('OTHER', 'Other')], max_length=6),
        ),
    ]
