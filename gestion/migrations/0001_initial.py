# Generated by Django 5.1.2 on 2024-10-17 10:21

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Borrower',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
                ('blocked', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Media',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
            ],
        ),
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
                ('author', models.CharField(max_length=150)),
                ('loandate', models.DateField()),
                ('available', models.BooleanField(default=True)),
                ('borrower', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gestion.borrower')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gestion.media')),
            ],
        ),
    ]
