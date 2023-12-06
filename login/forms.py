from django import forms


class FormDefUser(forms.Form):
    username = forms.CharField(label="ユーザーID", max_length=20, required=True)
    email = forms.EmailField(label="Eメール", widget=forms.EmailInput(), required=True)
    first_name = forms.CharField(label="名", required=True)
    last_name = forms.CharField(label="姓", required=True)
    password = forms.CharField(label="パスワード", required=True, widget=forms.PasswordInput(), min_length=8)
