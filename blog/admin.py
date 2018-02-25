from django.contrib import admin
from .models import Post

# To add, edit and delete the posts we've just modeled, we will use Django admin.
#  import (include) the Post model defined in the models.py; To make our model visible on the admin page, register it.
admin.site.register(Post)
