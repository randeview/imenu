from django.urls import include, path

urlpatterns = [
    path('auth/', include('apps.authentication.urls')),
    path('restaurant/', include('apps.restaurant.urls')),
    path('users/', include('apps.users.urls')),
]
