# Generated by Django 3.0.2 on 2020-03-22 19:32

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Waitlist',
            fields=[
                ('number', models.AutoField(primary_key=True, serialize=False)),
                ('guests', models.IntegerField()),
                ('lastname', models.CharField(max_length=128)),
                ('catagory', models.CharField(max_length=64)),
            ],
            options={
                'verbose_name': 'waitlist',
                'verbose_name_plural': 'waitlist',
            },
        ),
    ]