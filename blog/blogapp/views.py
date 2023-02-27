from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin, AccessMixin
from django.shortcuts import render, get_object_or_404, HttpResponseRedirect, redirect
from django.urls import reverse, reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView,TemplateView
from .models import Post, Tag, Category
from .forms import ContactForm, PostForm, PostCategoryForm
from django.core.mail import send_mail
from django.views.generic.base import ContextMixin
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


# Create your views here.

def main_view(request):
    # posts = Post.objects.all()
    # posts = Post.objects.filter(is_active=True)
    # для оптимизации
    posts = Post.active_objects.select_related('category','user').all()
    paginator = Paginator(posts, 5)
    page = request.GET.get('page')
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)
    title = 'главная'
    return render(request, 'blogapp/index.html', context={'posts': posts, 'title': title})


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


# Может читать только админ
@user_passes_test(lambda u: u.is_superuser)
def post(request, id):
    post = get_object_or_404(Post, id=id)
    all_tags = post.get_all_tags
    for item in all_tags:
        print(item)
    return render(request, 'blogapp/post.html', context={'post': post})


@login_required
def create_post(request):
    if request.method == 'GET':
        form = PostForm()
        return render(request, 'blogapp/create.html', context={'form': form})
    else:
        form = PostForm(request.POST, files=request.FILES)
        if form.is_valid():
            # добавить в форму текущего пользователя, request user -ткущий польщователь
            form.instance.user = request.user
            form.save()
            return HttpResponseRedirect(reverse('blog:main'))
        else:
            return render(request, 'blogapp/create.html', context={'form': form})


class NameContextMixin(ContextMixin):
    def get_context_data(self, *args, **kwargs):
        """
        отвечает за передачу параметров в контекст
        :param args:
        :param kwargs:
        :return:
        """
        context = super().get_context_data(*args, **kwargs)
        context['name'] = 'Теги'
        return context


# CRUD

# список тегов
class TagListView(ListView, NameContextMixin):
    model = Tag
    template_name = 'blogapp/tag_list.html'
    paginate_by = 2

    def get_queryset(self):
        """
        Получение данных
        """
        return Tag.active_objects.all()

    # если мы хотим чтобы в шаблоне было не objects:
    # context_object_name = 'tags'


# детальная инфа
# UserPassesTestMixin
class TagDetailView(UserPassesTestMixin, AccessMixin, DetailView, NameContextMixin):
    model = Tag
    template_name = 'blogapp/detail_tag.html'

    def test_func(self):
        return self.request.user.is_superuser

    # Это крч со свезкой с test_func, чтобы он не выкидывал 403 ошибку, а перенаправлял
    def handle_no_permission(self):
        return HttpResponseRedirect(reverse('userapp:login'))

    def get_queryset(self):
        """
        Получение данных
        :return:
        """
        pass

    def get_object(self, queryset=None):
        """
        Получает один объект
        :param queryset:
        :return:
        """
        return get_object_or_404(Tag, pk=self.tag_id)

    def get(self, request, *args, **kwargs):
        """
        Метод обработки гет запроса
        :param request:
        :param args:
        :param kwargs:
        :return:
        """
        self.tag_id = kwargs['pk']
        return super().get(request, *args, **kwargs)


# создание тега
# Важно LoginRequiredMixin -должен идти первым
class TagCreateView(LoginRequiredMixin, CreateView, NameContextMixin):
    # form_class=
    fields = '__all__'
    model = Tag
    success_url = reverse_lazy('blog:tag_list')
    template_name = 'blogapp/tag_create.html'

    def post(self, request, *args, **kwargs):
        """
        когда пришел пост запрос
        :param request:
        :param args:
        :param kwargs:
        :return:
        """
        return super().post(request, *args, **kwargs)

    def form_valid(self, form):
        """
        метод срабатывает после того как форма валидна
        :param form:
        :return:
        """
        # это если нужно в классах связать с другой моделью
        # form.instance.user = self.request.user
        return super().form_valid(form)


class UpdateTagView(UpdateView):
    fields = '__all__'
    model = Tag
    success_url = reverse_lazy('blog:tag_list')
    template_name = 'blogapp/tag_create.html'


class DeleteTagView(DeleteView):
    template_name = 'blogapp/tag_delete_confirm.html'
    model = Tag
    success_url = reverse_lazy('blog:tag_list')


class CategoryDetailView(DeleteView):
    template_name = 'blogapp/category_detail.html'
    model = Category

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = PostCategoryForm()
        return context


class PostCategoryCreateView(CreateView):
    model = Post
    template_name = 'blogapp/category_detail.html'
    # success_url = reverse_lazy
    form_class = PostCategoryForm

    def post(self, request, *args, **kwargs):
        self.category_pk = kwargs['pk']
        return super().post(request, *args, **kwargs)

    def form_valid(self, form):
        user = self.request.user
        form.instance.user = user
        category = get_object_or_404(Category, pk=self.category_pk)
        form.instance.category = category
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('blogapp:detail_category', kwargs={'pk': self.category_pk})

class SimpleMainAjax(TemplateView):
    template_name = 'blogapp/simple.html'
