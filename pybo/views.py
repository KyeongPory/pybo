from django.shortcuts import render,get_object_or_404,redirect,HttpResponse
from .models import Question,Answer
from django.utils import timezone

# Create your views here.
def index(request):
    question_list = Question.objects.order_by('-create_date')
    total_count = Question.objects.count()
    context = {
        'question_list' : question_list,
        'total_count':total_count
    }
    return render(request, 'pybo/question_list.html',context)

def detail(request,question_id):
    #question = Question.objects.get(id=question_id)
    question = get_object_or_404(Question, pk=question_id)
    context = {'question' : question}
    return render(request, 'pybo/question_detail.html',context)

def answer_create(request,question_id):
    question = get_object_or_404(Question, pk=question_id)
    content = request.POST.get('content')
    
    #Answer 생성이 목적
    #방법1
    '''answer = Answer(question = question, 
                    content = content,
                    create_date = timezone.now())
    answer.save()'''

    #방법2 ForeignKey 관계인 경우
    question.answer_set.create(content = content,
                    create_date = timezone.now())

    return redirect('pybo:detail', question_id=question.id)
