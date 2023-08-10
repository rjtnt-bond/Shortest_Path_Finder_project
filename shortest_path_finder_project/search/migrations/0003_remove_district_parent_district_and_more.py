# Generated by Django 4.2 on 2023-06-13 15:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('search', '0002_distance_district_delete_graphnode_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='district',
            name='parent_district',
        ),
        migrations.AddField(
            model_name='district',
            name='parent_districts',
            field=models.ManyToManyField(blank=True, related_name='child_districts', to='search.district'),
        ),
    ]