from django.conf.urls import url

# from apps.dashboard.views import index, createUserinfo
from apps.dashboard.views import UsersList, UsersCreate, UsersUpdate, UsersDelete

urlpatterns = [
    url(r'^$', UsersList.as_view(), name='userinfo-index'),
    url(r'^create$', UsersCreate.as_view(), name='userinfo-create'),
    url(r'^update/(?P<pk>\d+)/$', UsersUpdate.as_view(), name='userinfo-update'),
    url(r'^delete/(?P<pk>\d+)/$', UsersDelete.as_view(), name='userinfo-delete'),
]
