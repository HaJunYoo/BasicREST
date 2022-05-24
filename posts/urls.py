from django.urls import path

from . import views
from .views import jsonview, viewfeed, viewjson, viewrest


#views.Postlist 에는 수많은 메소드가 있다.
urlpatterns = [
    path('', views.PostList.as_view()),
    path('<int:pk>/', views.PostDetail.as_view()),
    path('jsonview/', jsonview, name='jsonview'),
    path('viewfeed/', viewfeed, name='viewfeed'),
    path('viewjson/', viewjson, name='viewjson'),
    path('viewrest/', viewrest, name='viewrest'),

]
