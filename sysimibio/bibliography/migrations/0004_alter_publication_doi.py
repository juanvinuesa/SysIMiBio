# Generated by Django 3.2 on 2021-07-16 15:31

from django.db import migrations, models
import sysimibio.bibliography.validators


class Migration(migrations.Migration):

    dependencies = [
        ('bibliography', '0003_publication_created_by'),
    ]

    operations = [
        migrations.AlterField(
            model_name='publication',
            name='DOI',
            field=models.CharField(blank=True, max_length=30, validators=[sysimibio.bibliography.validators.validate_doi_prefix, sysimibio.bibliography.validators.validate_doi_slash], verbose_name='DOI'),
        ),
    ]
