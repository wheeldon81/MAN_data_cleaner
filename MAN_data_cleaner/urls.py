
from django.conf.urls import include, url
from django.contrib import admin
from Cleaner import views

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),

     url(r'^nested_admin/', include('nested_admin.urls')),
     url(r'^grappelli/', include('grappelli.urls')), # grappelli URLS

    #url(r'^$', views.upload, name='uplink'),
    #url(r'^download/(.*)', views.download, name="download"),
    #url(r'^download_attachment/(.*)/(.*)', views.download_as_attachment,
    #    name="download_attachment"),
    #url(r'^exchange/(.*)', views.exchange, name="exchange"),
    #url(r'^parse/(.*)', views.parse, name="parse"),
    url(r'^import/', views.import_data, name="import"),
    #url(r'^import_sheet/', views.import_sheet, name="import_sheet"),
    url(r'^export/', views.export_data, name="export")
]



