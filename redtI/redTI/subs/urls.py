from django.urls import path
from subs.views import SubreditisView, ThreadView, PostView, SubreditiView, SubreditiCreateView, CreateThreadView, CreatePostView
app_name = "subs"

urlpatterns = [
    path('subreditis/', SubreditisView.as_view(), name="subreditis"),
    path('subreditiCreate/', SubreditiCreateView.as_view(), name="subreditiCreate"),
    path('subrediti/<slug:slug>/', SubreditiView.as_view(), name="subrediti"),
    path('thread/<int:pk>/', ThreadView.as_view(), name="thread"),
    path('threads/create', CreateThreadView.as_view(), name="create_thread"),
    path('post/<int:pk>/', PostView.as_view(), name="post"),
    path('posts/create', CreatePostView.as_view(), name="create_post"),

]