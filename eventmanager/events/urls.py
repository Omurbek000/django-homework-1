
from django.urls import path
from. import views


urlpatterns = [
    path(''views.event_list, name='event_list'),
    path('add'views.add_event, name='add_event')
    path('edit/<int:id>'views.edit_event, name='edit_event')
]
