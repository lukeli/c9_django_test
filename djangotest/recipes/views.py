from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse

from django.views import generic


from .forms import IngredientFormSet, InstructionFormSet, RecipeForm
from .models import Recipe, Ingredient, Instruction

class IndexView(generic.ListView):
    template_name = 'recipes/index.html'
    queryset = Recipe.objects.all()

class DetailView(generic.DetailView):
    model = Recipe
    template_name = 'recipes/detail.html'
    
    
def CreateRecipe(request):    
    if request.method == 'POST':
        
        recipe_form = RecipeForm(request.POST)
        recipe_form.save()
        
        ingredient_formset = IngredientFormSet(request.POST,  instance = recipe_form.instance,  prefix = 'ingredient')
        instruction_formset = InstructionFormSet(request.POST, instance = recipe_form.instance, prefix = 'instruction')
        if ingredient_formset.is_valid()  and instruction_formset.is_valid()  :
            ingredient_formset.save()
            instruction_formset.save() 
            
        return HttpResponseRedirect (reverse ('recipes:index'))
    else:
        recipe_form = RecipeForm()
        #recipe_form.save()
        
        ingredient_formset = IngredientFormSet(instance = recipe_form.instance,  prefix = 'ingredient')
        instruction_formset = InstructionFormSet(instance = recipe_form.instance, prefix = 'instruction')
    
    context = {'recipe_form': recipe_form,  'ingredient_formset': ingredient_formset, 'instruction_formset': instruction_formset  }
        
    return render (request, 'recipes/recipe_add.html',  context )                                       
 
 