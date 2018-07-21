# Generated by Django 2.0.7 on 2018-07-21 04:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_auto_20180721_0404'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customuser',
            name='age',
        ),
        migrations.AddField(
            model_name='customuser',
            name='birth',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='customuser',
            name='interest',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='customuser',
            name='nickname',
            field=models.CharField(default='nickname', max_length=22),
        ),
        migrations.AddField(
            model_name='customuser',
            name='realname',
            field=models.CharField(default='realname', max_length=22),
        ),
        migrations.AddField(
            model_name='customuser',
            name='userroles',
            field=models.IntegerField(choices=[(0, 'Visitor'), (1, 'Student'), (2, 'Teacher'), (3, 'Parent')], default=0),
        ),
    ]
