# Generated by Django 3.1.7 on 2021-04-02 08:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('thesis', '0018_auto_20210330_1140'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='student',
            name='specialty',
        ),
        migrations.AddField(
            model_name='student',
            name='mag_specialty',
            field=models.CharField(choices=[('Экол', 'Экология'), ('МБД', 'Медико-биологическое дело'), ('МФ', 'Медицинская физика'), ('БИНФ', 'Биоинформатика')], help_text='Выберите специальность магистранта', max_length=5, null=True),
        ),
        migrations.AddField(
            model_name='student',
            name='student_specialty',
            field=models.CharField(choices=[('ИСТЭ', 'Информационные системы и технологии (в экологии)'), ('ИСТЗ', 'Информационные системы и технологии (в здравоохранении)'), ('ПОД1', 'Природоохранная деятельность (экологический менеджмент и экспертиза)'), ('ПОД2', 'Природоохранная деятельность (экологический мониторинг)'), ('ЭТЭМ', 'Энергоэффективные технологии и энергетический менеджмент'), ('ЯиРБ', 'Ядерная и радиационная безопасность'), ('МФ', 'Медицинская физика')], help_text='Выберите специальность студента', max_length=5, null=True),
        ),
        migrations.AddField(
            model_name='teacher',
            name='title',
            field=models.CharField(blank=True, help_text='Введите звание руководителя', max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='research',
            name='docfile',
            field=models.FileField(blank=True, null=True, upload_to=''),
        ),
    ]
