# Generated by Django 3.0 on 2019-12-24 20:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('BeginToReason', '0007_delete_code_template'),
    ]

    operations = [
        migrations.CreateModel(
            name='Code_Template',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('template_name', models.CharField(max_length=30)),
                ('template_code', models.TextField(max_length=500)),
            ],
        ),
    ]