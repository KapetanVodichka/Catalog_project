# Generated by Django 4.2.4 on 2023-10-06 09:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_alter_user_code'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='code',
            field=models.CharField(blank=True, null=True, verbose_name='код верификации'),
        ),
    ]
