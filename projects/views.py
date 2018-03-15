# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import jwt
from django.http import HttpResponse

# Create your views here.
from django.views.decorators.csrf import csrf_exempt
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets, filters, permissions, status, exceptions
from rest_framework.generics import CreateAPIView
from rest_framework.pagination import PageNumberPagination
from rest_framework.reverse import reverse
from rest_framework.views import APIView
from rest_framework_jwt.settings import api_settings
from projects.filters import TaskSetFilter, TaskFilter, TaskSetRunFilter, TaskRunFilter, UserFilter, ProjectsFilter
from projects.models import User, Projects, TaskSet, Task, TaskInstance, TaskRun, TaskSetRun, Menus, TaskStatus
from projects.serializers import UserSerializer, ProjectsSerializer, TaskSetSerializer, TaskSerializer, \
    TaskInstanceSerializer, TaskRunSerializer, TaskSetRunSerializer, MenusSerializer, TaskStatusSerializer
from rest_framework.response import Response
from django.utils.translation import ugettext as _

jwt_payload_handler = api_settings.JWT_PAYLOAD_HANDLER
jwt_encode_handler = api_settings.JWT_ENCODE_HANDLER
jwt_decode_handler = api_settings.JWT_DECODE_HANDLER

class TaskStatusViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically provides `list`, `create`, `retrieve`,
    `update` and `destroy` actions.

    Additionally we also provide an extra `highlight` action.
    """
    queryset = TaskStatus.objects.all()
    serializer_class = TaskStatusSerializer

class CustPagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = 'page_size'
    page_query_param = "page"
    max_page_size = 100

# class UserViewSet(viewsets.ReadOnlyModelViewSet):
#     """
#     This viewset automatically provides `list` and `detail` actions.
#     """
#     queryset = User.objects.all()
#     serializer_class = UserSerializer
#     permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    pagination_class = CustPagination
    filter_backends = (DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter)
    filter_class = UserFilter
    search_fields = ('username',)
    ordering_fields = ('username',)


class CreateUserView(CreateAPIView):

    model = User.objects.all()
    permission_classes = [
        permissions.AllowAny # Or anon users can't register
    ]
    serializer_class = UserSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        user = self.model.get(username=serializer.data['username'])
        payload = jwt_payload_handler(user)
        token = jwt_encode_handler(payload)
        return Response(
            {
                'confirmation_url': reverse(
                    'activate-user', args=[token], request=request
                )
            },
            status=status.HTTP_201_CREATED, headers=headers
        )


class ActivateUser(APIView):

    def get(self, request, *args, **kwargs):
        token = kwargs.pop('token')
        try:
            payload = jwt_decode_handler(token)
        except jwt.ExpiredSignature:
            msg = _('Signature has expired.')
            raise exceptions.AuthenticationFailed(msg)
        except jwt.DecodeError:
            msg = _('Error decoding signature.')
            raise exceptions.AuthenticationFailed(msg)
        except jwt.InvalidTokenError:
            raise exceptions.AuthenticationFailed()

        user_to_activate = User.objects.get(id=payload.get('user_id'))
        user_to_activate.is_active = True
        user_to_activate.save()

        return Response(
            {'User Activated'},
            status=status.HTTP_200_OK
        )



class ProjectsViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically provides `list`, `create`, `retrieve`,
    `update` and `destroy` actions.

    Additionally we also provide an extra `highlight` action.
    """
    queryset = Projects.objects.all()
    serializer_class = ProjectsSerializer
    pagination_class = CustPagination
    filter_backends = (DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter)
    filter_class = ProjectsFilter
    search_fields = ('project_name',)
    ordering_fields = ('project_name',)

class TaskSetViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically provides `list`, `create`, `retrieve`,
    `update` and `destroy` actions.

    Additionally we also provide an extra `highlight` action.
    """
    queryset = TaskSet.objects.all()
    serializer_class = TaskSetSerializer
    pagination_class = CustPagination
    filter_backends = (DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter)
    filter_class = TaskSetFilter
    search_fields = ('taskset_name',)
    ordering_fields = ('taskset_name',)

class TaskViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically provides `list`, `create`, `retrieve`,
    `update` and `destroy` actions.

    Additionally we also provide an extra `highlight` action.
    """
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    pagination_class = CustPagination
    filter_backends = (DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter)
    filter_class = TaskFilter
    search_fields = ('task_name',)
    ordering_fields = ('task_name',)

class TaskInstanceViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically provides `list`, `create`, `retrieve`,
    `update` and `destroy` actions.

    Additionally we also provide an extra `highlight` action.
    """
    queryset = TaskInstance.objects.all()
    serializer_class = TaskInstanceSerializer

class TaskSetRunViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically provides `list`, `create`, `retrieve`,
    `update` and `destroy` actions.

    Additionally we also provide an extra `highlight` action.
    """
    queryset = TaskSetRun.objects.all()
    serializer_class = TaskSetRunSerializer
    pagination_class = CustPagination
    filter_backends = (DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter)
    filter_class = TaskSetRunFilter
    search_fields = ('tasksetrun_name','tasksetrun_status')
    ordering_fields = ('tasksetrun_name','tasksetrun_status')


class TaskRunViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically provides `list`, `create`, `retrieve`,
    `update` and `destroy` actions.

    Additionally we also provide an extra `highlight` action.
    """
    queryset = TaskRun.objects.all()
    serializer_class = TaskRunSerializer
    pagination_class = CustPagination
    filter_backends = (DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter)
    filter_class = TaskRunFilter
    search_fields = ('taskrun_name', 'taskrun_status')
    ordering_fields = ('taskrun_name', 'taskrun_status')



class MenusViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically provides `list`, `create`, `retrieve`,
    `update` and `destroy` actions.

    Additionally we also provide an extra `highlight` action.
    """
    queryset = Menus.objects.all()
    serializer_class = MenusSerializer




@csrf_exempt
def initDB_view(request):
    Projects.objects.all().delete()
    Task.objects.all().delete()
    TaskSet.objects.all().delete()
    TaskInstance.objects.all().delete()
    TaskSetRun.objects.all().delete()
    TaskRun.objects.all().delete()
    return HttpResponse('删除成功')
