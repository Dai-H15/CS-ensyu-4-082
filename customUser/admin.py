from django.contrib import admin
from . import models as customUserModels

# Register your models here.


class CustomUserAdmin(admin.ModelAdmin):
    list_display = ("PersonalData", "custom_user_Name", "custom_user_key", "Community")
    search_fields = ("custom_user_Name",)


class CommunityAdmin(admin.ModelAdmin):
    list_display = ("community_name", "community_Key", "introduce", "is_RegistByEmail")
    search_fields = ("community_name",)


admin.site.register(customUserModels.CustomUserModel, CustomUserAdmin)
admin.site.register(customUserModels.CommunityModel, CommunityAdmin)
