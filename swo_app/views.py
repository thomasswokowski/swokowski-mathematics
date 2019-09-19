from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Lesson

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

def donate(request):
    return render(request, 'swo_app/donate.html')

    
