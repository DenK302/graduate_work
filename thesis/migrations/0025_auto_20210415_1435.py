# Generated by Django 3.1.7 on 2021-04-15 11:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('thesis', '0024_auto_20210415_1434'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='student',
            name='specialty',
        ),
        migrations.AlterField(
            model_name='student',
            name='category',
            field=models.CharField(choices=[('Студент', (('ИСТЭ', 'Инженер- программист-эколог'), ('ИСТЗ', 'Инженер-программист'), ('ПОД', 'Эколог. Инженер по охране окружающей среды'), ('ЭТЭМ', 'Инженер-энергоменеджер'), ('ЯРБ', 'Инженер'), ('МФ', 'Медицинский физик'))), ('Магистрант', 'Магистрант'), ('Аспирант', 'Аспирант')], default='Студент', help_text='Категория студента', max_length=10),
        ),
    ]