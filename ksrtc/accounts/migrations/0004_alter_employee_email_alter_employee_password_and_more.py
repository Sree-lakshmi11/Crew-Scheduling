# Generated by Django 5.0.3 on 2024-04-06 12:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_alter_employee_email_alter_employee_username'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='email',
            field=models.EmailField(blank=True, max_length=254, verbose_name='email address'),
        ),
        migrations.AlterField(
            model_name='employee',
            name='password',
            field=models.CharField(max_length=128),
        ),
        migrations.AlterField(
            model_name='employee',
            name='username',
            field=models.CharField(max_length=150, unique=True),
        ),
    ]