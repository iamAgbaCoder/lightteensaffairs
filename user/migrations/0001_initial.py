# Generated by Django 4.2 on 2023-07-16 20:06

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Registration',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=20)),
                ('last_name', models.CharField(max_length=20)),
                ('email', models.EmailField(max_length=254)),
                ('whatsapp_number', models.CharField(max_length=14)),
                ('is_a_member_of_LTA', models.CharField(max_length=4)),
                ('how_did_you_hear_of_us', models.CharField(max_length=30)),
                ('expectations_for_SOTS', models.TextField()),
                ('date_registered', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name_plural': 'Registrations',
                'ordering': ('-date_registered',),
            },
        ),
        migrations.CreateModel(
            name='Volunteers',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=20)),
                ('last_name', models.CharField(max_length=20)),
                ('email', models.EmailField(max_length=254)),
                ('whatsapp_number', models.CharField(max_length=14)),
            ],
        ),
    ]