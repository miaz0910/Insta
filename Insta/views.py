from django.views.generic import TemplateView, ListView,DetailView
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.urls import reverse,reverse_lazy
from Insta.models import Post
from Insta.forms import CustomUserCreationForm
from django.contrib.auth.mixins import LoginRequiredMixin

class HelloWorld(TemplateView):
    template_name='test.html'

class PostsView(ListView):
    model=Post
    template_name='index.html'

class PostDetailView(DetailView):
    model=Post
    template_name='post_detail.html'

class PostCreateView(LoginRequiredMixin, CreateView):
    model=Post
    template_name='post_create.html'
    fields = '__all__'
    login_url='login'

class PostUpdateView(UpdateView):
    model=Post
    template_name='post_update.html'
    fields =['title']

class PostDeleteView(DeleteView):
    model=Post
    template_name='post_delete.html'
    success_url=reverse_lazy("posts")

class SignUp(CreateView):
    form_class=CustomUserCreationForm
    success_url=reverse_lazy("login")
    template_name='signup.html'
