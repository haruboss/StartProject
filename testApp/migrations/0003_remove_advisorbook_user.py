# Generated by Django 3.1.1 on 2021-05-02 10:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('testApp', '0002_advisorbook'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='advisorbook',
            name='user',
        ),
    ]
