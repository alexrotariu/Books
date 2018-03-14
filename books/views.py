from django.shortcuts import render, HttpResponse
from django.core.urlresolvers import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, TemplateView, DeleteView, UpdateView
from .models import Book
from .forms import BookForm


class BookList(ListView):
    model = Book
    template_name = 'books/book-list.html'
    context_object_name = 'books'
    paginate_by = 5


class BookListByAuthor(ListView):
    model = Book
    template_name = 'books/book-list_by_author.html'
    context_object_name = 'books'
    paginate_by = 5

    def get_queryset(self, author_slug):
        return Book.objects.filter(author_slug=author_slug)


def book_list_by_author(request, author_slug):
    books = Book.objects.filter(author_slug=author_slug)
    author = books[0].author

    return render(
        request,
        'books/book_list_by_author.html',
        context={'books': books, 'author': author}
    )


class BookDetail(DetailView):
    model = Book
    template_name = 'books/book-detail.html'


class BookAdd(CreateView):
    model = Book
    template_name = 'books/book-add.html'
    form_class = BookForm
    success_url = '/books/add/thanks'


class BookAddThanks(TemplateView):
    template_name = 'books/book-add-thanks.html'


class BookDelete(DeleteView):
    model = Book
    success_url = reverse_lazy('books:books')


class BookEdit(UpdateView):
    model = Book
    template_name = 'books/book-add.html'
    form_class = BookForm
    success_url = reverse_lazy('books:books')


def about(request):
    return render(request, 'books/about.html')