# Generated by Django 3.0.2 on 2020-02-17 07:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_auto_20200203_0538'),
        ('hospital', '0007_auto_20200210_1020'),
    ]

    operations = [
        migrations.CreateModel(
            name='Holidays',
            fields=[
                ('basemodel_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='app.BaseModel')),
                ('date', models.DateField()),
                ('name', models.CharField(max_length=200)),
            ],
            options={
                'abstract': False,
            },
            bases=('app.basemodel',),
        ),
    ]