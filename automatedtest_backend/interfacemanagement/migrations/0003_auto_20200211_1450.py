# Generated by Django 2.2.5 on 2020-02-11 06:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('interfacemanagement', '0002_auto_20200211_1242'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='interfaceflowmodel',
            options={'ordering': ['step'], 'verbose_name': '接口流程关系', 'verbose_name_plural': '接口流程关系'},
        ),
    ]