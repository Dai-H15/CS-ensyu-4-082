from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate
from django.db import IntegrityError
from .forms import FormDefUser
from customUser.models import CustomUserModel, CommunityModel
from .models import PersonalData
import PIL


def is_image(file):
    try:
        with PIL.Image.open(file):
            return True
    except PIL.UnidentifiedImageError:
        return False


def createDefUser(request):
    contexts = {}
    if request.method == "POST":
        username = request.POST.get("username")
        email = request.POST.get("email")
        first_name = request.POST.get("first_name")
        last_name = request.POST.get("last_name")
        password = request.POST.get("password")
        confirm = request.POST.get("confirm")
        if password == confirm:
            try:
                Newuser = User.objects.create_user(
                    username, email, password, first_name=first_name, last_name=last_name
                )
                Newuser.save()
                contexts["res"] = "0"
                aut = authenticate(username=username, password=password)
                login(request, aut)
            except IntegrityError:
                contexts["res"] = "1"
                contexts["message"] = "ユーザーの作成に失敗しました。そのユーザーIDはすでに使用されています。"
        else:
            contexts["res"] = "1"
            contexts["message"] = "ユーザーの作成に失敗しました。パスワードが一致しません"
    contexts["form"] = FormDefUser()
    return render(request, "login/createUser.html", contexts)


def editUser(request):
    contexts = {}
    if request.method == "POST":
        contexts["res"] = ""
        password = request.POST.get("password")
        username = request.POST.get("username")
        print(username, password)
        if authenticate(username=username, password=password) is None:
            contexts["res"] += "認証に失敗しました。パスワードを確かめてください。"
        else:
            s = PersonalData.objects.get(user_id=request.user.id)
            s.FirstName = request.POST.get("FirstName")
            s.LastName = request.POST.get("LastName")
            if s.email != request.POST.get("email"):
                CustomUsers = CustomUserModel.objects.filter(PersonalData=s).all()
                Everyone = CommunityModel.objects.get(community_name="Everyone")
                for user in CustomUsers:
                    user.Community = Everyone
                    user.save()
                contexts["res"] += "メールアドレスが変更されたため、すべてのカスタムユーザーの所属コミュニティがEveryoneに変更になりました。必要であれば、再度設定し直してください。"
            s.email = request.POST.get("email")
            s.phone = request.POST.get("phone")
            s.birth = request.POST.get("birth")
            if request.FILES:
                if is_image(request.FILES["image"]):
                    s.image = request.FILES["image"]
                else:
                    contexts["res"] += "画像の形式が不正です。画像を除くプロフィールの"
            s.save()
            contexts["res"] += "保存に成功しました"
    s = PersonalData.objects.get(user_id=request.user.id)
    print(s.image)
    contexts["username"] = s.username
    contexts["FirstName"] = s.FirstName
    contexts["LastName"] = s.LastName
    contexts["email"] = s.email
    contexts["phone"] = s.phone
    contexts["birth"] = s.birth
    if s.image:
        contexts["image_url"] = s.image.url
    c = CustomUserModel.objects.filter(PersonalData=s)
    contexts["customUsers"] = c
    return render(request, "login/editUser.html", contexts)