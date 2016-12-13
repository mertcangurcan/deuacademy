from django.conf.urls import url


from . import views

urlpatterns = [
    # url(r'^course/(?P<pk>[0-9]+)/$', views.course ,name='course' ),
    url(r'^$', views.Users.as_view(), name='users'),


]