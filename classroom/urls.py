from django.urls import path
from classroom import views

urlpatterns = [
    path('',views.room,name="room"),
    # path('upload/', views.upload_video, name='upload_video'),
    # path('progress/', views.progress, name='progress'),
]
