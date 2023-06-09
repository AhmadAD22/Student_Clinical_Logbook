# Generated by Django 4.1.7 on 2023-03-29 22:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('action', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ActionInformation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('place', models.CharField(max_length=250)),
                ('date', models.DateField()),
                ('patient_type', models.CharField(max_length=50)),
                ('complexity_level', models.CharField(choices=[('L', 'Low'), ('M', 'Medium'), ('H', 'High')], max_length=1)),
                ('status_number', models.PositiveSmallIntegerField(choices=[(1, 1), (2, 2), (3, 3), (4, 4)])),
                ('Action', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='action.action')),
            ],
        ),
    ]
