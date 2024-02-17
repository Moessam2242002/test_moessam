from django.shortcuts import render,redirect,get_object_or_404
from .models import *
from .form  import *
from django.db.models import Sum
# Create your views here.
def indedx(request):
    context={
        "books":Books.objects.all(),
        'form':update_book(),
        'category':Category.objects.all(),
        'formcat':CtegoryForm(),
        "status": Books.objects.values_list('status', flat=True).distinct(),
        "allbooks":Books.objects.filter(active=True).count(),
        'rentalbooks':Books.objects.filter(status='rental').count(),
        'soldbooks':Books.objects.filter(status='sold').count(),
        'availablebooks':Books.objects.filter(status='available').count(),
        'sold_price':(Books.objects.filter(status= 'sold').aggregate(Sum('price'))),
        'rental_html':(Books.objects.filter(status= 'rental').aggregate(Sum('total_rental'))),
    }
    # if request.method=="POST":
    if request.method=="POST":  
        data=update_book(request.POST,request.FILES)
        if data.is_valid():
            data.save()
            return redirect("/")
        cat_data=CtegoryForm(request.POST)
        if cat_data.is_valid():
            cat_data.save()
            return redirect("/")
    return render(request,'pages/index.html',context)
def books(request):
    title=None
    search=Books.objects.all()
    if 'search_name' in request.GET:
        word=request.GET['search_name']
        if word:
            search=search.filter(book_name__icontains=word)
            
    context={
        "books":search,
        'categories':Category.objects.all(),
        'category':Category.objects.all(),
        'formcat':CtegoryForm(),
        "status": Books.objects.values_list('status', flat=True).distinct(),
    }
    return render(request,'pages/books.html',context)
def delete(request,id):
    book_id=Books.objects.get(id=id)
    if request.method=='POST':
        book_id.delete()
        return redirect('/')
    return render(request,'pages/delete.html')
def update(request,id):
    book_id=Books.objects.get(id=id)
    if request.method=="POST":
        book_save=update_book(request.POST,request.FILES,instance=book_id)
        if book_save.is_valid():
            book_save.save()
            return redirect('/')
    else:
        book_save=update_book(instance=book_id)
    context={'book':book_save,}
    return render(request,'pages/update.html',context)
