from django.contrib import admin
from home.models import Detail, Section


class DetailsAdmin(admin.ModelAdmin):
    pass


class SectionAdmin(admin.ModelAdmin):
    pass


admin.site.register(Detail, DetailsAdmin)
admin.site.register(Section, SectionAdmin)
