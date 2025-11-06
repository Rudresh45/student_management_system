from django.shortcuts import render, redirect, get_object_or_404
from urllib3 import request
from .models import Student
from .forms import StudentForm
from django.contrib import messages


def dashboard(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Student added successfully')
            return redirect('students:dashboard')
    else:
        form = StudentForm()
    total_students = Student.objects.count()
    latest_students = Student.objects.order_by('-created_at')[:5]
    context = {
    'form': form,
    'total_students': total_students,
    'latest_students': latest_students,
    }
    return render(request, 'students/dashboard.html', context)

# List view
def student_list(request):
    query = request.GET.get('q')
    if query:
        students = Student.objects.filter(first_name__icontains=query) | Student.objects.filter(last_name__icontains=query) | Student.objects.filter(roll_number__icontains=query)
    else:
        students = Student.objects.all().order_by('roll_number')

    return render(request, 'students/list.html', {'students': students, 'query': query})


# Create page (separate create form if you prefer)
def student_create(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Student created')
            return redirect('students:student_list')
    else:
        form = StudentForm()
        return render(request, 'students/create.html', {'form': form})

# Edit
def student_edit(request, pk):
    student = get_object_or_404(Student, pk=pk)
    if request.method == 'POST':
        form = StudentForm(request.POST, instance=student)
        if form.is_valid():
            form.save()
            messages.success(request, 'Student updated')
            return redirect('students:student_list')
    else:
        form = StudentForm(instance=student)
        return render(request, 'students/edit.html', {'form': form, 'student': student})
    
    # Delete
def student_delete(request, pk):
    student = get_object_or_404(Student, pk=pk)
    if request.method == 'POST':
        student.delete()
        messages.success(request, 'Student deleted')
        return redirect('students:student_list')
    return render(request, 'students/delete.html', {'student': student})