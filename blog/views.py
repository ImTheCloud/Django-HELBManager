from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import (
    
    ListView,
    DetailView, 
    CreateView,
    UpdateView,
    DeleteView
) 
from .models import Post
from django import forms


class CommentForm(forms.Form):
    name = forms.CharField()
    url = forms.URLField()
    comment = forms.CharField(widget=forms.Textarea)
    



def home(request):
	context = {
		'posts' : Post.objects.all()
	}
	return render(request, 'blog/home.html', context)

class PostListView(ListView):
    model = Post
    template_name = 'blog/home.html' # <app>/<model>_<viewtype>.html
    context_object_name = 'posts'
    ordering = ['-date_posted']
    
class PostDetailView(DetailView):
    model = Post
    password = forms.CharField(widget=forms.PasswordInput)
    
class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    fields =['title','contributor','tasks_subtasks','status']
    
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    fields =['title','contributor','tasks_subtasks','status']
    
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
    
    def test_func(self):
        post = self.get_object()
       
        #if self.request.user == post.author:

        return True
    
        #return False
    
class PostDeleteView(LoginRequiredMixin , UserPassesTestMixin, DeleteView):
    model = Post
    success_url = '/'
    
    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False

def about(request):
	return render(request, 'blog/about.html', {'title': 'about'})
