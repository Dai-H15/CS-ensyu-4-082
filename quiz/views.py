from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, HttpResponse, Http404, JsonResponse
from django.utils import timezone
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from quiz.models import Article, Comment
from customUser.models import CustomUserModel as CustomUser
from django.db import IntegrityError
from .forms import quizMakeForm
import json


# Create your views here.
def index(request):
    try:
        if request.session["is_custom_selected"] is False:
            return redirect("portal")
    except KeyError:
        return redirect("portal")
    articles_posted_at = Article.objects.order_by('-posted_at')
    articles_answer = Article.objects.order_by('-answer')
    contexts = {
        "articles_posted_at": articles_posted_at,
        "articles_answer": articles_answer,
    }
    contexts["CustomUserData"] = CustomUser.objects.get(custom_user_key=request.session["CustomUserKey"])
    return render(request, "quiz/index.html", contexts)


def make(request):
    contexts = {}
    if request.method == "POST":
        try:
            form = quizMakeForm(request.POST)
            if form.is_valid():
            # Concatenate question values into the "body" field
                quiz = form.save(commit=False)
                total_questions = quiz.total_questions
                questions = []
                for i in range(1, total_questions + 1):
                    question = dict()
                    q = list(request.POST.get(f"question_{i}").split("\r\n"))
                    question["question"] = q[0]
                    question["select1"] = q[1]
                    question["select2"] = q[2]
                    question["select3"] = q[3]
                    question["select4"] = q[4]
                    question["correct"] = int(q[5])
                    questions.append(json.dumps(question, ensure_ascii=False, indent=2))
                body_content = ",".join(questions)
                body_content = "[" + body_content + "]"
                quiz.body = body_content

                # Save the form with updated data
                quiz.save()
                return redirect("detail", article_id=quiz.id)
        except Exception:
            contexts["res"] = "1"
    else:
        contexts["form"] = quizMakeForm()
    contexts["CustomUserData"] = CustomUser.objects.get(custom_user_key=request.session["CustomUserKey"])
    return render(request, "quiz/make.html", contexts)


def play(request):
    flag_posted_at = ''
    flag_like = ''
    flag_answer = ''
    flag_community = ''
    if ('sort' in request.GET):
        if request.GET['sort'] == 'like':
            articles = Article.objects.order_by('-like')
            flag_like = 'active'
        elif request.GET['sort'] == 'answer':
            articles = Article.objects.order_by('-answer')
            flag_answer = 'active'
        elif request.GET['sort'] == 'community':
            #articles = Article.objects.get(community=community_id)
            articles = Article.objects.order_by('-posted_at')
            flag_community = 'active'
        else:
            articles = Article.objects.order_by('-posted_at')
            flag_posted_at = 'active'
    else:
        articles = Article.objects.order_by('-posted_at')
        flag_posted_at = 'active'

    context = {
        "articles": articles,
        "flag_posted_at": flag_posted_at,
        "flag_like": flag_like,
        "flag_answer": flag_answer,
        "flag_community": flag_community,
    }
    context["CustomUserData"] = CustomUser.objects.get(custom_user_key=request.session["CustomUserKey"])
    return render(request, 'quiz/play.html', context)


def detail(request, article_id):
    try:
        article = Article.objects.get(pk=article_id)
    except Article.DoesNotExist:
        raise Http404("Aricle does not exist")
    if request.method == 'POST':
        comment = Comment(article=article, text=request.POST['text'])
        comment.save()
    context = {
        'article': article,
        'comments': article.comments.order_by('-posted_at')
    }
    context["CustomUserData"] = CustomUser.objects.get(custom_user_key=request.session["CustomUserKey"])
    return render(request, "quiz/detail.html", context)


def exam(request, article_id):
    try:
        article = Article.objects.get(pk=article_id)
    except Article.DoesNotExist:
        raise Http404("Aricle does not exist")
    context = {
        'article': article,
        'comments': article.comments.order_by('-posted_at')
    }
    if request.method == 'POST':
        context['result_text'] = request.POST['result_text']
        if 'text' in request.POST:
            comment = Comment(article=article, text=request.POST['text'])
            comment.save()
        context["CustomUserData"] = CustomUser.objects.get(custom_user_key=request.session["CustomUserKey"])
        return render(request, 'quiz/result.html', context)
    context["CustomUserData"] = CustomUser.objects.get(custom_user_key=request.session["CustomUserKey"])
    return render(request, 'quiz/exam.html', context)


def api_like(request, article_id):
    try:
        article = Article.objects.get(pk=article_id)
        article.like += 1
        article.save()
    except Article.DoesNotExist:
        raise Http404("Article does not exist")
    result = {
        'id' : article_id,
        'like' : article.like
    }
    return JsonResponse(result)


def api_answer(request, article_id):
    try:
        article = Article.objects.get(pk=article_id)
        article.answer += 1
        article.save()
    except Article.DoesNotExist:
        raise Http404("Article does not exist")
    return