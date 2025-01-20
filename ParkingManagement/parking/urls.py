from django.urls import path
from . import views

urlpatterns= [
    path('register/',views.register_slot,name='register_slot'),
    path('unregiter/',views.unregister_slot,name='unregister_slot'),

]

