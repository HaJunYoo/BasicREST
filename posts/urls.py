from django.urls import path

from . import views


#views.Postlist 에는 수많은 메소드가 있다.
urlpatterns = [
    path('', views.PostList.as_view()),
    path('<int:pk>/', views.PostDetail.as_view()),
]
