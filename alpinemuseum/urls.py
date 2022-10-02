from django.contrib import admin
from django.urls import path

from  alpinemuseum import views


from  alpinemuseum.views import UserDetail,Saved

urlpatterns = [
    path('rohit/', UserDetail.as_view(), name='add'),
    path('saved/', Saved, name='saved')
]