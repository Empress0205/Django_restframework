# Generated by Django 5.2.4 on 2025-07-25 11:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employees', '0002_employee_id_alter_employee_employee_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='employee',
            name='id',
        ),
        migrations.AlterField(
            model_name='employee',
            name='employee_id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
