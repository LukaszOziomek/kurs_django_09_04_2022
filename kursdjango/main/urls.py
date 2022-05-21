from django.urls import path

from main.views import hello, custom_greetings

# poczatek =  /hello
urlpatterns = [

    path('', hello, name="hello"),  # /
    path('<text>/', hello, name="hello2"),  #  /Gabrielka
    path(
        "<sent1>/<sent2>/", custom_greetings, name="custom_greetings)"
    ), # poczatek + /<sent1><sent2>
]