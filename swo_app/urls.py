from django.urls import path
from .views import CourseListView, LessonDetailView
from . import views

urlpatterns = [
    path('', views.home, name='app-home'),
    path('terms/', views.terms, name='app-terms'),
    path('donate/', views.donate, name='app-donate'),
    path('course/', CourseListView.as_view(), name='app-course'),
    path('course/<slug:slug>/', LessonDetailView.as_view(), name='lesson-detail'),
]

