# Generated by Django 2.2.24 on 2022-06-02

from django.db import migrations


def link_flats_and_owners(apps, schema_editor):
    Flat = apps.get_model('property', 'Flat')
    Owner = apps.get_model('property', 'Owner')

    for owner in Owner.objects.all():
        flat = Flat.objects.filter(owner=owner.name)
        owner.flats.set(flat)
        owner.save()


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0015_auto_20220602_2324'),
    ]

    operations = [
        migrations.RunPython(link_flats_and_owners)
    ]

