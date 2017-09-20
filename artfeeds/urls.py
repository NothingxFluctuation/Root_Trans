from django.conf.urls import url
from . import views
urlpatterns=[
	url(r'^$',views.index,name='index'),
        url(r'^urlshort/$',views.urlshort, name='urlshort'),
        url(r'^newsletter/$',views.newsletter, name='newsletter'),
        url(r'^privacy/$',views.privacy, name='privacy'),
        url(r'^terms/$',views.terms,name='terms'),
        url(r'^contact/$',views.contact,name='contact'),
        url(r'^shorty/$',views.shorty,name='shorty'),
        url(r'^newsl/$',views.newsl, name='newsl'),
    
]
