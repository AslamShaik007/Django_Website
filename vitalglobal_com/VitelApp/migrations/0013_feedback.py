# Generated by Django 4.0.6 on 2022-07-07 12:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('VitelApp', '0012_rename_partners_partner_program'),
    ]

    operations = [
        migrations.CreateModel(
            name='Feedback',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('QualityService', models.CharField(max_length=50)),
                ('CustomerService', models.CharField(max_length=50)),
                ('CompanyName', models.CharField(max_length=50)),
                ('Email', models.EmailField(max_length=50)),
                ('Suggestion', models.CharField(max_length=500)),
            ],
        ),
    ]
