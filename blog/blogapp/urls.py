from django.urls import path
from blogapp import views

app_name = 'blogapp'

urlpatterns = [
    path('', views.main_view, name='main'),
    path('createPost/', views.create_post, name='create'),
    path('post/<int:id>/', views.post, name='post')
]
