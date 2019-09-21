from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView, TemplateView
from .models import Lesson
from django.conf import settings

import stripe

stripe.api_key = settings.STRIPE_SECRET_KEY

def home(request):
    return render(request, 'swo_app/home.html')

def course(request):
    chapter = None
    context = {
        'chapters': Lesson.objects.order_by('chapter').values_list('chapter', flat=True).distinct(),
        'lessons': Lesson.objects.all()
    }
    return render(request, 'swo_app/course.html', context)

def lesson(request):
    lessons = Lesson.objects.all()
    return render(request, 'swo_app/lesson.html', {'lessons': lessons})

class CourseListView(ListView):
    model = Lesson
    template_name = 'swo_app/course.html'

    def get_context_data(self, **kwargs):
        context = super(CourseListView, self).get_context_data(**kwargs)
        context['chapters'] = Lesson.objects.order_by('chapter').values_list('chapter', flat=True).distinct()
        context['lessons'] = Lesson.objects.order_by('lesson_number')
        return context
 
class LessonDetailView(DetailView):
    model = Lesson
    template_name = 'swo_app/lesson_detail.html'

    def get_context_data(self, **kwargs):
        object_list = Lesson.objects.order_by('lesson_number').values_list('slug', flat=True)
        context = super(LessonDetailView, self).get_context_data(object_list=object_list, **kwargs)
        return context

def terms(request):
    return render(request, 'swo_app/terms.html')

class DonatePageView(TemplateView):
    template_name = 'swo_app/donate.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['key'] = settings.STRIPE_PUBLISHABLE_KEY
        return context

def charge(request):
    if request.method == 'POST':
        charge = stripe.Charge.create(
            amount=500,
            currency='usd',
            description='A Django charge',
            source=request.POST['stripeToken']
        )
        return render(request, 'swo_app/charge.html')
    else:
        return redirect(home)
    
