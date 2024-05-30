from django.shortcuts import get_object_or_404
from django.http import HttpResponse
from datetime import datetime
from . import forms, models
from django.views import generic


class CreateReviewView(generic.CreateView):
    template_name = "create_review.html"
    form_class = forms.ReviewForm
    success_url = "/books/"

    def form_valid(self, form):
        print(form.cleaned_data)
        return super(CreateReviewView, self).form_valid(form=form)


class EditBookView(generic.UpdateView):
    template_name = "edit.html"
    form_class = forms.BookForm
    success_url = "/books/"

    def get_object(self, **kwargs):
        book_id = self.kwargs.get("id")
        return get_object_or_404(models.AddBooks, id=book_id)

    def form_valid(self, form):
        print(form.cleaned_data)
        return super(EditBookView, self).form_valid(form=form)


class DeleteBookView(generic.DeleteView):
    template_name = "confirm_delete.html"
    success_url = "/books/"

    def get_object(self, **kwargs):
        book_id = self.kwargs.get("id")
        return get_object_or_404(models.AddBooks, id=book_id)


class CreateBookView(generic.CreateView):
    template_name = "create_book.html"
    form_class = forms.BookForm
    success_url = "/books/"

    def form_valid(self, form):
        print(form.cleaned_data)
        return super(CreateBookView, self).form_valid(form=form)


class AddBookView(generic.ListView):
    template_name = "books.html"
    context_object_name = "book"
    model = models.AddBooks

    def get_queryset(self):
        return self.model.objects.all().order_by("-id")


class BooksDetailView(generic.DetailView):
    template_name = "books_detail.html"
    context_object_name = "books_id"

    def get_object(self, **kwargs):
        books_id = self.kwargs.get("id")
        return get_object_or_404(models.AddBooks, id=books_id)


class SearchBookView(generic.ListView):
    template_name = "books.html"
    context_object_name = "book"
    paginate_by = 5

    def get_queryset(self):
        return models.AddBooks.objects.filter(
            title__icontains=self.request.GET.get("q")
        )

    def get_context_data(self, *, object_list=None, **kwargs):
        contex = super().get_context_data(**kwargs)
        contex["q"] = self.request.GET.get("q")
        return contex


def bio_view(request):
    if request.method == "GET":
        return HttpResponse("Я Данил Тен, мне 19 лет")


def hobby_view(request):
    if request.method == "GET":
        return HttpResponse("Моё хобби это спать")


def current_time_view(request):
    if request.method == "GET":
        current_time = datetime.now().time()
        return HttpResponse(current_time)
