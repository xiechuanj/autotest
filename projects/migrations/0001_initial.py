# -*- coding: utf-8 -*-
# Generated by Django 1.11.10 on 2018-03-09 15:31
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Menus',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', help_text='\u83dc\u5355\u540d', max_length=30, verbose_name='\u83dc\u5355\u540d')),
                ('code', models.CharField(default='', help_text='\u83dc\u5355code', max_length=30, verbose_name='\u83dc\u5355code')),
                ('desc', models.TextField(default='', help_text='\u83dc\u5355\u63cf\u8ff0', verbose_name='\u83dc\u5355\u63cf\u8ff0')),
                ('category_type', models.IntegerField(choices=[(1, '\u4e00\u7ea7\u83dc\u5355'), (2, '\u4e8c\u7ea7\u83dc\u5355'), (3, '\u4e09\u7ea7\u83dc\u5355')], help_text='\u83dc\u5355\u7ea7\u522b', verbose_name='\u83dc\u5355\u7ea7\u522b')),
                ('is_tab', models.BooleanField(default=False, help_text='\u662f\u5426\u5bfc\u822a', verbose_name='\u662f\u5426\u5bfc\u822a')),
                ('add_time', models.DateTimeField(auto_now=True, verbose_name='\u6dfb\u52a0\u65f6\u95f4')),
                ('parent_category', models.ForeignKey(blank=True, help_text='\u7236\u76ee\u5f55', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='sub_menu', to='projects.Menus', verbose_name='\u7236\u83dc\u5355\u7ea7\u522b')),
            ],
            options={
                'verbose_name': '\u83dc\u5355',
                'verbose_name_plural': '\u83dc\u5355',
            },
        ),
        migrations.CreateModel(
            name='Projects',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('project_name', models.CharField(default='', help_text='\u9879\u76ee\u540d\u79f0', max_length=30, verbose_name='\u9879\u76ee\u540d\u79f0')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='projects', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': '\u9879\u76ee\u8868',
                'verbose_name_plural': '\u9879\u76ee\u8868',
            },
        ),
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('task_name', models.CharField(default='', help_text='\u4efb\u52a1\u540d\u79f0', max_length=30, verbose_name='\u4efb\u52a1\u540d\u79f0')),
                ('projects', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='tasks', to='projects.Projects', verbose_name='\u9879\u76ee')),
            ],
            options={
                'verbose_name': '\u4efb\u52a1',
                'verbose_name_plural': '\u4efb\u52a1',
            },
        ),
        migrations.CreateModel(
            name='TaskInstance',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('taskinstance_name', models.CharField(help_text='\u4efb\u52a1\u5b9e\u4f8b\u540d\u79f0', max_length=30, verbose_name='\u4efb\u52a1\u5b9e\u4f8b\u540d\u79f0')),
                ('task', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='taskinstances', to='projects.Task', verbose_name='\u4efb\u52a1\u5b9e\u4f8b')),
            ],
            options={
                'verbose_name': '\u4efb\u52a1\u5b9e\u4f8b',
                'verbose_name_plural': '\u4efb\u52a1\u5b9e\u4f8b',
            },
        ),
        migrations.CreateModel(
            name='TaskRun',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('taskrun_name', models.CharField(default='', help_text='\u8fd0\u884c\u4efb\u52a1\u540d\u79f0', max_length=30, verbose_name='\u8fd0\u884c\u4efb\u52a1\u540d\u79f0')),
                ('taskrun_starttime', models.DateTimeField(auto_now_add=True, verbose_name='\u8fd0\u884c\u5f00\u59cb\u65f6\u95f4')),
                ('taskrun_endtime', models.DateTimeField(auto_now=True, verbose_name='\u8fd0\u884c\u7ed3\u675f\u65f6\u95f4')),
            ],
            options={
                'verbose_name': '\u8fd0\u884c\u4efb\u52a1',
                'verbose_name_plural': '\u8fd0\u884c\u4efb\u52a1',
            },
        ),
        migrations.CreateModel(
            name='TaskSet',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('taskset_name', models.CharField(default='', help_text='\u4efb\u52a1\u96c6\u540d\u79f0', max_length=30, verbose_name='\u4efb\u52a1\u96c6\u540d\u79f0')),
                ('projects', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='tasksets', to='projects.Projects', verbose_name='\u9879\u76ee')),
            ],
            options={
                'verbose_name': '\u4efb\u52a1\u96c6',
                'verbose_name_plural': '\u4efb\u52a1\u96c6',
            },
        ),
        migrations.CreateModel(
            name='TaskSetRun',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tasksetrun_name', models.CharField(default='', help_text='\u8fd0\u884c\u4efb\u52a1\u96c6\u540d\u79f0', max_length=30, verbose_name='\u8fd0\u884c\u4efb\u52a1\u96c6\u540d\u79f0')),
                ('tasksetrun_starttime', models.DateTimeField(auto_now_add=True)),
                ('tasksetrun_endtime', models.DateTimeField(auto_now=True)),
                ('taskset', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='tasksetruns', to='projects.TaskSet', verbose_name='\u8fd0\u884c\u4efb\u52a1\u96c6\u5b9e\u4f8b')),
            ],
            options={
                'verbose_name': '\u8fd0\u884c\u4efb\u52a1\u96c6',
                'verbose_name_plural': '\u8fd0\u884c\u4efb\u52a1\u96c6',
            },
        ),
        migrations.CreateModel(
            name='TaskStatus',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('taskstatus_id', models.IntegerField(verbose_name='\u8fd0\u884c\u4efb\u52a1\u96c6\u5b9e\u4f8b')),
                ('taskstatus_name', models.CharField(default='', help_text='\u8fd0\u884c\u4efb\u52a1\u96c6\u540d\u79f0', max_length=30, verbose_name='\u8fd0\u884c\u4efb\u52a1\u96c6\u540d\u79f0')),
            ],
            options={
                'verbose_name': '\u4efb\u52a1\u72b6\u6001',
                'verbose_name_plural': '\u4efb\u52a1\u72b6\u6001',
            },
        ),
        migrations.AddField(
            model_name='tasksetrun',
            name='tasksetrun_status',
            field=models.ForeignKey(help_text='\u8fd0\u884c\u4efb\u52a1\u96c6\u72b6\u6001', on_delete=django.db.models.deletion.CASCADE, to='projects.TaskStatus', verbose_name='\u8fd0\u884c\u4efb\u52a1\u96c6\u72b6\u6001'),
        ),
        migrations.AddField(
            model_name='taskrun',
            name='taskrun_status',
            field=models.ForeignKey(help_text='\u8fd0\u884c\u4efb\u52a1\u72b6\u6001', on_delete=django.db.models.deletion.CASCADE, to='projects.TaskStatus', verbose_name='\u8fd0\u884c\u4efb\u52a1\u72b6\u6001'),
        ),
        migrations.AddField(
            model_name='taskrun',
            name='taskrunset',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='taskruns', to='projects.TaskSetRun', verbose_name='\u8fd0\u884c\u4efb\u52a1'),
        ),
        migrations.AddField(
            model_name='taskinstance',
            name='taskset',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='taskinstances', to='projects.TaskSet', verbose_name='\u4efb\u52a1\u96c6\u5b9e\u4f8b'),
        ),
        migrations.AlterUniqueTogether(
            name='taskset',
            unique_together=set([('projects', 'taskset_name')]),
        ),
        migrations.AlterUniqueTogether(
            name='task',
            unique_together=set([('projects', 'task_name')]),
        ),
        migrations.AlterUniqueTogether(
            name='projects',
            unique_together=set([('user', 'project_name')]),
        ),
    ]
