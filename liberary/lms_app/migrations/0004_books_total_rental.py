# Generated by Django 5.0.1 on 2024-02-06 19:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lms_app', '0003_rename_author_books_auther_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='books',
            name='total_rental',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True),
        ),
    ]
