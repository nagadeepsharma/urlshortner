# Generated by Django 3.2.2 on 2021-11-12 06:33

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='shorturl',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('original_url', models.URLField()),
                ('short_query', models.CharField(max_length=20)),
                ('visits', models.IntegerField(default=0)),
            ],
        ),
    ]
