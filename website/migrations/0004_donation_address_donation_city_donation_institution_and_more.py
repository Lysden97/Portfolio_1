# Generated by Django 5.0.7 on 2024-07-16 21:42

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0003_rename_category_institution_categories_donation'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='donation',
            name='address',
            field=models.CharField(blank=True, default='', max_length=255),
        ),
        migrations.AddField(
            model_name='donation',
            name='city',
            field=models.CharField(blank=True, default='', max_length=255),
        ),
        migrations.AddField(
            model_name='donation',
            name='institution',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='website.institution'),
        ),
        migrations.AddField(
            model_name='donation',
            name='phone_number',
            field=models.CharField(blank=True, default='', max_length=20),
        ),
        migrations.AddField(
            model_name='donation',
            name='pick_up_comment',
            field=models.TextField(blank=True, default=''),
        ),
        migrations.AddField(
            model_name='donation',
            name='pick_up_date',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='donation',
            name='pick_up_time',
            field=models.TimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='donation',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='donation',
            name='zip_code',
            field=models.CharField(blank=True, default='', max_length=10),
        ),
    ]
