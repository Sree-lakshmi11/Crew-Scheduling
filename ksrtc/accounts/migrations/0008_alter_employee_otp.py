# Generated by Django 5.0.3 on 2024-04-06 20:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0007_alter_employee_otp_alter_employee_phone_number'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='otp',
            field=models.CharField(blank=True, max_length=6, null=True),
        ),
    ]
