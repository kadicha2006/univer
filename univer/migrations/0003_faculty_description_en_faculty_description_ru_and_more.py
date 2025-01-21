# Generated by Django 5.1.5 on 2025-01-21 16:33

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('univer', '0002_alter_schedule_day_of_week'),
    ]

    operations = [
        migrations.AddField(
            model_name='faculty',
            name='description_en',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='faculty',
            name='description_ru',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='faculty',
            name='name_en',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='faculty',
            name='name_ru',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='professor',
            name='bio_en',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='professor',
            name='bio_ru',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='professor',
            name='department_en',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='univer.faculty'),
        ),
        migrations.AddField(
            model_name='professor',
            name='department_ru',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='univer.faculty'),
        ),
        migrations.AddField(
            model_name='professor',
            name='title_en',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='professor',
            name='title_ru',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='professor',
            name='user_en',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='professor', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='professor',
            name='user_ru',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='professor', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='student',
            name='department_en',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='univer.faculty'),
        ),
        migrations.AddField(
            model_name='student',
            name='department_ru',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='univer.faculty'),
        ),
        migrations.AddField(
            model_name='student',
            name='user_en',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='student',
            name='user_ru',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
