from rest_framework import serializers
from .models import Company, Employee, Device, DeviceLog

class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = '__all__'

class EmployeeSerializer(serializers.ModelSerializer):
    company = CompanySerializer(read_only=True)

    class Meta:
        model = Employee
        fields = '__all__'

class DeviceSerializer(serializers.ModelSerializer):
    employee = EmployeeSerializer(read_only=True)

    class Meta:
        model = Device
        fields = '__all__'

class DeviceLogSerializer(serializers.ModelSerializer):
    device = DeviceSerializer(read_only=True)
    checked_out_by = EmployeeSerializer(read_only=True)
    checked_in_by = EmployeeSerializer(read_only=True)

    class Meta:
        model = DeviceLog
        fields = '__all__'