from django.urls import path
from fileapp import views

urlpatterns=[
    path('register/',views.register,name='register'),
    path('login/',views.login_user,name='login'),
    path('logout/', views.logout_user, name='logout'),
    path('',views.home_view),
    path('upload/',views.file_upload,name='upload'),
    path('filelist/',views.file_list,name='filelist'),
]