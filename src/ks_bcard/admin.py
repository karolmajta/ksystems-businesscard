from django.contrib import admin

from models import BCardSite, BCardPage

admin.site.register(BCardSite, admin.ModelAdmin)
admin.site.register(BCardPage, admin.ModelAdmin)