# Generated by Django 3.0.2 on 2020-02-13 10:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('specializations', '0002_auto_20200204_0740'),
        ('users', '0007_auto_20200207_1032'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='specialization',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='specializations.Specialization'),
        ),
    ]