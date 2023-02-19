from django.urls import path
from blogapp import views

app_name = 'blogapp'

urlpatterns = [
    path('', views.main_view, name='main'),
    path('contact/', views.contact_view, name='contact'),
    path('post/<int:id>/', views.post, name='post'),
    path('create/', views.create_post, name='create'),
    path('taglist/', views.TagListView.as_view(), name='tag_list'),
    path('detailtag/<int:pk>/', views.TagDetailView.as_view(), name='detail_tag'),
    path('tagcreate/', views.TagCreateView.as_view(), name='tag_create'),
    path('tagupdate/<int:pk>/', views.UpdateTagView.as_view(), name='tag_update'),
    path('tagdelete/<int:pk>/', views.DeleteTagView.as_view(), name='tag_delete'),
    path('detailcategory/<int:pk>/', views.CategoryDetailView.as_view(), name='detail_category'),
    path('categorypostcreate/<int:pk>', views.PostCategoryCreateView.as_view(), name='post_category_create'),
]
