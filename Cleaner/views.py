from django.shortcuts import render_to_response, render

from django.http import HttpResponseBadRequest, HttpResponse
from django import forms
from django.template import RequestContext
import django_excel as excel
import tablib
from Cleaner.models import  *
import re
import xlrd


# Create your views here.


class FileUploadedForm(forms.Form):
    uploaded_file = forms.FileField(required=False)




def import_data(request):

    if request.method == 'POST':
        form = FileUploadedForm(request.POST, request.FILES)
        if form.is_valid():
            input_file = request.FILES.get('uploaded_file')
            wb = xlrd.open_workbook(file_contents=input_file.read())
            wb_sheet = wb.sheet_by_index(0)
            for rownum in range(1, wb_sheet.nrows):
                row = wb_sheet.row_values(rownum)
                #your work with workbook goes here
                name = (wb_sheet.cell(rownum, 0).value)
                engine_type = (wb_sheet.cell(rownum, 1).value)

                s = Ship.objects.get_or_create(name=name, engine_type=engine_type)

                plate = (wb_sheet.cell(rownum, 2).value)
                try:
                    plate = int(plate)
                    plate = 'P' + str(plate)
                except:
                    plate = plate


                edition = (wb_sheet.cell(rownum, 3).value)

                p = Plate.objects.get_or_create(ship = s[0], name = plate, edition= edition)

                item_name = (wb_sheet.cell(rownum, 4).value)
                order_number = (wb_sheet.cell(rownum, 5).value)
                status = (wb_sheet.cell(rownum, 6).value)

                Item.objects.get_or_create(plate=p[0],name=item_name,order_number= order_number,status=status )

            ships = Ship.objects.all()
            for ship in ships:
                plates_number = ship.plate_set.all().count()
                Ship.objects.filter(id = ship.id).update(issue=plates_number-1)

            return HttpResponse("OK", status=200)
        else:
            return HttpResponseBadRequest()

    else:
        form = FileUploadedForm()
    return render(
        request,
        'upload_form.html',
        {
            'form': form,
            'title': 'Import excel data into database example',
            'header': 'Please upload sample-data.xls:'
        })



def export_data(request):
    headers = ('Ship','Engine Type','Plate','Edition', 'Item', 'Order Number','Status')
    data = []
    data = tablib.Dataset(*data, headers=headers)
    ships = Ship.objects.all()
    for ship in ships:
        plates = ship.plate_set.all()
        for plate in plates:
            items = plate.item_set.all()
            for item in items:
                data.append((ship.name, ship.engine_type, plate.name,plate.edition,
                             item.name, item.order_number, item.status))
                response = HttpResponse(data.xls, content_type='application/vnd.ms-excel;charset=utf-8')
                response['Content-Disposition'] = "attachment; filename=export.xls"
    return response
























