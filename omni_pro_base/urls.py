from django.urls import include, path

urlpatterns = [
    path(r"base/", include('health_check.urls')),
]
