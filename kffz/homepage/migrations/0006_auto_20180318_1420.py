# Generated by Django 2.0.2 on 2018-03-18 06:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('homepage', '0005_auto_20180318_1415'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogcategory',
            name='catogory',
            field=models.CharField(choices=[('科技&DIY', '科技&DIY'), ('财经', '财经'), ('技术', '技术'), ('阅读', '阅读'), ('娱乐', '娱乐')], max_length=10),
        ),
    ]
