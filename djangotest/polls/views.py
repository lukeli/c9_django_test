#from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse

from django.views import generic

from .models import Question, Choice
from .forms import QuestionForm

'''
def index(request):
    #return HttpResponse("Hello, world. You're at the polls index.")
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    context = {'latest_ql': latest_question_list}
    return render(request, 'polls/index.html', context)
'''
class IndexView(generic.ListView):
    template_name = 'polls/index.html'
    queryset = Question.objects.order_by('-pub_date')[:5]
    #model = Question  
    #context_object_name = 'latest_ql' # for ListView, the context variable 'question_list' will be 
                                       #  provided automatically from teh model name. 
                                       #  Or 'object_list' will be avaiable always.
                                       
    

    '''
    def get_queryset(self):
        """Return the last five published questions."""
        return Question.objects.order_by('-pub_date')[:5]
    '''    


'''
def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/detail.html', {'question': question})
'''
class DetailView(generic.DetailView):
    model = Question # for DetailView, the context variable 'question' will be provided automatically from the model name.
    template_name = 'polls/detail.html'
    
    
    
'''
def results(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/results.html', {'question': question})
'''
class ResultsView(generic.DetailView):
    model = Question  # for DetailView, the context variable 'question' will be provided automatically from teh model name.
    template_name = 'polls/results.html'



def vote(request, question_id):
    p = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = p.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form.
        return render(request, 'polls/detail.html', {
            'question': p,
            'error_message': "You didn't select a choice.",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse('polls:results', args=(p.id,)))
        

def new_question (request):
    if request.method == 'POST':
        form = QuestionForm(request.POST)
        if form.is_valid():
            #get the question text from the form
            q_txt = form.cleaned_data['question_text']
            #create a new questipon
            new_question = Question(question_text = q_txt)
            #save teh question
            new_question.save()
            #return http response
            return HttpResponseRedirect (reverse ('polls:detail', args=(new_question.pk,)))
    else:
        form = QuestionForm()
    
    return render(request, 'polls/question_edit.html', {'form': form})
    
def edit_question (request, question_id):
    existing_q = get_object_or_404(Question, pk=question_id)
    if request.method == 'POST':
        form = QuestionForm(request.POST, instance = existing_q )
        if form.is_valid():
            #get the question text from the form
            q_txt = form.cleaned_data['question_text']
            #create a new questipon
            new_question = Question(question_text = q_txt)
            #save teh question
            new_question.save()
            #return http response
            return HttpResponseRedirect (reverse ('polls:detail', args=(new_question.pk,)))
    else:
        form = QuestionForm(instance =existing_q )
    
    return render(request, 'polls/question_edit.html', {'form': form})