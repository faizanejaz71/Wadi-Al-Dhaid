# Generated by Django 5.1.6 on 2025-03-01 11:12

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Visa', '0002_visadetails'),
    ]

    operations = [
        migrations.CreateModel(
            name='VisaRequirements',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('person_type', models.CharField(max_length=100)),
                ('visa_details', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Visa.visadetails')),
            ],
        ),
        migrations.CreateModel(
            name='VisaDocuments',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('document_name', models.CharField(max_length=100)),
                ('visa_requirements', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Visa.visarequirements')),
            ],
        ),
    ]
