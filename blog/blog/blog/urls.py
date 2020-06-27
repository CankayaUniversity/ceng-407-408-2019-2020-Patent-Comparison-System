"""blog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from home import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home_view, name='home_view'),
    path('sign-in/', views.sign_in_view, name='sign_in_view'),
    path('sign-up/', views.sign_up_view, name='sign_up_view'),
    path('forgot_password/', views.forgot_password_view, name='forgot_password_view'),
    path('patent_one/', views.patent_one_view, name='patent_one_view'),
    path('patent_second/', views.patent_second_view, name='patent_second_view'),
    path('patent_third/', views.patent_third_view, name='patent_third_view'),
    path('patent_fourth/', views.patent_fourth_view, name='patent_fourth_view'),
    path('patent_fifth/', views.patent_fifth_view, name='patent_fifth_view'),
    path('contact/', views.contact_view, name='contact_view'),
    path('who_we_are/', views.who_we_are_view, name='who_we_are_view'),
    path('our_vision/', views.our_vision_view, name='our_vision_view'),
    path('result/', views.result_view, name='result_view'),
    path('bert_result/', views.bert_result_view, name='bert_result_view'),
    path('logout/', views.logout_account, name='logout'),
]
