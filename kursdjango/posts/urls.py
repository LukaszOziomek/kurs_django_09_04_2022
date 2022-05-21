from django.urls import path
from posts.views import posts_list, post_details

urlpatterns = [
    path("", posts_list, name="list"),
    path("<int:id>", post_details, name="list"),


]