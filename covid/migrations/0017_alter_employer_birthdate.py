# Generated by Django 3.2.5 on 2021-08-04 05:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('covid', '0016_alter_employer_wantmaketype'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employer',
            name='birthdate',
            field=models.CharField(blank=True, help_text='Дата рождения', max_length=20, null=True),
        ),
    ]