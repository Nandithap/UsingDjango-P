from . import views
from django.urls import path

urlpatterns = [
    path('',views.mypage1, name='mypage'),
    #path('about/',views.th,name='about'),
    #path('srv/',views.twoclm,name='service'),
    #path('srvv/',views.srve,name='srvextra'),
]