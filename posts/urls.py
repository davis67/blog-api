
from django.urls import path
from .import views

urlpatterns = [
    path('', views.PostListAPIView.as_view(), name="posts"),
    path('create/', views.PostCreateAPIView.as_view(), name="posts.create"),
    path('show/<int:id>', views.PostDetailAPIView.as_view(), name="posts.show"),
    path('edit/<int:id>', views.PostUpdateAPIView.as_view(), name="posts.update"),
    path('delete/<int:id>', views.PostDestroyAPIView.as_view(),
         name="posts.destroy"),
    path("comment/<int:pk>/", views.CommentCreateAPIView.as_view(), name="add-comment")
]
