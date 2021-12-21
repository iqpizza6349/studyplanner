from django.shortcuts import render, redirect
from .models import *
from member.models import BoardMember


def PlannerView(request):
    user_id = request.session.get('user')
    if not user_id:
        return redirect('/member/login')
    name = BoardMember.objects.get(pk=user_id)
    if request.method == "GET":
        boards = {'boards': Board.objects.filter(username=name)}
        return render(request, 'planners/planners.html', boards)

    elif request.method == "POST":
        username = name
        subject = request.POST['subject']
        goal = request.POST['goal']
        passs = request.POST['passs']
        time = request.POST['time']
        if subject == "":
            return redirect("/planners")
        board = Board(username=username, subject=subject, goal=goal, passs=passs, time=time)
        board.save()
        boards = {'boards': Board.objects.filter(username=name)}
        return render(request, 'planners/planners.html', boards)

    template_name = 'planners.html'


def PlanDetail(request, pk):
    user_id = request.session.get('user')
    name = BoardMember.objects.get(pk=user_id)
    if request.method == "GET":
        boards = Board.objects.get(pk=pk)
        return render(request, 'planners/plandetail.html', {'board':boards})
    elif request.method == "POST" and "insert" in request.POST:
        board = Board.objects.get(pk=pk)
        board.username = name
        board.subject = request.POST['subject']
        board.goal = request.POST['goal']
        board.passs = request.POST['passs']
        board.time = request.POST['time']
        board.save()
        return redirect("/planners")

    elif request.method == "POST" and "delete" in request.POST:
        board = Board.objects.get(pk=pk)
        board.delete()
        return redirect("/planners")