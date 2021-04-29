"""rest_api URL Configuration

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
import os
from django.contrib import admin
from django.urls import include, path, re_path
from rest_framework import routers, permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
#router = routers.DefaultRouter()
#router.register(r'users', views.UserViewSet)
#router.register(r'groups', views.GroupViewSet)
version = os.environ.get("BACKEND_VERSION", "")
url_prefix = "api/" + version

# Swagger settings
schema_view = get_schema_view(
   openapi.Info(
      title="Yogiyo Backend Rest API",
      default_version=version,
      description="Yogiyo Rest APIs for frontend application.",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="seunghyuk.jeon@deliveryhero.co.kr"),
      license=openapi.License(name="Delivery Hero Korea's proprietary digital asset. All rights reserved."),
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    # Django admin
    path('admin/', admin.site.urls),

    # APIs
    path(url_prefix + '/auth/', include('rest_auth.urls')),
    path(url_prefix + '/auth/registration/', include('rest_auth.registration.urls')),
    path(url_prefix + '/account/', include('allauth.urls')),
    path(url_prefix + '/forum/', include('forum.urls')),

    # Swagger
    re_path(r'^swagger(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    re_path(r'^redoc/$', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]
