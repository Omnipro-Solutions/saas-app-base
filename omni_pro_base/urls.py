from django.urls import include, path
from omni_pro_base.views import GroupViewSet, UserViewSet, TestCelery
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r"users", UserViewSet)
router.register(r"groups", GroupViewSet)

urlpatterns = [
    path("", include(router.urls)),
    path("api-auth/", include("rest_framework.urls", namespace="rest_framework")),
    path("test/task/celerity", TestCelery.as_view({"post": "test_celerity_task"}), name="test_celerity_task"),
]
