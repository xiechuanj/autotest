# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib.auth import get_user_model
from django.db import models

from django.db import models


User = get_user_model()
# Create your models here.


class Projects(models.Model):
    """
    项目表
    """
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="projects")
    project_name = models.CharField(default="", max_length=30, verbose_name="项目名称", help_text="项目名称")

    class Meta:
        verbose_name = "项目表"
        verbose_name_plural = verbose_name
        unique_together = ("user", "project_name")

    def __str__(self):
        return self.project_name

class Task(models.Model):
    """
    任务
    """
    projects = models.ForeignKey(Projects, verbose_name=u"项目", related_name="tasks", on_delete=models.CASCADE, )
    task_name = models.CharField(default="", max_length=30, verbose_name="任务名称", help_text="任务名称")

    class Meta:
        verbose_name = "任务"
        verbose_name_plural = verbose_name
        unique_together = ("projects", "task_name")

    def __str__(self):
        return self.task_name

class TaskSet(models.Model):
    """
    任务集
    """
    projects = models.ForeignKey(Projects, verbose_name=u"项目", related_name="tasksets", on_delete=models.CASCADE,)
    taskset_name = models.CharField(default="", max_length=30, verbose_name="任务集名称", help_text="任务集名称")


    class Meta:
        verbose_name = "任务集"
        verbose_name_plural = verbose_name
        unique_together = ("projects", "taskset_name")

    def __str__(self):
        return self.taskset_name


class TaskInstance(models.Model):
    """
    任务实例
    """
    taskset = models.ForeignKey(TaskSet, verbose_name=u"任务集实例", related_name="taskinstances" )
    task = models.ForeignKey(Task, verbose_name=u"任务实例", related_name="taskinstances")
    taskinstance_name = models.CharField(max_length=30, verbose_name="任务实例名称", help_text="任务实例名称")


    class Meta:
        verbose_name = "任务实例"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.taskinstance_name


class TaskStatus(models.Model):
    """
    任务状态表
    """
    taskstatus_id = models.IntegerField(verbose_name=u"状态id")
    taskstatus_name = models.CharField(default="", max_length=30, verbose_name="状态名称", help_text="状态名称")

    class Meta:
        verbose_name = "任务状态"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.taskstatus_name

class TaskSetRun(models.Model):
    """
    运行任务集
    """
    taskset = models.ForeignKey(TaskSet, verbose_name=u"运行任务集实例", related_name="tasksetruns")
    tasksetrun_name = models.CharField(default="", max_length=30, verbose_name="运行任务集名称", help_text="运行任务集名称")
    tasksetrun_status = models.ForeignKey(TaskStatus, verbose_name="运行任务集状态", help_text="运行任务集状态")
    tasksetrun_starttime = models.DateTimeField(auto_now_add=True)
    tasksetrun_endtime = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "运行任务集"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.tasksetrun_name


class TaskRun(models.Model):
    """
    运行任务
    """
    taskrunset = models.ForeignKey(TaskSetRun, verbose_name=u"运行任务", related_name="taskruns")
    taskrun_name = models.CharField(default="", max_length=30, verbose_name="运行任务名称", help_text="运行任务名称")
    taskrun_status = models.ForeignKey(TaskStatus, verbose_name="运行任务状态", help_text="运行任务状态")
    taskrun_starttime = models.DateTimeField(auto_now_add=True, verbose_name="运行开始时间")
    taskrun_endtime = models.DateTimeField(auto_now=True, verbose_name="运行结束时间")

    class Meta:
        verbose_name = "运行任务"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.taskrun_name


class Menus(models.Model):
    """
    菜单
    """
    MENU_TYPE = (
        (1, "一级菜单"),
        (2, "二级菜单"),
        (3, "三级菜单"),
    )

    name = models.CharField(default="", max_length=30, verbose_name="菜单名", help_text="菜单名")
    code = models.CharField(default="", max_length=30, verbose_name="菜单code", help_text="菜单code")
    desc = models.TextField(default="", verbose_name="菜单描述", help_text="菜单描述")
    category_type = models.IntegerField(choices=MENU_TYPE, verbose_name="菜单级别", help_text="菜单级别")
    parent_category = models.ForeignKey("self", null=True, blank=True, verbose_name="父菜单级别", help_text="父目录",
                                        related_name="sub_menu")
    is_tab = models.BooleanField(default=False, verbose_name="是否导航", help_text="是否导航")
    add_time = models.DateTimeField(auto_now=True, verbose_name="添加时间")

    class Meta:
        verbose_name = "菜单"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name