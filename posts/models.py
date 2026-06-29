from django.db import models
from django.contrib.auth.models import User



class Profile(models.Model):

    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE
    )

    bio = models.TextField(
        blank=True
    )

    profile_pic = models.ImageField(
        upload_to='profile_pics/',
        blank=True,
        null=True
    )


    def __str__(self):
        return self.user.username





class Post(models.Model):

    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE
    )

    content = models.TextField()


    image = models.ImageField(
        upload_to='post_images/',
        blank=True,
        null=True
    )


    created_at = models.DateTimeField(
        auto_now_add=True
    )


    def __str__(self):
        return self.content





class Like(models.Model):

    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE
    )


    post = models.ForeignKey(
        Post,
        on_delete=models.CASCADE
    )





class Comment(models.Model):

    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE
    )


    post = models.ForeignKey(
        Post,
        on_delete=models.CASCADE
    )


    text = models.TextField()


    created_at = models.DateTimeField(
        auto_now_add=True
    )


    def __str__(self):
        return self.text





class Follow(models.Model):

    follower = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="following"
    )


    following = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="followers"
    )


    def __str__(self):
        return f"{self.follower} follows {self.following}"