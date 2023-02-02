# Generated by Django 4.1.5 on 2023-02-01 09:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apl', '0004_alter_application_urgency'),
    ]

    operations = [
        migrations.AlterField(
            model_name='application',
            name='urgency',
            field=models.CharField(choices=[('не срочно', 'Не срочно'), ('срочно', 'Срочно'), ('очень срочно', 'Очень срочно')], default='не срочно', max_length=20),
        ),
    ]
