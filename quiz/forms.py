from django import forms
from quiz.models import Article

class quizMakeForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = ["image", "title", "detail", "result", "total_questions", "shuffle_q", "shuffle_c"]
        labels = {"image": "サムネイル画像", "title": "タイトル", "detail": "説明", "total_questions": "問題数", "result": "結果画面に表示したいテキスト", "shuffle_q": "問題をシャッフル", "shuffle_c": "選択肢をシャッフル"}
        widgets = {"detail": forms.Textarea, "result": forms.Textarea}

class quizEditForm(quizMakeForm):
    class Meta(quizMakeForm.Meta):
        fields = quizMakeForm.Meta.fields + ["body"]
        labels = quizMakeForm.Meta.labels.copy()
        labels["body"] = "クイズデータ"
        widgets = quizMakeForm.Meta.widgets.copy()
        widgets["body"] = forms.Textarea