from django.urls import path
from . import views

urlpatterns = [
    path('check_lsit/', views.CheckList_List_Create.as_view(), name='check_list_view_create')
]
