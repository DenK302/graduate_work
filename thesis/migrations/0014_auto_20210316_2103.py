# Generated by Django 3.1.7 on 2021-03-16 18:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('thesis', '0013_auto_20210316_1623'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='category',
            field=models.CharField(choices=[('С', 'Студент'), ('М', 'Магистрант'), ('А', 'Аспирант')], default='С', help_text='Категория студента', max_length=10),
        ),
    ]