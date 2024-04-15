"""
URL configuration for easy_healthcare project.

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
import os
from django.contrib import admin
from django.urls import path
from django.urls import include, path, re_path
from django.views.static import serve


urlpatterns = [
    path("admin/", admin.site.urls),
    path("healthpass/", include("healthpass.urls", namespace="health")),
    path("accounts/", include("django.contrib.auth.urls")),
]

# Serve the static HTML
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
urlpatterns += [
    re_path(r'^site/(?P<path>.*)$', serve,
        {'document_root': os.path.join(BASE_DIR, 'site'),
         'show_indexes': True},
        name='site_path'
        ),
]

# Add the custom error handler view to the handlers
<<<<<<< HEAD
handler500 = 'healthpass.views5.custom_server_error'
=======
handler500 = "healthpass.views5.custom_error_500"
handler404 = "healthpass.views5.custom_error_404"
handler403 = "healthpass.views5.custom_error_403"
handler400 = "healthpass.views5.custom_error_400"
>>>>>>> d4587570eb2ea87af95454b8da0f2e7052f05c11
