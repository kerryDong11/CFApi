from django.conf.urls import include,url
from django.urls import path,re_path
from rest_framework import routers
from cf_api import views
 
# 定义路由地址
route = routers.DefaultRouter()
 
# 注册新的路由地址
#route.register(r'student' , views.StudentViewSet)
 
# 注册上一级的路由地址并添加
urlpatterns = [
    #url('api/', include(route.urls)),
    path('users/', views.UsersAPIView.as_view()),
    re_path(r'users/(?P<pk>\d+)/', views.UserAPIView.as_view(),name='user-detail'),    
]