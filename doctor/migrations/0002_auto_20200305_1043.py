# Generated by Django 3.0.2 on 2020-03-05 10:43

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('appointment', '0003_auto_20200305_1043'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('doctor', '0001_initial'),
        ('patient', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='shareddocument',
            name='doctor',
            field=models.ForeignKey(limit_choices_to={'user_type': 'doctor'}, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='shareddocument',
            name='shared_document',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='shareddoc', to='patient.Document'),
        ),
        migrations.AddField(
            model_name='feedback',
            name='appointment',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='appointment.Appointment'),
        ),
        migrations.AddField(
            model_name='feedback',
            name='doctor',
            field=models.ForeignKey(limit_choices_to={'user_type': 'doctor'}, on_delete=django.db.models.deletion.CASCADE, related_name='doctor_feedback', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='feedback',
            name='patient',
            field=models.ForeignKey(limit_choices_to={'user_type': 'patient'}, on_delete=django.db.models.deletion.CASCADE, related_name='patient_feedback', to=settings.AUTH_USER_MODEL),
        ),
    ]
