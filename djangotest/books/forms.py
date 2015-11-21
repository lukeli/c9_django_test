from django.forms import ModelForm
from django.forms import modelformset_factory
from django.forms import formset_factory
from django.forms import inlineformset_factory

from .models import Author, Book

class AuthorForm(ModelForm):
    class Meta:
        model = Author
        fields = ['name']

class BookForm(ModelForm):
    class Meta:
        model = Book
        fields = ['title', 'author']

# if the formset is generatedd from the modelformset_factory you can usue save()
# if the formset is generatedd from the formset_factory you can not usue save() -- no such method error        
#AuthorFormSet =  formset_factory(AuthorForm, extra=3)   
AuthorFormSet =  modelformset_factory(Author, fields =['name'], extra=3) 

BookInlineFormSet = inlineformset_factory(Author, Book, fields = ('title',))