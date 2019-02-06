from django.contrib import auth
from django.contrib.auth.models import AnonymousUser, User
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, redirect
from django.template.context_processors import csrf

from ahome.forms import LoginForm, UserCreation
from ahome.models import Verse, Book, Chapter, Diary


def home(request):
    args = dict()
    met = request.META['HTTP_USER_AGENT']

    print(type(met), met)
    if auth.get_user(request).username != AnonymousUser.username:
        args['user'] = auth.get_user(request)
    args['verse'] = Verse.objects.all()
    # args['book'] = Book.objects.all()
    return render(request, 'ahome/home.html', args)


def verse(request, verse_id):
    args = dict()
    args['ver'] = Verse.objects.get(id=verse_id)
    return render(request, 'ahome/verse.html', args)


def list_book(request):
    args = dict()
    args['bk'] = Book.objects.all()
    return render(request, 'ahome/list_book.html', args)


def chapter(request, book_id):
    args = dict()
    args['bk'] = Book.objects.get(id=book_id)
    args['chap'] = Chapter.objects.filter(book=book_id)
    return render(request, 'ahome/chapter.html', args)


def text(request, text_id, num, do):
    args = dict()
    num = int(num)
    args['max_pos'] = len(Chapter.objects.filter(book__chapter=text_id))
    id_bk = Chapter.objects.get(id=text_id).book_id
    filter_on_id = Chapter.objects.filter(book__id=id_bk)
    if do == "0":
        args['text'] = filter_on_id.get(numer=num)
    elif do == "1":
        args['text'] = filter_on_id.get(numer=num+1)
    elif do == "2":
        args['text'] = filter_on_id.get(numer=num-1)
    return render(request, 'ahome/text.html', args)


def log_in(request):
    args = dict()
    if auth.get_user(request).username != AnonymousUser.username:
        args['user'] = auth.get_user(request)
    args['form_in'] = LoginForm()
    return render(request, 'ahome/logging_in.html', args)


def log_on(request):
    args = dict()
    if auth.get_user(request).username != AnonymousUser.username:
        args['user'] = auth.get_user(request)
    args['form_reg'] = UserCreation()
    if request.POST:
        args.update(csrf(request))
        username = request.POST.get('username')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')
        try:
            us = User.objects.get(username=username)
            args['error_text'] = "Такой пользователь уже существует. "
            return render(request, 'ahome/log_on.html', args)
        except User.DoesNotExist:
            if password1 != password2:
                args['error_text'] = "Пароли не совпадают "
                return render(request, 'ahome/log_on.html', args)
            newuser_form = UserCreation(request.POST)
            if newuser_form.is_valid():
                newuser_form.save()
                newuser = auth.authenticate(username=newuser_form.cleaned_data['username'],
                                            password=newuser_form.cleaned_data['password2'])
                auth.login(request, newuser)
                return redirect("/")
            args['error_text'] = "Пароль должен содержать не менее 8 символов, состоять из бкув и цифр и не быть " \
                                 "распространенным."

    return render(request, 'ahome/log_on.html', args)


def ok_log(request):
    args = dict()
    if request.POST:
        args.update(csrf(request))
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('/')
        args['errorText'] = "Я не узнаю Вас в гриме :("
    return render(request, 'ahome/logging_in.html', args)


def log_out(request):
    auth.logout(request)
    return redirect("/")


def diary(request):
    args = dict()
    args['dir'] = Diary.objects.all().order_by('-created')
    return render(request, 'ahome/diary.html', args)


def note_content(request):
    args = dict()
    args.update(csrf(request))
    if request.POST:
        if request.POST.get('diary_id'):
            diary = request.POST.get('diary_id')
            description = Diary.objects.get(id=diary).description
            # json_orders_user = json.dumps(list(description), cls=DjangoJSONEncoder)
            # return JsonResponse(json_orders_user, safe=False)
            return HttpResponse(description)
        return JsonResponse(False, safe=False)

