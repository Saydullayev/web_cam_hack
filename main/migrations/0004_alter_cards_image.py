# Generated by Django 5.0.2 on 2024-03-19 11:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_alter_cards_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cards',
            name='image',
            field=models.TextField(),
        ),
    ]