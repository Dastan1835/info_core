from django.http import HttpResponse
from django.core.paginator import Paginator
from django.shortcuts import render
from django.views import View
from django.views.generic import TemplateView
from django.shortcuts import redirect
from blog.telegram_bot import bot
from blog.models import Publication, Hashtag, Category, PublicationComment, Contact
from django.db.models import Q


# Create your views here.
class HomeView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        publications = Publication.objects.filter(is_active=True)
        paginator = Paginator(publications, 2)
        page_number = self.request.GET.get('page')
        page_obj = paginator.get_page(page_number)

        context = {
            'page_obj': page_obj
        }
        return context


class HomeSearchView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        search_word = self.request.GET['query']
        context = {
            'page_obj': Publication.objects.filter(
                Q(title__icontains=search_word) | Q(description__icontains=search_word) & Q(is_active=True)
            )
        }
        return context


class ContactView(TemplateView):
    template_name = 'contact.html'


def client_contact_view(request):
    input_name = request.POST['name']
    input_email = request.POST['email']
    input_subject = request.POST['subject']
    input_message = request.POST['message']
    Contact.objects.create(name=input_name, email=input_email, subject=input_subject, message=input_message)
    return HttpResponse("<h1>Ваше сообщение было создана </h1>")


class PublicationDetailView(TemplateView):
    template_name = 'publication-detail.html'

    def get_context_data(self, **kwargs):
        publication_pk = kwargs['pk']
        post = Publication.objects.get(id=publication_pk)
        hashtags = post.hashtags.all()
        related_posts = Publication.objects.filter(hashtags__in=hashtags).exclude(id=publication_pk).distinct()


        context = {
            "publication": post,
            'category_list': Category.objects.all(),
            'related_post_list': related_posts,
        }
        return context


class CreatePublicationCommentView(View):
    def post(self, request, *args, **kwargs):
        publication_pk = kwargs['pk']
        publication = Publication.objects.get(id=publication_pk)

        comment_text = request.POST['message']
        comment_name = request.POST['name']

        PublicationComment.objects.create(publication=publication, text=comment_text, user_name=comment_name)
        bot.send_message(chat_id=5278555399, text="для вашей публикация написали коментарии ")

        return redirect('publication-detail', pk=publication_pk)



