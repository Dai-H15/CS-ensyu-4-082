from django.shortcuts import render
from .models import CustomUserModel as CustomUser
from .models import CommunityModel as Communuty
from login.models import PersonalData
from .forms import CustomUserForm, CommunityModelForm, EditCustomUserForm
import secrets
import re
import PIL


def is_image(file):
    try:
        with PIL.Image.open(file):
            return True
    except PIL.UnidentifiedImageError:
        return False


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


def EditCustmUserData(CustomUserData, request, contexts):
    if CustomUserData.Community.is_RegistByEmail:
        if Check_Community(CollectPersonalData(request), CollectCommunity(request)):  # コミュニティーに所属できるかどうか確認
            if request.FILES:
                if is_image(request.FILES["image"]):
                    CustomUserData.image = request.FILES["image"]
                    contexts["res"] = "0"
                    contexts["message"] = "編集が完了しました。画像が変更されました。限定コミュニティに所属しています"
                else:
                    contexts["res"] = "0"
                    contexts["message"] = "画像の形式が不正です。画像を除くプロフィールの編集が完了しました。限定コミュニティに所属しています"
            else:
                contexts["res"] = "0"
                contexts["message"] = "編集が完了しました。画像は変更されていません。限定コミュニティに所属しています"
            CustomUserData.save()
        else:
            contexts["res"] = "1"
            contexts["message"] = "編集に失敗しました。そのコミュニティーには所属できません。メールアドレスを確認してください"
    else:  # 限定じゃないコミュニティー
        if request.FILES:
            if is_image(request.FILES["image"]):
                CustomUserData.image = request.FILES["image"]
                contexts["res"] = "0"
                contexts["message"] = "編集が完了しました。公開コミュニティに所属しています"
            else:
                contexts["res"] = "0"
                contexts["message"] = "画像の形式が不正です。画像を除くプロフィールの編集が完了しました。公開コミュニティに所属しています"
        else:
            contexts["res"] = "0"
            contexts["message"] = "編集が完了しました。画像は変更されていません。公開コミュニティに所属しています"
        CustomUserData.save()
        return CustomUserData, request, contexts


def CreateCustomUser(request):
    contexts = {}
    if request.method == "POST":
        form = CustomUserForm(data=request.POST, files=request.FILES)
        if form.is_valid():
            data = CustomUser()
            data.PersonalData = CollectPersonalData(request)
            data.Customdata = form.cleaned_data.get("Customdata")
            data.custom_user_Name = form.cleaned_data.get("custom_user_Name")
            data.custom_user_key = secrets.token_hex(32)
            data.Community = CollectCommunity(request)
            if CustomUser.objects.filter(Community=data.Community).filter(custom_user_Name=data.custom_user_Name).exists():
                contexts["message"] = "このコミュニティーには参加できません。すでにそのユーザー名は使用されています"
                contexts["res"] = "1"
            elif data.Community.is_RegistByEmail:
                if Check_Community(CollectPersonalData(request), CollectCommunity(request)):
                    if request.FILES:
                        if is_image(request.FILES["image"]):
                            data.image = request.FILES["image"]
                            contexts["res"] = "0"
                            contexts["message"] = "登録が完了しました。限定コミュニティーに所属しています"
                        else:
                            contexts["res"] = "0"
                            contexts["message"] = "画像の形式が不正です。画像を除くプロフィールの登録が完了しました。限定コミュニティーに所属しています"
                    data.save()
                else:
                    contexts["message"] = "このコミュニティーには参加できません。"
                    contexts["res"] = "1"
            else:
                if request.FILES:
                    if is_image(request.FILES["image"]):
                        data.image = request.FILES["image"]
                        contexts["res"] = "0"
                        contexts["message"] = "登録が完了しました。公開コミュニティーに所属しています"
                    else:
                        contexts["res"] = "0"
                        contexts["message"] = "画像の形式が不正です。画像を除くプロフィールの登録が完了しました。公開コミュニティーに所属しています"
                data.save()
            contexts["forms"] = form
        else:
            contexts["message"] = "登録に失敗しました。入力値を確かめてください"
            contexts["res"] = "1"
            contexts["forms"] = form
    else:
        contexts["forms"] = CustomUserForm
    users = ShowCustomUsers(request)
    contexts["CustomUsers"] = users
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
    contexts["form"] = CommunityModelForm()
    return render(request, "customUser/create/community.html", contexts)


def EditCustomUser(request):
    contexts = {}
    if request.method == "POST":
        if request.POST.get("selectusers"):
            request.session["CustomUserKey"] = request.POST.get("selectusers")
            CustomUserData = CustomUser.objects.get(custom_user_key=request.POST.get("selectusers"))
            if CustomUserData.image:
                contexts["image_url"] = CustomUserData.image.url
            contexts["editform"] = EditCustomUserForm(initial={
                "custom_user_Name": CustomUserData.custom_user_Name,
                "Community": CustomUserData.Community,
                "Customdata": CustomUserData.Customdata,
                "custom_user_key": request.POST.get("selectusers"),
                })
        else:
            try:
                form = EditCustomUserForm(data=request.POST, files=request.FILES, instance=CustomUser.objects.get(custom_user_key=request.POST.get("custom_user_key")))
                print(form.errors)
                if form.is_valid():
                    CustomUserData = CustomUser.objects.get(custom_user_key=form.cleaned_data.get("custom_user_key"))
                    CustomUserData.custom_user_Name = form.cleaned_data.get("custom_user_Name")
                    CustomUserData.Community = CollectCommunity(request)
                    CustomUserData.Customdata = form.cleaned_data.get("Customdata")
                    print(CustomUser.objects.filter(Community=CollectCommunity(request)).filter(custom_user_Name=form.cleaned_data.get("custom_user_Name")))
                    if CustomUser.objects.filter(Community=CollectCommunity(request)).filter(custom_user_Name=form.cleaned_data.get("custom_user_Name")).exists():  # 複数ユーザー名の重複
                        s = CustomUser.objects.filter(Community=CollectCommunity(request)).filter(custom_user_Name=form.cleaned_data.get("custom_user_Name")).filter(custom_user_Name=form.cleaned_data.get("custom_user_Name")).get().custom_user_key
                        print(s)
                        if s != request.session["CustomUserKey"]:
                            print(type(CollectCommunity(request)))
                            if CollectCommunity(request) == "Everyone":
                                contexts["res"] = "1"
                                contexts["message"] = "編集に失敗しました。すでにそのコミュニティーに所属しているか、すでにそのコミュニティーには同じ名前のユーザーが存在します"
                            else:
                                CustomUserData, request, contexts = EditCustmUserData(CustomUserData, request, contexts)
                        else:
                            CustomUserData, request, contexts = EditCustmUserData(CustomUserData, request, contexts)
                    else:
                        if CustomUserData.Community.is_RegistByEmail:
                            if Check_Community(CollectPersonalData(request), CollectCommunity(request)):  # コミュニティーに所属できるかどうか確認
                                if request.FILES:
                                    if is_image(request.FILES["image"]):
                                        CustomUserData.image = request.FILES["image"]
                                        contexts["res"] = "0"
                                        contexts["message"] = "編集が完了しました。画像が変更されました。限定コミュニティに所属しています"
                                    else:
                                        contexts["res"] = "0"
                                        contexts["message"] = "画像の形式が不正です。画像を除くプロフィールの編集が完了しました。限定コミュニティに所属しています"
                                else:
                                    contexts["res"] = "0"
                                    contexts["message"] = "編集が完了しました。画像は変更されていません。限定コミュニティに所属しています"
                                CustomUserData.save()
                            else:
                                contexts["res"] = "1"
                                contexts["message"] = "編集に失敗しました。そのコミュニティーには所属できません。メールアドレスを確認してください"
                        else:  # 限定じゃないコミュニティー
                            if request.FILES:
                                if is_image(request.FILES["image"]):
                                    CustomUserData.image = request.FILES["image"]
                                    contexts["res"] = "0"
                                    contexts["message"] = "編集が完了しました。公開コミュニティに所属しています"
                                else:
                                    contexts["res"] = "0"
                                    contexts["message"] = "画像の形式が不正です。画像を除くプロフィールの編集が完了しました。公開コミュニティに所属しています"
                            else:
                                contexts["res"] = "0"
                                contexts["message"] = "編集が完了しました。画像は変更されていません。公開コミュニティに所属しています"
                            CustomUserData.save()
                else:
                    contexts["res"] = "1"
                    contexts["message"] = "編集に失敗しました。値を確認してください"
                CustomUserData = CustomUser.objects.get(custom_user_key=form.cleaned_data.get("custom_user_key"))
                if CustomUserData.image:
                    contexts["image_url"] = CustomUserData.image.url
                contexts["editform"] = EditCustomUserForm(initial={
                    "custom_user_Name": CustomUserData.custom_user_Name,
                    "Community": CustomUserData.Community,
                    "Customdata": CustomUserData.Customdata,
                    "custom_user_key": request.POST.get("custom_user_key"),
                    })
            except CustomUser.DoesNotExist:
                contexts["res"] = "1"
                contexts["message"] = "対象のユーザーが存在しません"
            except CustomUser.MultipleObjectsReturned:
                contexts["res"] = "1"
                contexts["message"] = "エラーが発生しました"
    users = ShowCustomUsers(request)
    contexts["users"] = users.all()
    return render(request, "customUser/edit/customuser.html", contexts)
