from django.urls import path, include
from rest_framework.routers import DefaultRouter

from apps.users.views import UserCreateApiView, RolesListView, UsersListView

router = DefaultRouter()
router.register(r'users', UserCreateApiView, basename='user')
urlpatterns = router.urls
urlpatterns = [
    path('', include(router.urls)),
    path('roles/', RolesListView.as_view()),
    path('list/', UsersListView.as_view())
]
