from django.conf.urls import patterns, include, url
from apps.admin_sas.urls import admin_sas_urls

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
    url(r'^adm/', include(admin_sas_urls))
)
