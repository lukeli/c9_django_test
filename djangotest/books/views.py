from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse

from django.views.generic.edit import CreateView
from django.views import generic

from .forms import BookForm, BookInlineFormSet , AuthorForm, AuthorFormSet
from .models import Author, Book

class IndexView(generic.ListView):
    template_name = 'books/index.html'
    queryset = Author.objects.all()
   
def manage_author(request):
    if request.method == 'POST':
        formset = AuthorFormSet(request.POST, request.FILES )
        if formset.is_valid():
            # if the formset is generatedd from the modelformset_factory you can usue save()
            # if the formset is generatedd from the formset_factory you can not usue save() -- no such method error
            formset.save()
            # do something with the formset.cleaned_data
            # new_auths = []
            # for author_form in formset:
            #     if author_form.is_valid() and author_form.cleaned_data.get('name') :
            #         auth_nm = author_form.cleaned_data['name']
            #         #create a new questipon
            #         new_author = Author(name=auth_nm)
            #         #new_author.save()
            #         new_auths.append(new_author)
            
            # Author.objects.bulk_create(new_auths)
            return HttpResponseRedirect (reverse ('books:index'))
    else:
        formset = AuthorFormSet()
        
    return render (request, 'books/manage_author.html', {'formset': formset})                                       
 
 
def manage_books(request, author_id):
    
    author = Author.objects.get(pk=author_id)
    authorform =AuthorForm(instance = author)
    
    if request.method == 'POST':
        
        bookformset = BookInlineFormSet(request.POST, request.FILES, instance = author )
        
        if bookformset.is_valid():
            bookformset.save()
           
            return HttpResponseRedirect (reverse ('books:index'))
    else:
        bookformset = BookInlineFormSet(instance = author )
 
    context ={'bookformset': bookformset, 'authorform': authorform  }     
    return render (request, 'books/manage_books.html', context)                                       
 
                                       
                                       
def add_user_book(request, author_id):
     author = Author.objects.get(pk=author_id)
     if request.method == "POST":
         formset =  BookInlineFormSet  (request.POST, request.FILES, instance = author)
         if formset.is_valid():
             formset.save()
             return HttpResponseRedirect (reverse ('books:index'))
         else:
             formset = BookInlineFormSet (instance=author)
         
         context ={'bookformset': bookformset, 'authorform': authorform  }   
         return render(request, 'books/add_user_book.html', context)