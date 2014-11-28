from django.conf.urls import patterns, url
# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

admin_sas_urls = patterns('apps.admin_sas.views',
    url(r'^$','principal', name="principal"),
    url(r'^login$', 'login', name="login"),
    url(r'^logout$', 'v_logout', name="v_logout"),
    url(r'^produtos$', 'produtos', name="produtos"),   
    url(r'^myprodutos$', 'myprodutos', name="myprodutos"), 
    url(r'^blog$', 'blog', name="blog"), 
    url(r'^mensajes$', 'mensajes', name="mensajes"), 

)  


