# Generated by Django 3.1.7 on 2021-03-30 06:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('thesis', '0016_research_research_file'),
    ]

    operations = [
        migrations.AlterField(
            model_name='research',
            name='research_file',
            field=models.FileField(blank=True, null=True, upload_to='docs/'),
        ),
    ]
