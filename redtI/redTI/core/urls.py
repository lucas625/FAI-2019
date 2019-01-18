from django.urls import path
from core.views import HomeView, VoteView

app_name = "core"

urlpatterns = [
    path('', HomeView.as_view(), name="home"),
    path('vote', VoteView.as_view(), name='vote'),
]