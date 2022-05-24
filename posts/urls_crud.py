from django.urls import path

from . import views_crud

urlpatterns = [
    path('', views_crud.index, name='index'),
    path('read/', views_crud.read, name='read'),
    path('create/', views_crud.create, name='create'),
    path('edit/<int:id>/', views_crud.edit, name='edit'),
    path('edit/update/<int:id>/', views_crud.update, name='update'),
    path('delete/<int:id>/', views_crud.delete, name='delete'),

]

# <int:id> id를 정수형태로 매핑해서 view에 전달