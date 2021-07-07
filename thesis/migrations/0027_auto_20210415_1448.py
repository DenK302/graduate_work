# Generated by Django 3.1.7 on 2021-04-15 11:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('thesis', '0026_auto_20210415_1440'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='specialty',
            field=models.CharField(blank=True, choices=[('ИСТЭ', 'Инженер- программист-эколог'), ('ИСТЗ', 'Инженер-программист'), ('ПОД', 'Эколог. Инженер по охране окружающей среды'), ('ЭТЭМ', 'Инженер-энергоменеджер'), ('ЯРБ', 'Инженер'), ('МФ', 'Медицинский физик')], default='ИСТЭ', help_text='Выберите специальность студента', max_length=4, null=True),
        ),
    ]