# Generated by Django 4.1.7 on 2023-07-05 16:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Printer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
                ('api_key', models.CharField(max_length=100, unique=True)),
                ('check_type', models.CharField(choices=[('kitchen', 'Kitchen'), ('client', 'Client')], max_length=100)),
                ('point_id', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Check',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(choices=[('kitchen', 'Kitchen'), ('client', 'Client')], max_length=100)),
                ('order', models.JSONField()),
                ('status', models.CharField(choices=[('new', 'New'), ('rendered', 'Rendered'), ('printed', 'Printed')], default='new', max_length=150)),
                ('pdf_file', models.FileField(blank=True, null=True, upload_to='media/pdf')),
                ('print_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='printer.printer')),
            ],
        ),
    ]
