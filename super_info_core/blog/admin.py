from django.contrib import admin
from blog.models import Publication, Category, Hashtag, Contact, PublicationComment
from modeltranslation.admin import TranslationAdmin


@admin.register(Publication)
class PublicationAdmin(TranslationAdmin):
    list_display = ['id', 'title']


@admin.register(Category)
class CategoryAdmin(TranslationAdmin):
    list_display = ['id', 'title']


@admin.register(Hashtag)
class HashtagAdmin(TranslationAdmin):
    list_display = ['id', 'title']


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ['name', 'message']

    def has_add_permission(self, request):
        return False

    def has_change_permission(self, request, obj=None):
        return False


@admin.register(PublicationComment)
class PublicationCommentAdmin(admin.ModelAdmin):
    list_display = ['user_name']

