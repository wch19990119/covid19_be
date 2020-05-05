# Generated by Django 3.0.4 on 2020-05-05 06:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0004_auto_20200502_1716'),
    ]

    operations = [
        migrations.CreateModel(
            name='Region',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64)),
                ('adcode', models.IntegerField()),
            ],
            options={
                'verbose_name': '地区',
                'verbose_name_plural': '地区',
                'ordering': ['adcode'],
            },
        ),
        migrations.AddField(
            model_name='user',
            name='regions',
            field=models.ManyToManyField(to='login.Region'),
        ),
    ]
