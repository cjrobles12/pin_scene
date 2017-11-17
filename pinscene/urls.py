"""Define URL pattern for pinscene app"""

from django.conf.urls import url

from . import views

urlpatterns = [

    #Home page for Pinscene app
    url(r'^$', views.index, name='index'),
    #Show all pins
    url(r'^pins/$', views.pins, name='pins'),
    #Detail page for single pinball machine
    url(r'^pins/(?P<pin_id>\d+)/$', views.pin, name='pin'),
    #page for adding a new pin
    url(r'^new_pin/$', views.new_pin, name='new_pin'),
    #page for editing existing pins
    url(r'^edit_pin/(?P<pin_id>\d+)/$', views.edit_pin, name="edit_pin"),
    #delete a pin
     url(r'^delete/(?P<pk>[0-9]+)/$', views.delete_pin, name='delete_pin')
]