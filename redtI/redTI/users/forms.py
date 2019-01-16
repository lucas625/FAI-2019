from django import forms

from .models import User

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())#widget muda o tipo de input
    confirm_password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = [
            'username', 'email', 'password'
        ]
    
    def clean(self):
        cleaned_data = super(UserForm, self).clean()
        password = cleaned_data.get('password')
        confirm_password = cleaned_data.get('confirm_password')

        if password != confirm_password:
            raise forms.ValidationError(#mostra uma mensagem de erro personalizada para o usuário
                "erro!!!! suas senhas não são iguais!"
            )
    
    def save(self):
        raw_password = self.cleaned_data.get('password')
        self.instance.username = self.cleaned_data.get('username')#o self.instance faz a ligação com o modelo como o objects la em template
        self.instance.set_password(raw_password)
        self.instance.save()
        return self.instance