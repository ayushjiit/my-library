from django.shortcuts import render
from .models import lib
from django.utils import timezone
from .forms import libform
from django.shortcuts import redirect
from django.shortcuts import render, get_object_or_404

# Create your views here.

#def lib_first(request):
 #   books = lib.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
  #  return render(request, 'library/lib_first.html', { 'books' : books})




def lib_first(request):
    books = lib.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'library/lib_first.html', {})






def lib_a(request):
    books = lib.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'library/lib_list1.html', { 'books' : books })


def lib_b(request):
    books = lib.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'library/lib_list2.html', { 'books' : books })


def lib_c(request):
    books = lib.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'library/lib_list3.html', { 'books' : books })


def lib_d(request):
    books = lib.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'library/lib_list4.html', { 'books' : books })



def lib_e(request):
    books = lib.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'library/lib_list5.html', { 'books' : books })





def lib_new(request):
    if request.method == "POST":
        form = libform(request.POST)
        if form.is_valid():
            lib = form.save(commit=False)
            lib.author = request.user
            lib.published_date = timezone.now()
            lib.save()
            return render(request, 'library/lib_first.html', {})
    else:
        form = libform()
    return render(request, 'library/lib_edit.html', {'form': form})








