# Generated by Django 2.0 on 2019-01-18 12:57

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('subs', '0002_auto_20190117_1414'),
    ]

    operations = [
        migrations.CreateModel(
            name='LikePost',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('valor', models.CharField(max_length=10)),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='likepost', to='subs.Post')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='likepost', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='LikeThread',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('valor', models.CharField(max_length=10)),
                ('thread', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='likethread', to='subs.Thread')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='likethread', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AlterUniqueTogether(
            name='likethread',
            unique_together={('thread', 'user')},
        ),
        migrations.AlterUniqueTogether(
            name='likepost',
            unique_together={('post', 'user')},
        ),
    ]
