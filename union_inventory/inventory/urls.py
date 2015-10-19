"""URLs for 'inventory' app"""

from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', 'inventory.views.index'),
    url(r'^view-inventory/(?P<inventory_id>\d+)/$', 'inventory.views.view_inventory'),
    # used to use (?P<inventory_id>[0-9]+) but then changed 
    url(r'^edit-inventory/(?P<inventory_id>\d+)/$', 'inventory.views.edit_inventory'),
    url(r'^delete-inventory/(?P<inventory_id>\d+)/$', 'inventory.views.delete_inventory'),
    url(r'^edit-computer/(?P<computer_id>\d+)/$', 'inventory.views.edit_computer'),
    url(r'^delete-computer/(?P<computer_id>\d+)/$', 'inventory.views.delete_computer'),
]
