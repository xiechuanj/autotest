from django.conf.urls import url, include
from rest_framework_jwt.views import obtain_jwt_token

from projects.views import ActivateUser, CreateUserView


urlpatterns = [
    url(r'^', include('projects.urls')),
    url(r'^api-auth/', obtain_jwt_token),
    url('^api-register/$', CreateUserView.as_view()),
    url(
        '^api-activate/(?P<token>.+?)/$',
        ActivateUser.as_view(),
        name='activate-user'
    ),
]