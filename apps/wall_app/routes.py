from django.conf.urls import url
from . import views

urlpatterns = [
    # url(r'^wall/(?P<user_id>\d+)$', views.index),
    
    url(r'^wall$', views.index),
    url(r'^wall/post$', views.post_message),
    url(r'^wall/comment$', views.post_comment),
    url(r'^wall/(?P<message_id>\d+)/destroy/message$', views.destroy_message),
    url(r'^wall/(?P<comment_id>\d+)/destroy/comment$', views.destroy_comment),
    
]

