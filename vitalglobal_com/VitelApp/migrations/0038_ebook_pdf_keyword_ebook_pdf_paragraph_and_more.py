# Generated by Django 4.0.6 on 2024-02-28 10:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('VitelApp', '0037_request_demo_now_name_request_demo_now_phonenumber'),
    ]

    operations = [
        migrations.AddField(
            model_name='ebook_pdf',
            name='keyword',
            field=models.CharField(blank=True, default='Vitelglobal', max_length=256, null=True),
        ),
        migrations.AddField(
            model_name='ebook_pdf',
            name='paragraph',
            field=models.CharField(blank=True, max_length=256, null=True),
        ),
        migrations.AddField(
            model_name='whitepaper_pdf',
            name='keyword',
            field=models.CharField(blank=True, default='Vitelglobal', max_length=256, null=True),
        ),
        migrations.AddField(
            model_name='whitepaper_pdf',
            name='paragraph',
            field=models.CharField(blank=True, max_length=256, null=True),
        ),
    ]
