# Generated by Django 4.2.4 on 2023-08-24 07:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Faculty',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fname', models.CharField(blank=True, max_length=100)),
                ('lname', models.CharField(blank=True, max_length=100)),
                ('email', models.EmailField(blank=True, max_length=254)),
                ('course', models.CharField(blank=True, max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sfname', models.CharField(blank=True, max_length=100)),
                ('slname', models.CharField(blank=True, max_length=100)),
                ('mobile', models.PositiveSmallIntegerField(blank=True)),
                ('faculty', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.faculty')),
            ],
        ),
    ]
