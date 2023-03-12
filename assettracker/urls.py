from django.urls import path
from .views import (
    CompanyListCreateView,
    CompanyRetrieveUpdateDestroyView,
    EmployeeListCreateView,
    EmployeeRetrieveUpdateDestroyView,
    DeviceListCreateView,
    DeviceRetrieveUpdateDestroyView,
    DeviceLogListCreateView,
    DeviceLogRetrieveUpdateDestroyView,
)

urlpatterns = [
    path('companies/', CompanyListCreateView.as_view(), name='company-list-create'),
    path('companies/<int:pk>/', CompanyRetrieveUpdateDestroyView.as_view(), name='company-detail'),
    path('employees/', EmployeeListCreateView.as_view(), name='employee-list-create'),
    path('employees/<int:pk>/', EmployeeRetrieveUpdateDestroyView.as_view(), name='employee-detail'),
    path('devices/', DeviceListCreateView.as_view(), name='device-list-create'),
    path('devices/<int:pk>/', DeviceRetrieveUpdateDestroyView.as_view(), name='device-detail'),
    path('logs/', DeviceLogListCreateView.as_view(), name='devicelog-list-create'),
    path('logs/<int:pk>/', DeviceLogRetrieveUpdateDestroyView.as_view(), name='devicelog-detail'),
]