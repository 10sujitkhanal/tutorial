from django.shortcuts import render, get_object_or_404
from .models import Course, Category, Lesson
from django.core.paginator import Paginator

# Create your views here.
def home(request):
    course = Course.objects.all().order_by('-created_at')[:6]
    category = Category.objects.all()
    return render(request, 'index.html', {'course': course, 'category': category})

def course_list(request):
    category = request.GET.get('category')
    if category:
        course_queryset = Course.objects.filter(category__slug=category).select_related('category').all()
    else:
        course_queryset = Course.objects.select_related('category').all()
    paginator = Paginator(course_queryset, 6)  # 6 courses per page
    page_number = request.GET.get('page')
    courses = paginator.get_page(page_number)

    

    context = {
        'course': courses,
        'category': Category.objects.all(),
    }
    return render(request, 'course_list.html', context)

def details(request, slug):
    course = get_object_or_404(Course.objects.prefetch_related('lessons', 'category'), slug=slug)
    lesson = Lesson.objects.get(order=1)
    return render(request, 'details.html', {'course': course, 'lesson': lesson})

def lesson_detail(request, course_slug, lesson_slug):
    course = get_object_or_404(Course, slug=course_slug)
    lesson = get_object_or_404(Lesson, slug=lesson_slug, course=course)

    return render(request, 'lesson_details.html', {'course': course, 'lesson': lesson})