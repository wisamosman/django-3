from django.shortcuts import render
from .models import post
from .forms import postForm
# Create your views here.
def post_list(request):
    date = post.objects.all()
    return render(request,'posts/posts.html',{'posts':date})

def post_detail(request,post_id):
    date = post.objects.get(id=post_id)
    return render(request,'posts/detail.html',{'post':date})

def new_post(request):
    from = postForm()
    return render(request,'posts/new.html',{'form':form})