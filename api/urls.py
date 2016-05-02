from django.conf.urls import url, include

from .views import *

urlpatterns = [
    url(r'^$', view=index),
    url(r'^api/toggle/$', view=toggle)
]
