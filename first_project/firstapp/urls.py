from django.urls import path
from . import views

app_name = 'firstapp'

urlpatterns = [
    path('hello', views.index, name='index'), #ここでどのviewを表示させるかを決める。
    path('page/<str:user_name>', views.user_page, name='user_page'),
    path('numberpage/<str:user_name>/<int:number>', views.number_page, name='number_page'),
]