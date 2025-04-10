# Generated by Django 4.2 on 2025-04-05 11:49

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='OrganizationProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('photo', models.ImageField(blank=True, upload_to='users/%Y/%m/%d/')),
                ('registration_number', models.CharField(max_length=20, unique=True)),
                ('phone_number', models.CharField(max_length=15)),
                ('registration_certificate', models.FileField(blank=True, upload_to='ngo_docs/%Y/%m/%d/')),
                ('is_verified', models.BooleanField(default=False)),
                ('website', models.URLField(blank=True)),
                ('annual_budget', models.DecimalField(blank=True, decimal_places=2, max_digits=14, null=True)),
                ('registration_date', models.DateField(blank=True, null=True)),
                ('date_established', models.DateField(blank=True, null=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
