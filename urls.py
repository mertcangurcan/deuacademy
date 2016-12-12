from django.conf.urls import url

from . import views

urlpatterns = [
    # url(r'^sold/$', views.advert_sold, ),
    url(r'^courses/$', views.Courses_view.as_view(), ),
    url(r'^course/(?P<pk>[0-9]+)/$', views.course ,name='course' ), 
    url(r'^form/', views.form,name='form'),
    url(r'^course/(?P<pk>[0-9]+)/delete/$', views.delete_course, name='delete_course'),
    url(r'^course/(?P<pk>[0-9]+)/edit/$', views.edit_course, name='edit_course'),

]