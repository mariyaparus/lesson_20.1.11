from django.shortcuts import render
from django.urls import reverse_lazy, reverse
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, TemplateView

from dogs.models import Category, Dog


# Create your views here.

class IndexView(TemplateView):
    template_name = 'dogs/index.html'
    extra_context = {
        'title': 'Питомник - Главная',
    }

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        context_data['object_list'] = Category.objects.all()[:3]
        return context_data


# def index(request):
#     categories_list = Category.objects.all()
#     context = {
#         'object_list': categories_list[:3],
#         'title': 'Питомник - Главная'
#     }
#     return render(request, 'dogs/index.html', context)


# def categories(request):
#     categories_list = Category.objects.all()
#     context = {
#         'object_list': categories_list,
#         'title': 'Питомник - Все наши породы'
#     }
#     return render(request, 'dogs/categories.html', context)


class CategoryListView(ListView):
    model = Category
    extra_context = {
        'title': 'Питомник - Все наши породы'
    }

    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     context.update({'title': 'Питомник - Все наши породы'})
    #     return context


# def category_dogs(request, pk):
#     category_item = Category.objects.get(pk=pk)
#     categories_list = Dog.objects.filter(category_id=pk)
#     context = {
#         'object_list': categories_list,
#         'title': f'Собаки породы - {category_item}'
#     }
#     return render(request, 'dogs/dogs.html', context)


class DogListView(ListView):
    model = Dog

    def get_queryset(self):
        """
        Выводить только опубликованные материалы
        """
        queryset = super().get_queryset()
        queryset = queryset.filter(category_id=self.kwargs.get('pk'))
        return queryset

    def get_context_data(self, *args, **kwargs):
        context_data = super().get_context_data(*args, **kwargs)

        category_item = Category.objects.get(pk=self.kwargs.get('pk'))
        context_data['category_pk'] = category_item.pk,
        context_data['title'] = f'Собаки породы - {category_item.name}'

        return context_data


class DogCreateView(CreateView):
    model = Dog
    fields = ('name', 'category',)
    success_url = reverse_lazy('dogs:categories')


class DogUpdateView(UpdateView):
    model = Dog
    fields = ('name', 'category',)

    def get_success_url(self):
        return reverse('dogs:category_dogs', args=[self.object.category.pk])


class DogDeleteView(DeleteView):
    model = Dog
    success_url = reverse_lazy('dogs:categories')
