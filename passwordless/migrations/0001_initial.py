# Generated by Django 4.1.4 on 2023-01-08 08:14

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='AuthFailure',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hash', models.CharField(db_index=True, editable=False, max_length=64)),
                ('created', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name': 'Passwordless failure',
                'ordering': ('-created',),
            },
        ),
        migrations.CreateModel(
            name='AuthRequest',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('email', models.EmailField(db_index=True, editable=False, max_length=254)),
                ('type', models.CharField(choices=[('E', 'Change Email'), ('L', 'Login')], editable=False, max_length=1)),
                ('hash', models.CharField(blank=True, db_index=True, editable=False, max_length=64, null=True)),
                ('otp', models.CharField(blank=True, editable=False, max_length=24, null=True)),
                ('email_sent', models.BooleanField(default=False, editable=False)),
                ('is_used', models.BooleanField(default=False, editable=False)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('user', models.ForeignKey(blank=True, editable=False, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Passwordless request',
                'ordering': ('-created',),
            },
        ),
    ]
