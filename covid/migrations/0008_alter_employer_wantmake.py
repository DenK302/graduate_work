# Generated by Django 3.2.5 on 2021-07-29 10:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('covid', '0007_auto_20210729_1322'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employer',
            name='wantmake',
            field=models.BooleanField(default=True, help_text='Желает ли сделать'),
        ),
    ]