from django.contrib import admin
from django.urls import path, include

urlpatterns = [
  path('admin/', admin.site.urls),
  path('', include('user_account.urls', namespace='user_account')),
  path('reports/', include('reports.urls', namespace='reports')),
]
