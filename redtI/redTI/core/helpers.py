from subs.models import Post, Thread
from .models import LikePost, LikeThread
from users.helpers import update_user_karma
def return_thread_or_post(target_type, target_id):
    if target_type == 'post':
        return Post.objects.get(id=target_id)
    if target_type == 'thread':
        return Thread.objects.get(id=target_id)

def return_votethread_or_votepost(target_type, target, user):
    if target_type == 'post':
        return LikePost.objects.get_or_create(post=target, user=user)
    if target_type == 'thread':
        return LikeThread.objects.get_or_create(thread=target, user=user)

def modify_vote_count(vote, target):
    if vote.valor == 1:#já votou, perceba que aki temos apenas curtir ou ncurtir(neutro), n existe dislike propriamente dito
        vote.valor = 0
        vote.save()
        target.vote_count -= 1
        target.save()
        return
    vote.valor = 1
    vote.save()
    target.vote_count += 1
    target.save()
    return

def modify_karma(target_type, target_id, user):
    target = return_thread_or_post(target_type, target_id)
    vote, created = return_votethread_or_votepost(target_type, target, user)
    modify_vote_count(vote, target)
    update_user_karma(target.autor)
