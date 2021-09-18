from django.urls import path

from . import views

urlpatterns = [

    path('',views.sign_up_page,name="sign_up_page"),
    path('login_page/',views.login_page,name="login_page"),
    path('display_info/',views.display_info,name="display_info"),

]

