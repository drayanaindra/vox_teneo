from django.conf.urls import patterns, include, url
from django.views.generic import TemplateView
from .views import LoginView, RegisterView

urlpatterns = patterns('',
    url(r'^$', TemplateView.as_view(template_name='main_page.html'), name='index')
)