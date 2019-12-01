from django.urls import path, re_path

from . import views

app_name = 'demo'

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    re_path(r'^(?P<q_date>\d{4}-\d{2}-\d{2})$', views.DateView.as_view(), name='date'),
    re_path(r'^(?P<q_date>\d{4}-\d{2}-\d{2})/(?P<q_publisher>\d+)$', views.PublisherView.as_view(), name='publisher'),
]