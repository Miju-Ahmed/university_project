# courses/views.py
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic.edit import CreateView
from django.contrib import messages
from .models import Course, Department
from .forms import CourseForm

# --- Course List (Existing View, slightly updated) ---
def course_list(request):
    courses = Course.objects.all().order_by('title')
    return render(request, 'courses/course_list.html', {'courses': courses})

# --- Course Detail (Existing View, updated) ---
def course_detail(request, pk):
    course = get_object_or_404(Course, pk=pk)
    return render(request, 'courses/course_detail.html', {'course': course})


# --- Course Creation (New View) ---
class CourseCreateView(LoginRequiredMixin, UserPassesTestMixin, CreateView):
    model = Course
    form_class = CourseForm
    template_name = 'courses/course_form.html'
    success_url = reverse_lazy('course_list')

    # Test to make sure only teachers can create courses
    def test_func(self):
        return self.request.user.profile.user_type == 'teacher'

    def form_valid(self, form):
        # Assign the current teacher to the course automatically
        course = form.save()
        self.request.user.profile.teaching_courses.add(course)
        messages.success(self.request, 'Course created successfully!')
        return super().form_valid(form)


# --- Course Enrollment and Teaching Logic (New Views) ---
@login_required
def enroll_in_course(request, pk):
    course = get_object_or_404(Course, pk=pk)
    profile = request.user.profile

    if profile.user_type == 'student':
        profile.enrolled_courses.add(course)
        messages.success(request, f"You have successfully enrolled in {course.title}.")
    else:
        messages.error(request, "Only students can enroll in courses.")

    return redirect('course_detail', pk=pk)

@login_required
def assign_teacher_to_course(request, pk):
    course = get_object_or_404(Course, pk=pk)
    profile = request.user.profile

    if profile.user_type == 'teacher':
        profile.teaching_courses.add(course)
        messages.success(request, f"You are now assigned to teach {course.title}.")
    else:
        messages.error(request, "Only teachers can be assigned to courses.")

    return redirect('course_detail', pk=pk)