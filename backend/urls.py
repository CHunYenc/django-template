"""backend URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.urls import path, include
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView, SpectacularRedocView
from django.conf import settings
from django.conf.urls.static import static
from apps.utils import get_client_ip

API_URL = 'api'
URL_V1 = f'{API_URL}/v1'
# URL_V2 = f'{API_URL}/v2'

urlpatterns = [
    path('admin/', admin.site.urls),
    # API Document
    path('schema/v1/', SpectacularAPIView.as_view(), name='schema'),
    path(f'{URL_V1}/redoc/',
         SpectacularRedocView.as_view(url_name='schema'), name='redoc'),
    # APPS
    path(f"{URL_V1}/system/", include('apps.system.urls'))
]


if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL,
                          document_root=settings.STATIC_ROOT)
    import debug_toolbar

    urlpatterns += [
        path('__debug__/', include('debug_toolbar.urls')),
        path("ip/", get_client_ip)  # 若使用 server 開發，可以檢查連到 server 是什麼 ip
    ]

# default: "Django Administration"
# admin.site.site_header = 'Admin'
