from django.urls import path
from subs.views import SubreditisView, ThreadView, PostView, SubreditiView
app_name = "subs"

urlpatterns = [
    path('subreditis/', SubreditisView.as_view(), name="subreditis"),
    path('subrediti/<slug:slug>/', SubreditiView.as_view(), name="subrediti"),
    path('thread/<int:pk>/', ThreadView.as_view(), name="thread"),
    path('post/<int:pk>/', PostView.as_view(), name="post"),

]