from django.http import HttpResponse
from django.shortcuts import render
from django.views import View
from django.views.generic import TemplateView
from django.shortcuts import redirect
from blog.models import Publication, Hashtag, Category, PublicationComment, Contact


# Create your views here.
class HomeView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = {
            'publication_list': Publication.objects.all(),
            'hashtags': Hashtag.objects.all()
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
        context = {
            "publication": Publication.objects.get(id=publication_pk),
            'hashtags': Hashtag.objects.all(),
            'category_list': Category.objects.all()
        }
        return context


class CreatePublicationCommentView(View):
    def post(self, request, *args, **kwargs):
        publication_pk = kwargs['pk']
        publication = Publication.objects.get(id=publication_pk)

        comment_text = request.POST['message']
        comment_name = request.POST['name']

        PublicationComment.objects.create(publication=publication, text=comment_text, user_name=comment_name)

        return redirect('publication-detail', pk=publication_pk)



