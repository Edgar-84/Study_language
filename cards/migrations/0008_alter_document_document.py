# Generated by Django 4.1.1 on 2022-11-20 17:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cards', '0007_alter_document_document'),
    ]

    operations = [
        migrations.AlterField(
            model_name='document',
            name='document',
            field=models.FileField(upload_to='documents/%Y/%m/%d/'),
        ),
    ]
