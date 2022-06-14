# Generated by Django 2.2.24 on 2022-06-02

from django.db import migrations


def fill_owner_model(apps, schema_editor):
    Flat = apps.get_model('property', 'Flat')
    Owner = apps.get_model('property', 'Owner')
    for flat in Flat.objects.all().iterator():
        Owner.objects.get_or_create(
            name=flat.owner,
            phonenumber=flat.owners_phonenumber,
            pure_phonenumber=flat.owner_pure_phone
        )


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0013_auto_20220602_2231'),
    ]

    operations = [
        migrations.RunPython(fill_owner_model)
    ]