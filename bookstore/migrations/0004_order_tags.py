# Generated by Django 4.1.5 on 2023-01-25 15:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bookstore', '0003_tag_order_book_order_customer'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='tags',
            field=models.ManyToManyField(to='bookstore.tag'),
        ),
    ]