from django.contrib import admin
from django.urls import path, include
from users import views as user_views

from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include("django.contrib.auth.urls")),
    path('register/', user_views.register, name="register"),
    path('active/<uidb64>/<token>/', user_views.activate, name="activate"),
    path('profile/', user_views.profile, name="profile"),
    path("update_password", user_views.change_password, name="change_password"),
    path('', include('blog.urls', namespace='blog')),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL,
                          document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)