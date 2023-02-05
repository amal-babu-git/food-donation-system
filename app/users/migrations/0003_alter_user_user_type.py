# Generated by Django 4.1.6 on 2023-02-05 01:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_rename_first_name_user_full_name_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='user_type',
            field=models.CharField(choices=[('D', 'Donar'), ('A', 'Agent'), ('AD', 'Admin')], default='D', max_length=2),
        ),
    ]
