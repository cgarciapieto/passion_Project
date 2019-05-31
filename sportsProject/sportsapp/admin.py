
from django.contrib import admin

from .models import UserModel
from .models import PostModel
from .models import News

admin.site.register(UserModel)
admin.site.register(PostModel)
admin.site.register(News)