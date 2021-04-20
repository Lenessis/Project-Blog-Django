from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('blog/', include('mainapp.urls', namespace='blog')),
    path('admin/', admin.site.urls),
]