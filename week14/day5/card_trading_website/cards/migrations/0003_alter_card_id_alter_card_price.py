# Generated by Django 4.2.3 on 2023-07-25 13:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cards', '0002_alter_card_current_owner_alter_card_previous_owner_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='card',
            name='id',
            field=models.CharField(max_length=255, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='card',
            name='price',
            field=models.IntegerField(default=839),
        ),
    ]
