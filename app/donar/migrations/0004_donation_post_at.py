# Generated by Django 4.1.6 on 2023-02-23 02:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('donar', '0003_rename_is_ordered_donation_is_booked_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='donation',
            name='post_at',
            field=models.DateTimeField(auto_now=True),
        ),
    ]