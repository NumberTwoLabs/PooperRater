from django.conf.urls import patterns, include, url
from django.contrib import admin
from pooperRater import views

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'NumberTwoLabs.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),

    url(r'^$', views.googleplace, name='map'),
    url(r'^yelp', views.yelp_api, name='yelp_api')
)
