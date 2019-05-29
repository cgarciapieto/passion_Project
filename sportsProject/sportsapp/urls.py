from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('createPost/', views.createPost, name='createPost'),
    path('viewPost/', views.viewPost, name='viewPost'),
    path('postList/', views.postList, name='postList'),
    path('editPost/<int:post_id>/', views.editPost, name='editPost'),
    path('createUser/', views.createUser, name='createUser'),
    path('postDetails/', views.postDetails, name='postDetails'),
    path('deletePost/<int:post_id>/', views.deletePost, name='deletePost'),
    # path('media/<path:path>/', serve, {'document_root': settings.MEDIA_ROOT}),

]