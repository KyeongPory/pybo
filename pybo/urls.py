from django.urls import path
from .views import index,detail,answer_create

app_name = 'pybo'

urlpatterns = [
    path('', index,name='index'),
    path('<int:question_id>/',detail,name='detail'),
    path('answer/create/<int:question_id>/',answer_create, name='answer_create'),
]
