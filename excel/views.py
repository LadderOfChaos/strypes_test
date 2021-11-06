from django.shortcuts import render
from .forms import CsvModelForm
from .models import Xlsx, XlsxData
import csv


def upload_file_view(request):
    form = CsvModelForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        form.save()
        form = CsvModelForm()
        obj = Xlsx.objects.get(activated=False)
        with open(obj.file_name.path, 'r') as f:
            reader = csv.reader(f)
            for i, row in enumerate(reader):
                if i == 0:
                    pass
                else:
                    row = ''.join(row)
                    row = row.replace(";", " ")
                    row = row.split()
                    XlsxData.objects.create(
                        First_name=row[0],
                        Last_name=row[1],
                        Mobile=row[2],
                        Start_date=row[3],
                        Salary=row[5],
                        Employee_ID=row[6],
                    )
            obj.activated = True
            obj.save()
    return render(request, 'excel/upload.html', {'form': form})
