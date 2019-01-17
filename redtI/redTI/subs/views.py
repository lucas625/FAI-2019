from .models import Subrediti, Thread, Post
from django.shortcuts import render
from django.urls import reverse_lazy
from django.contrib.auth import views
from django.views import generic
from .forms import CreateThreadForm
# Create your views here.
class SubreditisView(generic.ListView):
    template_name = 'subs/subreditis.html'
    model = Subrediti
    context_object_name = 'subreditis'

class SubreditiView(generic.DetailView):
    template_name = 'subs/subrediti.html'
    model = Subrediti

class SubreditiCreateView(generic.CreateView):
    fields = [
        'title',
        'descricao',
    ]
    success_url = reverse_lazy('subs:subreditis')
    model = Subrediti
    template_name = 'subs/subreditiCreate.html'

    def form_valid(self, form):#estamos sobre escrevendo a validação do formulário.
        self.object = form.save(commit=False)
        self.object.criador_id = self.request.user.id#pegamos assim o usuário
        slug = self.object.title
        slug = slug.replace(' ', '-')
        self.object.slug = slug
        self.object.save()
        return super(generic.edit.ModelFormMixin, self).form_valid(form)

class ThreadView(generic.DetailView):
    template_name = 'subs/thread.html'
    model = Thread

class CreateThreadView(generic.CreateView):
    template_name = 'subs/create_thread.html'
    model = Thread
    form_class = CreateThreadForm

    def get_initial(self):
        self.subrediti = self.request.GET.get('sub', None)#GET pega do http e o get pega do dicionario, o segundo é o default
        return {
            'subrediti': Subrediti.objects.get(id=self.subrediti),
            'autor': self.request.user
        }
    
    def get_context_data(self, **kwargs):#vai ser para mostrar em qual subrediti estamos criando a thread
        context = super().get_context_data(**kwargs)
        context['subrediti'] = Subrediti.objects.get(id=self.subrediti)
        return context

    def get_success_url(self):
        subrediti = Subrediti.objects.get(id=self.subrediti)
        return reverse_lazy('subs:subrediti', kwargs={'slug': subrediti.slug})


class PostView(generic.DetailView):
    template_name = 'subs/post.html'
    model = Post

class CreatePostView(generic.CreateView):
    fields = [
        'content',
    ]
    model = Post
    template_name = 'subs/create_post.html'
    def get_initial(self):
        self.thread = self.request.GET.get('thread', None)

    def form_valid(self, form):#estamos sobre escrevendo a validação do formulário.
        self.object = form.save(commit=False)
        self.object.autor_id = self.request.user.id#pegamos assim o usuário
        self.object.thread_id = self.thread
        self.object.save()
        return super(generic.edit.ModelFormMixin, self).form_valid(form)

    def get_success_url(self):
        thread = Thread.objects.get(id=self.thread)
        return reverse_lazy('subs:thread', kwargs={'pk': thread.pk})