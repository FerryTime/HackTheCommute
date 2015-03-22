from django.conf.urls import patterns, include, url

from ferrytime import views

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'hackthecommute.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^index/', views.index, name='index'),
    url(r'^$', views.index, name='index'),
    url(r'^forecast$', views.forecast, name='forecast'),
    url(r'^register$', views.register, name='register'),
    url(r'^login$', 'django.contrib.auth.views.login', name='login'),
)
