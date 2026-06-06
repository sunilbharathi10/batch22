from django.shortcuts import render, redirect, get_object_or_404
from .models import Student
from .forms import StudentForm


# CREATE + READ
def student_list(request):

    if request.method == "POST":

        form = StudentForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('student_list')

    else:
        form = StudentForm()

    students = Student.objects.all()

    return render(
        request,
        'list.html',
        {
            'form': form,
            'students': students
        }
    )


# UPDATE
def update_student(request, id):

    student = get_object_or_404(
        Student,
        id=id
    )

    if request.method == "POST":

        form = StudentForm(
            request.POST,
            instance=student
        )

        if form.is_valid():
            form.save()
            return redirect('student_list')

    else:

        form = StudentForm(
            instance=student
        )

    return render(
        request,
        'update.html',
        {'form': form}
    )


# DELETE
def delete_student(request, id):

    student = get_object_or_404(
        Student,
        id=id
    )

    student.delete()

    return redirect('student_list')