from django.contrib import admin

from .models import Company, Keyword



class KeywordInline(admin.TabularInline):
    model = Keyword


class CompanyAdmin(admin.ModelAdmin):
    inlines = [
        KeywordInline,
    ]

admin.site.register(Company, admin_class=CompanyAdmin)

