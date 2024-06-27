from django.urls import path
from .views import tweet_list, tweet_create, tweet_edit, tweet_delete,register


urlpatterns = [
   path('create/', tweet_create,name='tweet_create'),
   path('', tweet_list,name='tweet_list'),
   path('edit/<int:tweet_id>/', tweet_edit,name='tweet_edit'),
   path('delete/<int:tweet_id>/', tweet_delete,name='tweet_delete'),   
   path('register/', register,name='register')    
]