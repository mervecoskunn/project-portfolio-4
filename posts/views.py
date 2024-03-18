from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.views import generic
from posts import models, forms
from django.urls import reverse


class PostCreateView(generic.CreateView):
    model = models.Post
    form_class = forms.PostCreateForm
    template_name = 'posts/post_create.html'

    def get_success_url(self):
        return reverse('posts:user_page', args=[self.request.user.id])

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def post(self, request, *args, **kwargs):
        return super().post(request, *args, **kwargs)


class PostDetailView(generic.DetailView):
    model = models.Post
    template_name = 'posts/post_detail.html'

    def get(self, request, *args, **kwargs):
        liked = self.get_object().like.filter(id=self.request.user.id).exists()
        context = {
            'object': self.get_object(),
            'liked': liked,
            'comment_form': forms.CommentCreateForm
        }
        return render(request, 'posts/post_detail.html', context=context)


class PostListView(generic.ListView):
    model = models.Post
    queryset = models.Post.objects.filter(is_approved=True)
    template_name = 'posts/post_list.html'
    paginate_by = 6

    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)


class PostEditView(generic.UpdateView):
    model = models.Post
    form_class = forms.PostEditForm
    template_name = 'posts/post_edit.html'

    def get_success_url(self):
        return reverse('posts:manage_posts', args=[self.request.user.id])

    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return super().post(request, *args, **kwargs)


class PostDeleteView(generic.DeleteView):
    model = models.Post
    template_name = 'posts/post_delete.html'

    def get_success_url(self):
        return reverse('posts:manage_posts', args=[self.request.user.id])

    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return super().post(request, *args, **kwargs)


class CommentCreateView(generic.CreateView):
    model = models.Comment
    form_class = forms.CommentCreateForm
    template_name = 'posts/post_detail.html'

    def get_success_url(self):
        return reverse('posts:post_detail', args=[self.kwargs.get('post_id')])

    def form_valid(self, form):
        form.instance.author = self.request.user
        form.instance.post_id = self.kwargs.get('post_id')
        return super().form_valid(form)

    def post(self, request, *args, **kwargs):
        return super().post(request, *args, **kwargs)


class CategoryListView(generic.ListView):
    model = models.Category
    queryset = models.Category.objects.all()
    template_name = 'categories/category_list.html'
    paginate_by = 6

    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)


class CategoryDetailView(generic.DetailView):
    model = models.Category
    template_name = 'categories/category_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

    def get(self, request, *args, **kwargs):
        posts = models.Post.objects.filter(is_approved=True,
                                           category__id=kwargs.get('pk'))
        context = {
            'object': self.get_object(),
            'posts': posts
        }
        return render(request, 'categories/category_detail.html', context)


class UserPageView(generic.TemplateView):
    template_name = 'posts/user_page.html'


class ManagePostView(generic.ListView):
    model = models.Post
    template_name = 'posts/manage_posts.html'
    paginate_by = 6

    def get_queryset(self):
        user = self.request.user
        return models.Post.objects.filter(author=user)

    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)


class PostLike(generic.DetailView):

    def post(self, request, *args, **kwargs):
        post = get_object_or_404(models.Post, pk=kwargs.get('post_id'))
        if post.like.filter(id=request.user.id).exists():
            post.like.remove(request.user)
        else:
            post.like.add(request.user)
        return HttpResponseRedirect(
            reverse('posts:post_detail', 
                args=[kwargs.get('post_id')]))


def category_on_all_pages(request):
    return {'categories': models.Category.objects.all()}
