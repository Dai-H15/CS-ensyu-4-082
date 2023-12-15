from django import forms 
from .models import CustomUserModel, CommunityModel


class CustomUserForm(forms.ModelForm):
    class Meta:
        model = CustomUserModel
        fields = ("custom_user_Name", "Community", "Customdata")
        labels = {
            "custom_user_Name": "カスタムユーザー名",
            "Community": "所属コミュニティ",
            "Customdata": "プロフィール"
        }


class CommunityModelForm(forms.ModelForm):
    class Meta:
        model = CommunityModel
        fields = ("community_name", "introduce")
        labels = {
            "community_name": "コミュニティー名",
            "introduce": "紹介文"
        }
