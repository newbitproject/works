# Generated by Django 2.2.1 on 2019-05-21 09:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('newsapp', '0007_auto_20190521_1801'),
    ]

    operations = [
        migrations.CreateModel(
            name='TotalDb',
            fields=[
                ('id', models.TextField(primary_key=True, serialize=False)),
                ('date', models.TextField(blank=True, null=True)),
                ('title', models.TextField(blank=True, null=True)),
                ('content', models.TextField(blank=True, null=True)),
                ('category', models.TextField(blank=True, null=True)),
                ('date_tmp', models.BigIntegerField(blank=True, null=True)),
                ('tokenized_doc', models.TextField(blank=True, null=True)),
                ('tokenized_title', models.TextField(blank=True, null=True)),
                ('query', models.TextField(blank=True, null=True)),
            ],
            options={
                'db_table': 'total_db',
                'managed': False,
            },
        ),
        migrations.DeleteModel(
            name='total_db',
        ),
    ]