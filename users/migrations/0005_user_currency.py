# Generated by Django 4.0a1 on 2021-09-22 16:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_user_language_alter_user_avatar_alter_user_gender'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='currency',
            field=models.CharField(blank=True, choices=[('krw', 'krw'), ('usd', 'usdollar')], max_length=10, null=True),
        ),
    ]