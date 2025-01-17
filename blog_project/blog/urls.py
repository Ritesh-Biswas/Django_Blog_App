from django.urls import path # type: ignore
from . import views

urlpatterns = [
    path('',views.home, name='home'),
    path('post/<int:id>', views.post_detail, name='post_detail'),
    path('create/',views.create_post, name='create_post'),
    path('delete/<int:id>',views.delete_post, name='delete_post')
]
