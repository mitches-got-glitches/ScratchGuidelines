# Generated by Django 5.0.4 on 2024-05-06 10:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tableapp', '0004_rename_favoriteguideline_favouriteguideline'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customguidelines',
            name='external_url',
            field=models.URLField(blank=True, max_length=1024, null=True),
        ),
        migrations.AlterField(
            model_name='customguidelines',
            name='name',
            field=models.CharField(max_length=1024),
        ),
    ]
