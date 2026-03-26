from django.urls import path
from .views import get_report, create_report

urlpatterns = [
    path('create/', create_report, name='create_report'),
    path('<int:report_id>/', get_report, name='get_report')
]
