from django.shortcuts import render
from .models import CustomUserModel as CustomUser
from .models import CommunityModel as Communuty
from login.models import PersonalData
from .forms import CustomUserForm, CommunityModelForm
import secrets
import re


def ShowCustomUsers(self):
    return CustomUser.objects.filter(PersonalData=PersonalData.objects.get(user=self.user))


def CollectPersonalData(self):
    return PersonalData.objects.get(user=self.user)


def CollectCommunity(self):
    return Communuty.objects.get(community_Key=self.POST.get("Community"))


def Check_is_RegistByEmail(self):
    if re.fullmatch(r"@[a-z]+[.]+[a-z]+[.]*[a-z]*", (self.POST.get("community_name"))) is None:
        return False
    else:
        return True


def Check_Community(PersonalData, community):
    user_mail_addr = PersonalData.email
    community_name = community.community_name
    if re.search(community_name, user_mail_addr) is None:
        return False
    else:
        return True


def CreateCustomUser(request):
    contexts = {}
    if request.method == "POST":
        form = CustomUserForm(request.POST)
        if form.is_valid():
            data = CustomUser()
            data.PersonalData = CollectPersonalData(request)
            data.Customdata = form.cleaned_data.get("Customdata")
            data.custom_user_Name = form.cleaned_data.get("custom_user_Name")
            data.custom_user_key = secrets.token_hex(32)
            data.Community = CollectCommunity(request)
            if data.Community.is_RegistByEmail:
                if Check_Community(CollectPersonalData(request), CollectCommunity(request)):
                    data.save()
                    contexts["message"] = "登録が完了しました。限定コミュニティーに所属しています"
                    contexts["res"] = "0"
                else:
                    contexts["message"] = "このコミュニティーには参加できません。"
                    contexts["res"] = "1"
            else:
                data.save()
                contexts["message"] = "登録が完了しました。公開コミュニティーに所属しています"
                contexts["res"] = "0"
        else:
            contexts["message"] = "登録に失敗しました。入力値を確かめてください"
            contexts["res"] = "1"
    users = ShowCustomUsers(request)
    contexts["CustomUsers"] = users
    contexts["form"] = CustomUserForm
    contexts["PersonalData"] = CollectPersonalData(request)
    return render(request, "customUser/create/customuser.html", contexts)


def CreateCommunity(request):
    contexts = {}
    if request.method == "POST":
        form = CommunityModelForm(request.POST)
        if form.is_valid():
            if Communuty.objects.filter(community_name=form.cleaned_data.get("community_name")).exists():
                contexts["res"] = "1"
                contexts["message"] = "コミュニティーの作成に失敗しました。すでに存在しています"
            else:
                data = Communuty()
                data.community_Key = secrets.token_hex(32)
                data.community_name = form.cleaned_data.get("community_name")
                data.introduce = form.cleaned_data.get("introduce")
                data.is_RegistByEmail = Check_is_RegistByEmail(request)
                data.save()
                contexts["res"] = "0"
                if Check_is_RegistByEmail(request):
                    contexts["message"] = "コミュニティーを作成しました。同じドメインに所属するユーザーのみ所属することができます"
                else:
                    contexts["message"] = "コミュニティーを作成しました。すべてのユーザーが所属することができます"
        else:
            contexts["res"] = "1"
            contexts["message"] = "コミュニティーの作成に失敗しました。"
    contexts["form"] = CommunityModelForm
    return render(request, "customUser/create/community.html", contexts)
