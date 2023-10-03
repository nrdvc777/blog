from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin


from blog.models import Post
# Create your views here.
class BlogListView(ListView):
    model = Post
    template_name = 'home.html'

class BlogCreateView(LoginRequiredMixin, CreateView):
    model = Post
    template_name = 'post_new.html'
    fields = ['title', 'body']

    def form_valid(self, form):
        form.instance.author_id = self.request.user.id
        return super().form_valid(form)

class BlogDetailView(DetailView):
    model = Post
    template_name = 'post_detail.html'

class BLogUpdateView(LoginRequiredMixin, UpdateView):  
    model = Post  
    template_name = 'post_edit.html'  
    fields = ['title', 'body']



class BlogdDeleteView(DeleteView):
    model = Post
    template_name = 'post_delete.html'
    success_url = reverse_lazy('home')

    # def getqueryset(self):
    #   queryset = super().getqueryset()
    #   return queryset.filter(author=self.request.user)

def pnf404View(request):
    return render(request, '404.html')


def servererror500(request):
    return render(request, '500.html')