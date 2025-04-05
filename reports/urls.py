from django.urls import path
from . import views 

app_name = "reports"

urlpatterns = [
  path('create-report/', views.create_report, name='create_report'),
  path('reports-list/', views.report_list, name='report_list'),
]