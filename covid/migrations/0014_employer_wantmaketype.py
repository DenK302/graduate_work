# Generated by Django 3.2.5 on 2021-08-02 11:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('covid', '0013_alter_employer_liveplace'),
    ]

    operations = [
        migrations.AddField(
            model_name='employer',
            name='wantmaketype',
            field=models.CharField(blank=True, help_text='Тип прививки', max_length=50, null=True),
        ),
    ]