from django.shortcuts import render, get_object_or_404, HttpResponseRedirect
from django.urls import reverse, reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Post, Tag
from .forms import ContactForm, PostForm
from django.core.mail import send_mail


# Create your views here.

def main_view(request):
    posts = Post.objects.all()
    return render(request, 'blogapp/index.html', context={'posts': posts})


def contact_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            #     Получить данные из формы
            name = form.cleaned_data['name']
            message = form.cleaned_data['message']
            email = form.cleaned_data['email']
            send_mail(
                'Тест из питона',
                message,
                'kiryamiass7@gmail.com',
                [email],
                fail_silently=True,
            )
            return HttpResponseRedirect(reverse('blog:main'))
        else:
            return render(request, 'blogapp/contact.html', context={'form': form})
    else:
        form = ContactForm()
        return render(request, 'blogapp/contact.html', context={'form': form})


def post(request, id):
    post = get_object_or_404(Post, id=id)
    return render(request, 'blogapp/post.html', context={'post': post})


def create_post(request):
    if request.method == 'GET':
        form = PostForm()
        return render(request, 'blogapp/create.html', context={'form': form})
    else:
        form = PostForm(request.POST, files=request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('blog:main'))
        else:
            return render(request, 'blogapp/create.html', context={'form': form})


# CRUD

# список тегов
class TagListView(ListView):
    model = Tag
    template_name = 'blogapp/tag_list.html'


# детальная инфа
class TagDetailView(DetailView):
    model = Tag
    template_name = 'blogapp/detail_tag.html'


# создание тега
class TagCreateView(CreateView):
    # form_class=
    fields = '__all__'
    model = Tag
    success_url = reverse_lazy('blog:tag_list')
    template_name = 'blogapp/tag_create.html'


class UpdateTagView(UpdateView):
    fields = '__all__'
    model = Tag
    success_url = reverse_lazy('blog:tag_list')
    template_name = 'blogapp/tag_create.html'


class DeleteTagView(DeleteView):
    template_name = 'blogapp/tag_delete_confirm.html'
    model = Tag
    success_url = reverse_lazy('blog:tag_list')
