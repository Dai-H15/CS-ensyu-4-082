from django import forms
from quiz.models import Article

class quizMakeForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = ("image", "title", "detail", "result", "total_questions", "shuffle_q", "shuffle_c")
        labels = {"image": "サムネイル画像", "title": "タイトル", "detail": "説明", "total_questions": "問題数", "result": "結果画面に表示したいテキスト", "shuffle_q": "問題をシャッフル", "shuffle_c": "選択肢をシャッフル"}
        widgets = {"detail": forms.Textarea, "result": forms.Textarea}
        
    '''
    title = forms.CharField(label="タイトル", max_length=200, required=True)
    detail = forms.CharField(label="説明", widget=forms.Textarea, required=True)
    total_questions = forms.IntegerField(label="問題数", min_value=0, required=True)
    body = forms.CharField(label="クイズ本体", widget=forms.Textarea, required=True)
    result = forms.CharField(label="結果", widget=forms.Textarea, required=True)
    '''