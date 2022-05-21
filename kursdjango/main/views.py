from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def hello(request, text="Django!"):
    return HttpResponse(f"Hello {text}")


# /hello/<sent1>/<sent2>  -> <H1>sent1 sent2</H1>
def custom_greetings(request, sent1, sent2):
    return HttpResponse(f"<h1>{sent1} {sent2}</h1>")

