# Generated by Django 4.0.6 on 2024-03-01 06:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('VitelApp', '0038_ebook_pdf_keyword_ebook_pdf_paragraph_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='setup_plans',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstname', models.CharField(max_length=50)),
                ('lastname', models.CharField(max_length=50)),
                ('password', models.CharField(max_length=255)),
                ('email', models.EmailField(max_length=100)),
                ('mobile', models.CharField(max_length=100)),
                ('quantity', models.IntegerField()),
                ('businessname', models.CharField(max_length=100)),
                ('businessaddress', models.CharField(max_length=500)),
                ('Suite', models.CharField(max_length=100)),
                ('city', models.CharField(max_length=50)),
                ('zipcode', models.CharField(max_length=50)),
                ('state', models.CharField(max_length=50)),
                ('country', models.CharField(max_length=50)),
                ('dids', models.CharField(max_length=100)),
                ('submitted_on', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
