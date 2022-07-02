
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),

    path('api/token/', include('djoser.urls.jwt')),
    path('', include('registration.urls'))
]
