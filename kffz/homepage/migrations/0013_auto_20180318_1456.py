# Generated by Django 2.0.2 on 2018-03-18 06:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('homepage', '0012_auto_20180318_1455'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='category',
            field=models.CharField(choices=[('科技&DIY', '科技&DIY'), ('财经', '财经'), ('技术', '技术'), ('阅读', '阅读'), ('娱乐', '娱乐')], default='科技&DIY', max_length=10, null=True),
        ),
    ]
