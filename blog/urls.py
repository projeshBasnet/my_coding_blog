from django.urls import path
from .views import Home, UserLogin,UserLogout,CreatePost,PostDetail

urlpatterns = [
    path('',Home,name='home'),
    path('login',UserLogin,name='userlogin'),
    path('logout',UserLogout,name='userlogout'),
    path('createpost',CreatePost,name='createpost'),
    path('postdetail/<pk>',PostDetail,name='postdetail'),
]