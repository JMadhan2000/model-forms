from django.contrib import admin

# Register your models here.
from app.models import *

class CustomizeWebPage(admin.ModelAdmin):
    list_display=['Name','Url','Email']
    list_display_links=['Url']
    list_editable=['Email']
    list_filter=['Name']
    list_per_page=1
    search_fields=['Email']



admin.site.register(Topic)
admin.site.register(WebPage,CustomizeWebPage)
admin.site.register(AccessRecord)


admin.site.site_header='Madhan.site'
admin.site.site_title='Mohan'
admin.site.index_title='Reddys'