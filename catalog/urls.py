from django.urls import path
from catalog.apps import NewappConfig
from catalog.views import home
from . import views


app_name = NewappConfig.name
urlpatterns = [
    path(' /home/', home, name='home'),
    path('contacts/', views.contacts, name='contacts'),
]
