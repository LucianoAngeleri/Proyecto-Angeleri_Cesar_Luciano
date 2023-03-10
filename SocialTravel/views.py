from django.shortcuts import render
from django.urls import reverse_lazy
from SocialTravel.models import Post

from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

# Create your views here.
def index(request):
    return render(request, "SocialTravel/index.html")

def mostrar_otro_template(request):
    posts = Post.objects.all()
    return render(request, "SocialTravel/otro_template.html",{"post":posts})
































class PostList(ListView):
    model = Post    
    context_object_name ="posts"
class PostDetail(DetailView):
    model = Post  
    context_object_name ="post"
class PostUpdate(UpdateView):
    model = Post  
    success_url = reverse_lazy("post-list")
    fields = '__all__'

class PostDelete(DeleteView):
    model = Post  
    success_url = reverse_lazy("post-list")
    fields = '__all__'
class PostCreate(CreateView):
    model = Post  
    success_url = reverse_lazy("post-list")
    fields = '__all__'
class PostSearch(ListView):
    model = Post
    context_object_name ="posts"

    def get_queryset(self):
        criterio = self.request.GET.get("criterio")
        result = Post.objects.filter(carousel_caption_title__icontains=criterio).all()
        return result
