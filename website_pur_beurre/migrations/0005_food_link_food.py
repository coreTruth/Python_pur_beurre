# Generated by Django 2.0.1 on 2018-06-24 15:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website_pur_beurre', '0004_auto_20180624_0329'),
    ]

    operations = [
        migrations.AddField(
            model_name='food',
            name='link_food',
            field=models.CharField(max_length=300, null=True),
        ),
    ]
