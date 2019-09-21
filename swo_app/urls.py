from django.urls import path
from .views import CourseListView, LessonDetailView, DonatePageView
from . import views

urlpatterns = [
    path('', views.home, name='app-home'),
    path('terms/', views.terms, name='app-terms'),
    path('charge/', views.charge, name='app-charge'),
    path('donate/', DonatePageView.as_view(), name='app-donate'),
    path('course/', CourseListView.as_view(), name='app-course'),
    path('course/<slug:slug>/', LessonDetailView.as_view(), name='lesson-detail'),
]

