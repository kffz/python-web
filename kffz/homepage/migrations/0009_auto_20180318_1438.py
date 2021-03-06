# Generated by Django 2.0.2 on 2018-03-18 06:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('homepage', '0008_auto_20180318_1424'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='category',
            field=models.ForeignKey(choices=[('科技&DIY', '科技&DIY'), ('财经', '财经'), ('技术', '技术'), ('阅读', '阅读'), ('娱乐', '娱乐')], null=True, on_delete=django.db.models.deletion.CASCADE, to='homepage.BlogCategory'),
        ),
        migrations.AlterField(
            model_name='blogcategory',
            name='catogory',
            field=models.CharField(choices=[('科技&DIY', '科技&DIY'), ('财经', '财经'), ('技术', '技术'), ('阅读', '阅读'), ('娱乐', '娱乐')], default='技术', max_length=10),
        ),
    ]
