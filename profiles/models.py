from django.db import models
from django.contrib.auth.models import User
from itertools import chain
import random

# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    avatar = models.ImageField(upload_to='avatars', default='avatar.png')
    background = models.ImageField(upload_to='backgrounds', default='background.jpg')
    following = models.ManyToManyField(User, related_name='following', blank=True)
    bio = models.TextField(default="No bio ...")
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.user)

    # Can use these methods in template. From views.py user profiles = Profiles.objects.get(user=request.user). Then in template {{ profile }}> Then to use the methods just use {{ profile.get_my_posts }}

    def get_my_posts(self):
        # Getting all posts from author link of foreignkey. You have to add add lowercase post instead of Post like you would normally use. _set gives you all objects from model. It is default reverse relationship syntax
        return self.post_set.all()

        # Below is the reverse relationship using the related_name attribute from author
        #return self.posts.all()
    
    @property
    def numb_posts(self):
        return self.post_set.all().count()
    
    # this is a queryset
    #@property treats this method as field and you can remove the parenthesis from self.get_following() from list below
    #@property
    def get_following(self):
        return self.following.all()

    # to make into a list
    def get_following_users(self):
        # Below is list comprehension. A list comprehension works by naming the for loop and also using the same name in the for loop. The idea is suppose to be [expression for val in collection] can also add an if clause or multiple if clauses [expr for val in collection if <test1> and <test2>] can loop over more than one collection [expr for val1 in collection1 and val2 in collection2]
        following_list = [p for p in self.get_following()]
        return following_list

    def get_my_and_following_posts(self):
        # Get list of users we are following
        users = [user for user in self.get_following()]
        posts = []
        qs = None
        # Loop through the list
        for u in users:
            # Get profile of particular user
            p = Profile.objects.get(user=u)
            # Get posts of particular user
            p_posts = p.post_set.all()
            # Added it to posts list
            posts.append(p_posts)
        # Get my posts
        my_posts = self.post_set.all()
        posts.append(my_posts)
        if len(posts) > 0:
            #* is unpacking posts
            qs = sorted(chain(*posts), reverse=True, key=lambda obj: obj.created)
        return qs
    
    # Following suggestions
    def get_proposals_for_following(self):
        # Get all profiles besides our own
        profiles = Profile.objects.all().exclude(user=self.user)
        # Create a followers list
        followers_list = [p for p in self.get_following()]
        # Get all profiles that are not in followers_list
        available = [p.user for p in profiles if p.user not in followers_list]
        random.shuffle(available)
        # Return 3 proposals
        return available[:3]

    @property
    def following_count(self):
        return self.get_following().count()

    def get_followers(self):
        # Get all profiles
        qs = Profile.objects.all()
        # Create followers list
        followers_list = []
        # For loop qs
        for profile in qs:
            # Checking to see if we are in profile following list
            if self.user in profile.get_following():
                # add profile to followers_list
                followers_list.append(profile)
        return followers_list

    @property
    def followers_count(self):
        return len(self.get_followers())