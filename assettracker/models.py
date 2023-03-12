from django.db import models

# Create your models here.

class Company(models.Model):
    name = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    phone = models.CharField(max_length=20)

    def __str__(self):
        return self.name

class Employee(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    company = models.ForeignKey(Company, on_delete=models.CASCADE, related_name='employees')

    def __str__(self):
        return self.name

class Device(models.Model):
    name = models.CharField(max_length=255)
    serial_number = models.CharField(max_length=255)
    type = models.CharField(max_length=255)
    status = models.CharField(max_length=255)
    employee = models.ForeignKey(Employee, on_delete=models.SET_NULL, related_name='devices', null=True, blank=True)

    def __str__(self):
        return self.name

class DeviceLog(models.Model):
    device = models.ForeignKey(Device, on_delete=models.CASCADE, related_name='logs')
    checked_out_by = models.ForeignKey(Employee, on_delete=models.SET_NULL, null=True, blank=True, related_name='checked_out_logs')
    checked_in_by = models.ForeignKey(Employee, on_delete=models.SET_NULL, null=True, blank=True, related_name='checked_in_logs')
    checkout_date = models.DateTimeField(auto_now_add=True)
    checkin_date = models.DateTimeField(null=True, blank=True)
    condition_when_checked_out = models.CharField(max_length=255, null=True, blank=True)
    condition_when_checked_in = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self):
        return f"{self.device} ({self.checkout_date})"
