# Generated by Django 2.2.2 on 2019-07-01 15:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('django_rossvyaz', '0003_phonecode_mnc'),
    ]

    operations = [
        migrations.AlterField(
            model_name='phonecode',
            name='mnc',
            field=models.CharField(db_index=True, max_length=32, verbose_name='Mobile Network Code'),
        ),
    ]