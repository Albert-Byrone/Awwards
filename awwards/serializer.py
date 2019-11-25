from rest_framework  import serializers
from django.contrib.auth.models import User
from .models import Post,Profile


class ProfileSerializer(serializers.ModelSerializer):
    model = Profile
    fields = ['name','prof_picture','bio','location','contact']


