# Generated by Django 3.2.15 on 2023-08-30 02:14

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='RIVUE',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ProModel', models.CharField(max_length=50)),
                ('ProName', models.CharField(max_length=200)),
                ('ProRev', models.CharField(max_length=1000)),
                ('ProEmail', models.EmailField(max_length=254)),
                ('ProCom', models.CharField(max_length=150)),
            ],
            options={
                'db_table': 'RIVUE',
            },
        ),
    ]
