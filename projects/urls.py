from django.conf.urls import url, include
from rest_framework.routers import DefaultRouter
from projects import views

# Create a router and register our viewsets with it.
router = DefaultRouter()

router.register(r'users', views.UserViewSet)
router.register(r'projects', views.ProjectsViewSet)
router.register(r'tasksets', views.TaskSetViewSet)
router.register(r'tasks', views.TaskViewSet)
router.register(r'taskinstances', views.TaskInstanceViewSet)
router.register(r'tasksetruns', views.TaskSetRunViewSet)
router.register(r'taskruns', views.TaskRunViewSet)
router.register(r'menus', views.MenusViewSet)
router.register(r'taskstatus', views.TaskStatusViewSet)



# The API URLs are now determined automatically by the router.
urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^initdb/$',views.initDB_view),
]