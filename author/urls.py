from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import AuthorViewSet

router = DefaultRouter()
router.register("", AuthorViewSet, basename="manage")
urlpatterns = [
    path("", include(router.urls)),
]
app_name = "author"
