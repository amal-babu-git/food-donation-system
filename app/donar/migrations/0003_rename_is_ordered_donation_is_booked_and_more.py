# Generated by Django 4.1.6 on 2023-02-07 12:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('donar', '0002_donation_remark'),
    ]

    operations = [
        migrations.RenameField(
            model_name='donation',
            old_name='is_ordered',
            new_name='is_booked',
        ),
        migrations.AddField(
            model_name='donation',
            name='is_collected',
            field=models.BooleanField(default=False),
        ),
    ]