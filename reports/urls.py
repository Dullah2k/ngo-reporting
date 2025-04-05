from django.urls import path
from . import views 

app_name = "reports"

urlpatterns = [
  path('create-report/', views.create_report, name='create_report'),
  path('reports-list/', views.report_list, name='report_list'),
  path('reports/<int:pk>/', views.report_detail, name='report_details'),
  path('reports/<int:pk>/review/', views.review_report, name='review_report'),
]