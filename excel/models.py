from django.db import models

class Xlsx(models.Model):
    file_name=models.FileField(upload_to='xlsx')
    activated = models.BooleanField(default=False)

    def __str__(self):
        return f'file id: {self.id}'


class XlsxData(models.Model):
    First_name = models.CharField(max_length=20)
    Last_name = models.CharField(max_length=20)
    Mobile = models.BigIntegerField()
    Start_date = models.DateField()
    Salary = models.CharField(max_length=10)
    Employee_ID = models.CharField(max_length=6)

