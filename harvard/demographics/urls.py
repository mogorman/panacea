from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^add/patient', views.add, name='add'),
    url(r'^edit/patient/(?P<patient_id>[0-9]*)', views.edit_by_patient, name='edit'),
    url(r'^edit/(?P<patient_id>[0-9]*)', views.edit_by_id, name='edit'),
    url(r'^list/status_update/(\d+)/(\d+)', views.status_update, name='status_update'),
    url(r'^list', views.list, name='list'),
    url(r'^review/(?P<patient_id>[0-9]*)', views.review, name='review'),
    url(r'^signup/$', views.signup, name='signup'),
    ]
