#coding:utf-8

from django.conf.urls import patterns, include, url
from mysite import views
from django.conf.urls.defaults import *
from django.contrib.auth.views import login, logout

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$', views.index),
    url(r'^login/$', views.login_view),
    url(r'^homepage/',views.homepage),
    url(r'^logout/$',views.logout_view),
    url(r'^reg/',views.reg),
    url(r'^register/',views.register),
    url(r'^reg_op/',views.reg_op),

    url(r'^upclassinfo/',views.upclassinfo),
    url(r'^upload_file/',views.upload_file),
    url(r'^file_download/',views.file_download),
    url(r'^file_download_op/filename=(?P<filename>.{1,500})/$', views.file_download_op),

	url(r'^setting/',views.setting),
    url(r'^setting_op/',views.setting_op),

    url(r'^upsoftware/',views.upsoftware),
    url(r'^upsoftware_op/',views.upsoftware_op),

    url(r'^software_download/',views.software_download),
    url(r'^software_download_op/',views.software_download_op),

    url(r'^other_download/',views.other_download),
    url(r'^other_download_op/',views.other_download_op),

    url(r'^upother/',views.upother),
    url(r'^upother_op/',views.upother_op),

    url(r'^notice/',views.notice),
    # url(r'^www/', include('www.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
     url(r'^admin/', include(admin.site.urls)),
)
