# -*- coding: utf-8 -*-
from projects.models import TaskSet, Task, TaskSetRun, TaskRun, User, Projects

__author__ = 'xiechuan'

import django_filters
from django.db.models import Q




class TaskSetFilter(django_filters.rest_framework.FilterSet):
    """
    任务集的过滤类
    """
    class Meta:
        model = TaskSet
        fields = ['taskset_name',]

class TaskFilter(django_filters.rest_framework.FilterSet):
    """
    任务的过滤类
    """

    class Meta:
        model = Task
        fields = ['task_name', ]

class TaskSetRunFilter(django_filters.rest_framework.FilterSet):
    """
    运行任务集的过滤类
    """
    class Meta:
        model = TaskSetRun
        fields = ['tasksetrun_name','tasksetrun_status']

class TaskRunFilter(django_filters.rest_framework.FilterSet):
    """
    运行任务的过滤类
    """

    class Meta:
        model = TaskRun
        fields = ['taskrun_name', 'taskrun_status']

class UserFilter(django_filters.rest_framework.FilterSet):
    """
    用户的过滤类
    """

    class Meta:
        model = User
        fields = ['username',]

class ProjectsFilter(django_filters.rest_framework.FilterSet):
    """
    项目的过滤类
    """

    class Meta:
        model = Projects
        fields = ['user','project_name']