from django.contrib import admin
from .models import Hoot, User, Follow


class FollowAdmin(admin.ModelAdmin):
    list_display = ["following_user", "followed_user"]
    
admin.site.register(Hoot)
admin.site.register(Follow, FollowAdmin)
admin.site.register(User)
