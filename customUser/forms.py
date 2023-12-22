from django import forms
from .models import CustomUserModel, CommunityModel


class CustomUserForm(forms.ModelForm):
    class Meta:
        model = CustomUserModel
        fields = ("custom_user_Name", "Community", "Customdata", "image")
        labels = {
            "custom_user_Name": "カスタムユーザー名",
            "Community": "所属コミュニティー",
            "Customdata": "プロフィール",
            "image": "プロフィール画像"
        }


class CommunityModelForm(forms.ModelForm):
    class Meta:
        model = CommunityModel
        fields = ("community_name", "introduce")
        labels = {
            "community_name": "コミュニティー名",
            "introduce": "紹介文"
        }


class EditCustomUserForm(forms.ModelForm):
    custom_user_key = forms.CharField(widget=forms.HiddenInput)

    class Meta:
        model = CustomUserModel
        fields = ("image", "custom_user_Name", "Customdata", "Community", "custom_user_key")
        labels = {
            "custom_user_Name": "カスタムユーザー名",
            "Community": "所属コミュニティー",
            "Customdata": "プロフィール",
            "image": "プロフィール画像"
        }
