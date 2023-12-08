from django.urls import path
from profileapp import views

urlpatterns = [
    path('search/', views.user_search, name='user_search'),  
    path('<str:username>/', views.userprofileview, name='user_profile'),
]