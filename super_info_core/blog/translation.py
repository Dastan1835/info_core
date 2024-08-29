from modeltranslation.translator import register, TranslationOptions

from blog.models import Category, Hashtag, Publication


@register(Category)
class CategoryTranslationOptions(TranslationOptions):
    fields = ('title', )


@register(Hashtag)
class HashtagTranslationOptions(TranslationOptions):
    fields = ('title',)


@register(Publication)
class PublicationTranslationOptions(TranslationOptions):
    fields = ('title', 'shorts_description', 'description',)
