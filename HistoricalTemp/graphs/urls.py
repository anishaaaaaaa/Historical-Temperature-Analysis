from django.conf.urls import url
from django.urls import path
from django.views.generic import TemplateView

from . import views


urlpatterns = [
    path('histtemp', views.history),
    url(r'^plot/$', TemplateView.as_view(template_name='plot.html'), name="plot"),
]
