# Generated by Django 3.1.7 on 2021-03-17 10:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('thesis', '0014_auto_20210316_2103'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='category',
            field=models.CharField(choices=[('С', 'Студент'), ('М', 'Магистрант'), ('А', 'Аспирант')], default='С', help_text='Категория студента', max_length=1),
        ),
        migrations.AlterField(
            model_name='teacher',
            name='email',
            field=models.CharField(blank=True, help_text='Введите электронную почту руководителя', max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='teacher',
            name='phone_number',
            field=models.CharField(blank=True, help_text='Введите номер телефона руководителя', max_length=18, null=True),
        ),
    ]
