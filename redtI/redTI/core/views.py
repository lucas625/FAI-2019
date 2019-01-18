from django.shortcuts import render
from django.views import generic
from .helpers import modify_karma
# Create your views here.

class HomeView(generic.TemplateView):
    template_name = 'core/home.html'

class VoteView(generic.RedirectView):#redirectview só serve para redirecionar
    def get_redirect_url(self, *args, **kwargs):
        self.target_type = self.request.GET.get('target_type', None)#diz se é thread ou post
        self.target_id = self.request.GET.get('target_id', None)#qual o id do alvo
        modify_karma(self.target_type, self.target_id, self.request.user)
        return self.request.META.get('HTTP_REFERER')#da o refresh na página