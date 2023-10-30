"""
URL configuration for Medicalshop project.

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
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from shop_app import admin_urls, consumer_urls, pharmacy_urls
from shop_app.views import IndexView,SignInView,SignUpView

urlpatterns = [
    path('admin/',admin_urls.urls()),
    path('consumer/',consumer_urls.urls()),
    path('pharmacy/',pharmacy_urls.urls()),
    path('signin',SignInView.as_view()),
    path('signup',SignUpView.as_view()),
    path('',IndexView.as_view()),
]
if settings.DEBUG:
    urlpatterns+=static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)
    urlpatterns+=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)