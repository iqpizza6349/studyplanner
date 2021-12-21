from member.models import BoardMember
from .models import Post
from .forms import BoardForm
from django.shortcuts import render, redirect


# Create your views here.
def board_list(request):
    boards = Post.objects.all().order_by('-id')
    return render(request, 'board_list.html', {"boards": boards})


def board_write(request):

    user_id = request.session.get('user')
    if not user_id:
        return redirect('/member/login')

    if request.method == "GET":
        form = BoardForm()

    elif request.method == "POST":
        form = BoardForm(request.POST, request.FILES)

        if form.is_valid():
            # form의 모든 validators 호출 유효성 검증 수행
            # 이 부분에 session 처리 예정
            user_id = request.session.get('user')
            name = BoardMember.objects.get(pk=user_id)

            board = Post()
            board.title     = form.cleaned_data['title']
            board.contents  = form.cleaned_data['contents']
            board.photos = form.cleaned_data['photos']
            board.writer = name

            board.save()
            return redirect('/board/')

    return render(request, 'board_write.html',{'form':form})


def board_detail(request, pk):
    post = Post.objects.get(pk=pk)

    return render(request, 'board_detail.html', {'post':post})


def board_remove(request, pk):
    user_id = request.session.get('user')
    name = BoardMember.objects.get(pk=user_id)
    post = Post.objects.get(pk=pk)
    if post.writer == name:
        post.delete()
        return redirect('/board/')
    return render(request, 'board_detail.html', {'post':post})

