from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^add', views.add, name='add'),
    url(r'^edit/(?P<patient_id>[0-9]*)', views.edit, name='edit'),
    url(r'^list', views.list, name='list'),
    url(r'^review/(?P<patient_id>[0-9]*)', views.review, name='review'),
    url(r'^signup/$', views.signup, name='signup'),
    ]
