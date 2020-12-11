# Generated by Django 3.1.3 on 2020-12-11 11:02

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(help_text='NAME', max_length=50)),
                ('contact_address', models.CharField(help_text='NAME', max_length=50)),
                ('email', models.CharField(help_text='NAME', max_length=50)),
                ('mobile', models.CharField(help_text='NAME', max_length=50)),
            ],
            options={
                'ordering': ['-id'],
            },
        ),
    ]
