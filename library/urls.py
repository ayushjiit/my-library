from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.lib_first, name='lib_first'),
    
    url(r'^lib/a/$', views.lib_a, name='lib_a'),
    url(r'^lib/b/$', views.lib_b, name='lib_b'),
    url(r'^lib/c/$', views.lib_c, name='lib_c'),
    url(r'^lib/d/$', views.lib_d, name='lib_d'),
    url(r'^lib/e/$', views.lib_e, name='lib_e'),
    url(r'^lib/new/$', views.lib_new, name='lib_new'),
]
