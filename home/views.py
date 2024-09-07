from django.shortcuts import render,redirect
from .forms import StudentForm
from .models import Student
from django.shortcuts import get_object_or_404

# Create your views here.
def student_list(request):
    student = Student.objects.all()
    return render (request, 'home/student_list.html', {'student':student})

def home(request):
    return render (request, 'home/index.html')


def create_student(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('student_list')
    else:
        form = StudentForm()
        return render (request, 'home/create_student.html', {'form':form})

def update_student(request, stu_id):
    student = Student.objects.get(pk=stu_id)
    if request.method == 'POST':
        form = StudentForm(request.POST, instance=student)
        if form.is_valid():
            form.save()
            return redirect('student_list')        
    else:
        form = StudentForm(instance=student)
        return render(request, 'home/update.html', {'form':form})

def delete_student(request, stu_id):
    student = Student.objects.get(pk=stu_id)
    if request.method == 'POST':
        student.delete()
        return redirect('student_list')
    else: 
        return render(request, 'home/delete.html')
    
# def search(requset):
#     query = requset.GET.get('search')
#     results = Student.objects.filter(field_icontains = query)
#     return render (requset, 'home/student_list.html', {'results':results})
    
