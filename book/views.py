from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from . import models, forms


def book_list_view(request):
    books = models.Book.objects.all()
    return render(request, 'book_list.html', context={'book': books})


def books_detail_view(request, id):
    book = get_object_or_404(models.Book, id=id)
    return render(request, 'book_detail.html',
                  {'book': book})


def add_book(request):
    method = request.method
    if method == 'POST':
        form = forms.BookForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponse('Book created')
    else:
        form = forms.BookForm()
    return render(request, 'add_book.html', {'form': form})


def book_update(request, id):
    book_object = get_object_or_404(models.Book, id=id)
    if request.method == 'POST':
        form = forms.BookForm(instance=book_object, data=request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse('Book Updated Successfully')
            # return redirect(reverse('shows:show_all'))
    else:
        form = forms.BookForm(instance=book_object)
    return render(request, 'show_update.html', {'form': form, 'object': book_object})


def book_delete(request, id):
    book_object = get_object_or_404(models.Book, id=id)
    book_object.delete()
    return HttpResponse('Book Deleted')
