from django.shortcuts import render
from datetime import datetime
from posts.models import Post


def welcome(request):
     
     return render(request, "website/welcome.html",
                  {"current_time":str(datetime.now()),
                   "posts": Post.objects.all(),
                   "name_posts":Post.objects.count()})
