from django.contrib import admin
from howler.models import Hoot, User, Follow


class FollowAdmin(admin.ModelAdmin):
    list_display = ["following_user", "followed_user"]


class UserAdmin(admin.ModelAdmin):
    fields = ("username", "email", "is_superuser", "is_staff", "is_active")
    # inlines = [FollowersInline]


admin.site.register(Hoot)
admin.site.register(Follow, FollowAdmin)
admin.site.register(User, UserAdmin)
