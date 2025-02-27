# Generated by Django 4.1 on 2022-08-09 11:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('PSSApp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ContactUs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=60)),
                ('Organization_Name', models.CharField(max_length=50)),
                ('Mobile', models.CharField(max_length=50)),
                ('Email', models.EmailField(max_length=50)),
                ('Message', models.CharField(max_length=500)),
                ('Submitted_on', models.DateTimeField(null=True)),
            ],
        ),
    ]
