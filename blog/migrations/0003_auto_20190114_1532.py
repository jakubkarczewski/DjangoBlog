# Generated by Django 2.1.5 on 2019-01-14 14:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_post_author'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='post',
            options={'permissions': (('can_delete', 'Can delete posts.'),)},
        ),
    ]
