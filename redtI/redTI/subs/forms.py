from django import forms
from .models import Thread, Post

class CreateThreadForm(forms.ModelForm):
    class Meta:#apenas definindo o modelo e os campos para aparecerem
        model = Thread
        fields = ['title']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        field = forms.CharField()
        self.fields['post'] = field
    
    def save(self):
        post_content = self.cleaned_data['post']#cleaned data são as coisas digitadas no dicionario
        self.instance.subrediti_id = self.initial['subrediti'].id
        self.instance.autor = self.initial['autor']
        self.instance.save()
        Post.objects.create(
            content = post_content,
            autor = self.instance.autor,
            thread = self.instance
        )
        return super().save()