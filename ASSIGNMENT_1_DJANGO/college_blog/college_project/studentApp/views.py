from django.shortcuts import render, get_object_or_404
from .models import Student


def student_list(request):

    query = request.GET.get('q')
    dept = request.GET.get('dept')

    students = Student.objects.all()

    # Search by name
    if query:
        students = students.filter(name__icontains=query)

    # Filter by department
    if dept:
        students = students.filter(department__dept_name__iexact=dept)

    return render(request, 'studentApp/student_list.html', {
        'students': students
    })


def student_detail(request, slug):
    student = get_object_or_404(Student, slug=slug)
    return render(request, 'studentApp/student_detail.html', {
        'student': student
    })