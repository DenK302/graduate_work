# Generated by Django 3.2.5 on 2021-07-29 10:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('covid', '0009_alter_employer_wantmake'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employer',
            name='vactinationfull',
            field=models.BooleanField(default=True, help_text='Полная вакцинация'),
        ),
    ]
