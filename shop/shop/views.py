from django import forms
from django.http import Http404, HttpResponse
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.template import loader
from django.urls import reverse
from django.views import View
from django.views import generic

from shop.models import Category, Item


def xxx(request):
    return HttpResponse('html')


class CategoryList(generic.ListView):
    model = Category
    context_object_name = 'categories'

    # def get_queryset(self):
    #     return Category.objects.order_by('title')


class CategoryView(generic.DetailView):
    model = Category
    # template_name = 'shop/category_detail.html'


def add_item(request, category_id):
    try:
        category = Category.objects.get(pk=category_id)
    except Category.DoesNotExist:
        raise Http404("Question does not exist")

    form = NewItemForm(request.POST)
    if form.is_valid():
        category.item_set.create(title=request.POST['title'], price=request.POST['price'])

        return HttpResponseRedirect(reverse('shop:category', category_id))

    context = {
        'category': category,
        'form': form
    }

    return render(request, 'shop/category_detail.html', context)


class NewItemForm(forms.Form):
    title = forms.CharField(label='Title', max_length=100)
    price = forms.DecimalField(label='Price', max_digits=15, decimal_places=2)


from django.forms import ModelForm
from shop.models import Item

class ItemForm(ModelForm):
    class Meta:
        model = Item
        fields = ['title', 'price', 'category']

class ItemFormView(View):
    template_name = 'shop/item_detail.html'

    def get(self, request, pk, *args, **kwargs):
        item = Item.objects.get(pk=pk)
        form = ItemForm(instance=item)
        return render(request, self.template_name, {'form': form, 'item': item})

    def post(self, request, pk, *args, **kwargs):
        item = Item.objects.get(pk=pk)
        form = ItemForm(request.POST)
        if form.is_valid():
            item.title = form.instance.title
            item.price = form.instance.price
            item.category = form.instance.category
            item.save()
        return render(request, self.template_name, {'form': form, 'item': item})
