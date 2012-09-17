from django.shortcuts import render, get_object_or_404
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

def view(request, username):
    user = get_object_or_404(User, username=username)

    return render(request, 'profile/view.html', {
        'user': user,
    })

@login_required
def edit(request):
    return render(request, 'profile/edit.html')
