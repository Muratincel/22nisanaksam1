# Generated by Django 4.2.3 on 2024-08-01 18:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0003_kullanici_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='kullanici',
            name='kullaniciAdi',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]