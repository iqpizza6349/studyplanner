from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import BoardMember
from django.contrib.auth.hashers import make_password, check_password
from .forms import LoginForm


# Create your views here.
def register(request):
    if request.method == 'GET':
        return render(request, 'register.html')
    elif request.method == 'POST':
        name = request.POST.get('username', None)
        email = request.POST.get('email', None)
        password = request.POST.get('password', None)
        re_password = request.POST.get('re_password', None)
        res_data = {}

        if not (name and email and password and re_password):
            res_data['error'] = '모든 값을 입력해야 합니다'
            print(res_data)

        elif password != re_password:
            res_data['error'] = '비밀번호가 다릅니다.'
            print(res_data)

        elif BoardMember.objects.filter(username=name).exists():
            res_data['error'] = '중복된 아이디입니다'

        else:
            member = BoardMember(
                username=name,
                password=make_password(password),
                email=email,
            )
            member.save()
            return redirect('/')

        return render(request, 'register.html', res_data)


# def login(request):
#     res_data = {}
#     try:
#         if request.method == "GET":
#             return render(request, 'login.html')
#         elif request.method == "POST":
#             username = request.POST.get('username', None)
#             password = request.POST.get('password', None)
#             if not (username and password):
#                 res_data['error'] = '모든 값을 입력하세요!'
#             else:
#                 member = BoardMember.objects.get(username=username)
#
#                 if check_password(password, member.password):
#                     request.session['user'] = member.id
#                     return redirect('/loginsuccess')
#                 else:
#                     res_data['error'] = '비밀번호가 다릅니다!'
#     except BoardMember.DoesNotExist:
#         res_data['error'] = '아이디가 없습니다.'
#     return render(request, 'login.html', res_data)

def login(request):
    if request.method == 'GET':
        form = LoginForm()
    elif request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            request.session['user'] = form.user_id
            return redirect('/')

    return render(request, 'login.html', {'form' : form})


def loginsuccess(request):
    user_id = request.session.get('user')

    if user_id:
        member = BoardMember.objects.get(pk=user_id)
        return HttpResponse(member.username)

    return HttpResponse('Home!')


def logout(request):
    if request.session.get('user'):
        del(request.session['user'])

    return redirect('/')
