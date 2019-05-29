
from django.contrib import admin

from .models import UserModel
from .models import PostModel

admin.site.register(UserModel)
admin.site.register(PostModel)