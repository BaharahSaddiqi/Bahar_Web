from django.urls import path 
from . import views


#'http://example.com/posts/'

#'http://example.com/posts/new'

#'http://example.com/posts/1'

#'http://example.com/posts/delete/6766767'




urlpatterns = [
    path('new', views.new, name='new'),
    path('<int:id>', views.detail, name='details'),
    path('delete/<int:id>', views.delete, name='delete'),
]