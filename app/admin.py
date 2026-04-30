from django.contrib import admin
from .models import Student


@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ('name', 'surename', 'age', 'email', 'created_at')
    list_filter = ('age', 'created_at')
    search_fields = ('name', 'surename', 'email')

    prepopulated_fields = {"slug": ("name", "surename")}

    readonly_fields = ('created_at',)

    fieldsets = (
        ("Asosiy malumotlar", {
            'fields': ('name', 'surename', 'age')
        }),
        ("Kontakt", {
            'fields': ('email', 'phone_number')
        }),
        ("Qo'shimcha", {
            'fields': ('picture', 'slug', 'created_at')
        }),
    )