from .views import post_create, post_delete, post_detail, post_update, post_list
from django.urls import path, include

urlpatterns = [
    path('create/', post_create, name='postcreate'),
    path('<int:pk>/', post_detail, name='postdetail'),
    path('', post_list, name='postlist'),
    path('<int:pk>/edit/', post_update, name='postupdate'),
    path('<int:pk>/delete/', post_delete, name='postdelete'),
]
