# Generated by Django 2.1 on 2018-08-27 20:16

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Record',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('patient_name', models.CharField(max_length=100)),
                ('DOB', models.CharField(max_length=100)),
                ('phone_number', models.CharField(max_length=20)),
                ('PCP', models.CharField(blank=True, max_length=100)),
                ('insurance', models.CharField(blank=True, max_length=500)),
                ('medical_history', models.TextField(blank=True)),
                ('drug_allergies', models.TextField(blank=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('last_modified', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
