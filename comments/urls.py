from django.urls import path
from . import views

app_name = 'comments'

urlpatterns = [
    path('add/<post_id>/', views.add_comment, name='add_comment'),
    path('add-reply/<comment_id>/', views.add_reply, name='add_reply'),
    path('delete/<comment_id>/', views.delete_comment, name='delete_comment'),
    path('delete-reply/<reply_id>/', views.delete_reply, name='delete_reply'),
]
