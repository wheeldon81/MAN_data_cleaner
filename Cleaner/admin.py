from argparse import Action
from django.contrib import admin

# Register your models here.
from django.contrib.admin import TabularInline, StackedInline, site

from Cleaner.models import *

#admin.site.register(Ship)
from django.contrib import admin
import nested_admin




class ItemInline(nested_admin.NestedStackedInline):
    model = Item
    extra = 0



class PlateInline(nested_admin.NestedStackedInline):
    model = Plate
    inlines = [ItemInline]
    extra = 0

class ShipAdmin(nested_admin.NestedModelAdmin):
    inlines = [PlateInline]
    extra = 0
    list_display = ('name', 'engine_type','issue')

admin.site.register(Ship, ShipAdmin)




