from django.urls import path
from .views import index,detail

app_name = 'pybo'

urlpatterns = [
    path('', index,name='index'),
    path('<int:question_id>/',detail,name='detail'),

]
