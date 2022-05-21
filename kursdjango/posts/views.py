from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from posts.models import Post


def posts_list(request):
    result = "Lista postow<br>"
    posts = Post.objects.all()
    for post in posts:
        result += f"{post}<br>"
    return render(request, 'posts/list.html', {})



def post_details(request, id):
    result = "Szczegoly postu<br>"
    post = Post.objects.get(id=id)
    result += "<br>"
    result += str(post)
    return HttpResponse(result)