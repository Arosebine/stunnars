# Generated by Django 3.2 on 2021-06-10 17:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('choice', '0005_alter_order_event_desire'),
    ]

    operations = [
        migrations.CreateModel(
            name='ContactForm',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('email', models.EmailField(max_length=254)),
                ('message', models.CharField(max_length=1000)),
            ],
        ),
        migrations.DeleteModel(
            name='Message',
        ),
        migrations.DeleteModel(
            name='Order',
        ),
    ]