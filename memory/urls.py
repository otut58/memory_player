from django.urls import path

from memory import views

urlpatterns = [
    path('', views.top, name='top'),
    #path('top_info', views.top_info, name='top_info'),
    path("memories/new/", views.memory_new, name="memory_new"),
    path("memories/<int:memory_id>/", views.memory_detail, name="memory_detail"),
    path("memories/comment/<int:memory_id>/", views.create_comment, name="comment_create"),
]