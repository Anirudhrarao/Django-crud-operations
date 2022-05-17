from django.http import HttpResponse
from django.shortcuts import redirect, render
from .models import Book
from .forms import BookForm
# Create your views here.

def index(request):
    book = Book.objects.all()
    return render(request,'library.html',{'book':book})

def upload(request):
    upload = BookForm()
    if request.method == 'POST':
        upload = BookForm(request.POST,request.FILES)
        if upload.is_valid():
            upload.save()
            return redirect(index)
        else:
            return HttpResponse('Something wrong with your form')
    return render(request,'upload.html',{'upload':upload})

def update(request,book_id):
    book_id = int(book_id)
    try:
        book = Book.objects.get(id=book_id)
    except Book.DoesNotExist:
        return redirect(index)
    upd_form = BookForm(request.POST or None,instance=book)
    if upd_form.is_valid():
        upd_form.save()
        return redirect(index)
    return render(request,'upload.html',{'upload':upd_form})
def delete(request,book_id):
    book_id = int(book_id)
    try:
        book = Book.objects.get(id=book_id)
    except Book.DoesNotExist:
        return redirect(index)
    book.delete()
    return redirect(index)