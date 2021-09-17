from django.urls import path

from . import views

urlpatterns = [
    path('', views.login_page, name='login_page'),
    path('signup/',views.sign_up_page,name="sign_up_page")

]