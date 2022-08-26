from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth.mixins import PermissionRequiredMixin
from django.shortcuts import render
from django.views.generic import CreateView

from .models import *


def index(request):
    return render(request, 'index.html')


from django.views import generic


class BoardListView(generic.ListView):
    model = Board
    paginate_by = 10


@login_required
def profile(request):
    user = request.user
    cont = Contributor.objects.get(user=user)
    boards = Board.objects.filter(contributors__in=[cont])
    context = {
        'user': user,
        'cont': cont,
        'boards': boards
    }
    return render(request, 'contributor_detail.html', context=context)


class BoardDetailView(generic.DetailView):
    model = Board


class CreatePostView(PermissionRequiredMixin, CreateView):
    permission_required = 'task.change_task'
    model = Task
    fields = ('name', 'content')


@login_required
def change_task(request):
    return render(request, 'change_task.html')
