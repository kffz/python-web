# Generated by Django 2.0.2 on 2018-03-18 06:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('homepage', '0004_auto_20180316_2034'),
    ]

    operations = [
        migrations.CreateModel(
            name='BlogCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('catogory', models.CharField(choices=[('科技&DIY', '科技&DIY'), ('财经', '财经'), ('技术', '技术'), ('阅读', '阅读'), ('娱乐', '娱乐')], default='技术', max_length=10)),
            ],
        ),
        migrations.RemoveField(
            model_name='blog',
            name='rating',
        ),
        migrations.AddField(
            model_name='blog',
            name='category',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='homepage.BlogCategory'),
        ),
    ]
