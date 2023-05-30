# Generated by Django 3.2.16 on 2023-02-21 09:49

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='version',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, help_text='時間戳記，為最初建立資料的時間。')),
                ('updated_at', models.DateTimeField(auto_now=True, help_text='時間戳記，為每次更新資料時間。')),
                ('version', models.CharField(max_length=10, unique=True)),
                ('content', models.TextField()),
                ('activate', models.BooleanField(default=True)),
            ],
            options={
                'verbose_name_plural': 'System Version - 系統版本歷程記錄',
                'db_table': 'log_version',
            },
        ),
    ]
