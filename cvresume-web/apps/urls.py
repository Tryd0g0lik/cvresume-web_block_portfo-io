"""cvresume_web URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
# import slug as slug
from django.urls import path, include, re_path
from rest_framework import routers

from apps import views
from cvresume_web import settings

router = routers.SimpleRouter()

urlpatterns = [
    path('', views.indexPage, name='indexPage'),
    re_path(
        r"^\w*-?/",
        views.innerPage,
        name='innerpage'
    )
]

if settings.DEBUG:
    import debug_toolbar
    urlpatterns = [
        path('__debug__/', include(debug_toolbar.urls)),
    ] + urlpatterns
