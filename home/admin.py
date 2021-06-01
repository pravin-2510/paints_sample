from django.contrib import admin
from .models import Contact

# Register your models here.
class ContactAdmin(admin.ModelAdmin):
    list_display = ('name','email','phone','contact_date','contact_time')
    list_filter = ('contact_date',)
    search_fields = ['name']

admin.site.register(Contact, ContactAdmin)
admin.site.site_header = 'Om Gurudev Paints'
admin.site.title = 'Om Gurudev Paints'