from django.contrib import admin
from .models import PersonalData
# Register your models here.


class PersonalDataAdmin(admin.ModelAdmin):
    list_display = ("username", "FirstName", "LastName", "birth", "phone", "user_key", "email", "image", "user")
    search_fields = ("username",)
    readonly_fields = ("username", "user_key", "user")


admin.site.register(PersonalData, PersonalDataAdmin)
