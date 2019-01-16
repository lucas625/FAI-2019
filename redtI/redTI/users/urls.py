from django.urls import path
from users.views import ProfileView, LogoutView, LoginView, CadastroView
app_name = "users"

urlpatterns = [
    path('profile/<int:pk>/', ProfileView.as_view(), name="profile"),
    path('logout/', LogoutView.as_view(), name="logout"),
    path('login/', LoginView.as_view(), name="login"),
    path('cadastro/', CadastroView.as_view(), name="cadastro"),
]