from django.contrib import admin

# Register your models here.
from .models import Lodging
#admin.site.register(Lodging)
class LodgingAdmin(admin.ModelAdmin):
	#fields = ["lodge_name", "Lodge_address", "City", "Country", "Pub_date" ]
	list_display = ("lodge_name","city", "country", "pub_date");
	list_filter = ['country']
	search_fields = ['city']
	list_per_page = 50 #pagination

admin.site.register(Lodging, LodgingAdmin)