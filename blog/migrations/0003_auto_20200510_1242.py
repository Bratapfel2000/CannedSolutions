# Generated by Django 3.0.3 on 2020-05-10 10:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20200510_1146'),
    ]

    operations = [
        migrations.CreateModel(
            name='TestModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('test_thing', models.CharField(max_length=100)),
            ],
        ),
        migrations.DeleteModel(
            name='Comment',
        ),
    ]
