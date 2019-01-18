from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.core.validators import MaxValueValidator, MinValueValidator
# Create your models here.

class IndexedTimeStampedModel(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

class VoteAbstractModel(models.Model):
    user = models.ForeignKey('users.User', on_delete=models.CASCADE, blank=False, null=False)
    valor = models.IntegerField(default=0, validators=[
        MaxValueValidator(1),#like
        MinValueValidator(0)#dislike
    ])

    class Meta:
        abstract = True

class LikePost(VoteAbstractModel):
    post = models.ForeignKey('subs.Post', related_name='likeposts', on_delete=models.CASCADE, blank=False, null=False)
    class Meta:
        unique_together = [('post', 'user')]

    def __str__(self):
        return str(self.user.username) + ':' + str(self.post) +':' + str(self.valor)


class LikeThread(VoteAbstractModel):
    thread = models.ForeignKey('subs.Thread', related_name='likethreads', on_delete=models.CASCADE, blank=False, null=False)

    class Meta:
        unique_together = [('thread', 'user')]

    def __str__(self):
        return str(self.user.username) + ':' + str(self.thread.title) +':' + str(self.valor)
