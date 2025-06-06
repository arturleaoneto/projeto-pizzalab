"""
URL configuration for setup project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from pizza_lab.views import (
    MenuListView,
    MenuUpdateView,
    MenuDeleteView,
    MenuCreateView,
    TemplateView,
)
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
)
from user.views import ProfileList

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", TemplateView.as_view(template_name="pizza_lab/home.html"), name="home"),
    path("gestao/", MenuListView.as_view(), name="menu"),
    path("create/", MenuCreateView.as_view(), name="menu_create"),
    path("update/<int:pk>", MenuUpdateView.as_view(), name="menu_update"),
    path("delete/<int:pk>", MenuDeleteView.as_view(), name="menu_delete"),
    path("api/token/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("profile/", ProfileList.as_view()),
]
