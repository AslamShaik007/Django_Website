# Generated by Django 4.1.4 on 2023-01-04 07:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('VitelApp', '0029_alter_contactus_submitted_on'),
    ]

    operations = [
        migrations.AddField(
            model_name='contactus',
            name='HowYouKnow',
            field=models.CharField(default=None, max_length=500),
            preserve_default=False,
        ),
    ]
