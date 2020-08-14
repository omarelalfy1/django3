
from django.views.generic.edit import UpdateView,CreateView,DeleteView
from django.views.generic import ListView,DetailView
from .models import Post
from django.urls import reverse_lazy
# Create your views here.

class TopicListView(ListView):
    model = Post
    template_name = "home.html"

class TopicDetailView(DetailView):
    model = Post
    template_name = "post_detail.html"

class TopicCreatView(CreateView):
    model = Post
    template_name = "post_new.html"
    fields="__all__"
class TopicDeleteView(DeleteView):
    model = Post
    template_name = "post_delete.html"
    success_url = reverse_lazy("home")

class TopicUpdateView(UpdateView,):
    model = Post
    template_name = "post_edit.html"
    fields = ["title","body"]



