# Generated by Django 3.1.7 on 2021-03-16 09:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('thesis', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='research',
            options={'verbose_name': 'Исследовательская работа', 'verbose_name_plural': 'Исследовательские работы'},
        ),
        migrations.AlterModelOptions(
            name='student',
            options={'verbose_name': 'Студент', 'verbose_name_plural': 'Студенты'},
        ),
        migrations.AlterModelOptions(
            name='teacher',
            options={'verbose_name': 'Преподаватель', 'verbose_name_plural': 'Преподаватели'},
        ),
        migrations.AlterModelOptions(
            name='work',
            options={'verbose_name': 'Работа', 'verbose_name_plural': 'Работы'},
        ),
    ]