from .views import TopicListView,TopicDetailView,TopicCreatView,TopicUpdateView,TopicDeleteView
from django.urls import path

urlpatterns = [
    path("post/<int:pk>/delete/",TopicDeleteView.as_view(), name="post_delete"),
    path("post/<int:pk>/edit/",TopicUpdateView.as_view(), name="post_edit"),
    path("post/new/",TopicCreatView.as_view(),name="post_new"),
    path("post/<int:pk>/",TopicDetailView.as_view(),name ="post_detail"),
    path("",TopicListView.as_view(), name ="home"),
               ]