from django.db.models.functions import TruncYear, Cast
from django.shortcuts import render, get_object_or_404
from .models import Teacher, Student, Research
from django.views import generic
from django.db.models import Q, Sum, Count
from django.views.generic import TemplateView, ListView
from django.http import Http404, HttpResponseRedirect, HttpResponseNotFound
from django.urls import reverse
import os
from django.contrib.auth.decorators import login_required
from django.db.models import FloatField


def index(request):
    latest_research_list = Research.objects.order_by('-date')[:6]
    return render(
        request,
        'index.html',
        context={'latest_research_list': latest_research_list},
    )


class ResearchListView(generic.ListView):
    model = Research
    paginate_by = 5

    def get_queryset(self):
        research_list = Research.objects.order_by('-date')
        return research_list


def TeacherWorksView(request, pk):
    try:
        works_list = Research.objects.filter(teacher=Teacher.objects.get(pk=pk))
    except Research.DoesNotExist:
        raise Http404("Research does not exist")
    return render(
        request,
        'thesis/research_list.html',
        context={'research_list': works_list.order_by('-date')}
    )


class ResearchDetailView(generic.DetailView):
    model = Research

    def research_detail_view(request, pk):
        try:
            research_id = Research.objects.get(pk=pk)
        except Research.DoesNotExist:
            raise Http404("Research does not exist")

        return render(
            request,
            'thesis/research_detail.html',
            context={'research': research_id, }
        )


class SearchResearchView(ListView):
    model = Research
    template_name = 'thesis/research_list.html'

    def get_queryset(self):  # новый
        query = self.request.GET.get('query')
        object_list = Research.objects.filter(
            Q(topic__icontains=query.title())
        )
        return object_list


class StudentListView(generic.ListView):
    model = Student
    paginate_by = 5

    def get_queryset(self):
        student_list = Student.objects.order_by('full_name')
        return student_list


class StudentDetailView(generic.DetailView):
    model = Student

    def student_detail_view(request, pk):
        try:
            student_id = Student.objects.get(pk=pk)
        except Student.DoesNotExist:
            raise Http404("Student does not exist")

        return render(
            request,
            'thesis/student_detail.html',
            context={'student': student_id, }
        )


class SearchStudentView(ListView):
    model = Student
    template_name = 'thesis/student_list.html'

    def get_queryset(self):
        query = self.request.GET.get('query')
        object_list = Student.objects.filter(Q(full_name__icontains=query.title()))
        return object_list


class TeacherListView(generic.ListView):
    model = Teacher
    paginate_by = 5

    def get_queryset(self):
        teacher_list = Teacher.objects.order_by('full_name')
        return teacher_list


def TeacherDetailView(request, pk):
    try:
        teacher = Teacher.objects.get(pk=pk)
    except Teacher.DoesNotExist:
        raise Http404("Teacher does not exist")
    years = list()
    srb = list()
    researches_per_year = teacher.research_set.annotate(year=TruncYear('date')).values('year').annotate(
        sr_ball=Cast(Sum('score'), FloatField()) / Cast((Count('score')), FloatField()))
    for research in researches_per_year:
        years.append(research['year'].year)
        srb.append(research['sr_ball'])
    research_year_info = zip(years, srb)
    return render(
        request,
        'thesis/teacher_detail.html',
        {"teacher": teacher, "researches_year_info": research_year_info}
    )


class SearchTeacherView(ListView):
    model = Teacher
    template_name = 'thesis/teacher_list.html'

    def get_queryset(self):
        query = self.request.GET.get('query')
        object_list = Teacher.objects.filter(
            Q(full_name__icontains=query.title())
        )
        return object_list


@login_required
def CreateTeacher(request):
    if request.POST:
        a = Teacher(
            full_name=request.POST['full_name'],
            degree=request.POST['degree'],
            title=request.POST['title'],
            phone_number=request.POST['phone_number'],
            email=request.POST['email']
        )
        a.save()
        return HttpResponseRedirect(reverse('teachers'))
    else:
        return render(request, "thesis/create_teacher.html")


@login_required
def DeleteTeacher(request, pk):
    try:
        teacher = Teacher.objects.get(pk=pk)
        teacher.delete()
        return HttpResponseRedirect(reverse('teachers'))
    except Teacher.DoesNotExist:
        return HttpResponseNotFound("<h2>Руководитель не найден</h2>")


@login_required
def EditTeacher(request, pk):
    try:
        teacher = Teacher.objects.get(pk=pk)
        if request.POST:
            teacher.full_name = request.POST.get("full_name")
            teacher.degree = request.POST.get("degree")
            teacher.title = request.POST.get("title")
            teacher.phone_number = request.POST.get("phone_number")
            teacher.email = request.POST.get("email")
            teacher.save()
            return HttpResponseRedirect(reverse('teachers'))
        else:
            return render(request, "thesis/edit_teacher.html", {"teacher": teacher})
    except Teacher.DoesNotExist:
        return HttpResponseNotFound("<h2>Преподаватель не найден</h2>")


@login_required
def CreateStudent(request):
    if request.POST:
        a = Student(
            full_name=request.POST['full_name'],
            category=request.POST['category'],
            specialty=request.POST['specialty'],
            form=request.POST['form'],
            phone_number=request.POST['phone_number'],
            email=request.POST['email'],
            date_start=request.POST['date_start'],
            date_end=request.POST['date_end']
        )
        a.save()
        return HttpResponseRedirect(reverse('students'))
    else:
        return render(request, "thesis/create_student.html",
                      {"category_student": Student.STUDENT_CATEGORY, "student_specialty": Student.STUDENT_SPECIALITY,
                       "magistr_specialty": Student.MAGISTR_SPECIALITY, "student_form": Student.FORM_CATEGORY})


@login_required
def DeleteStudent(request, pk):
    try:
        student = Student.objects.get(pk=pk)
        student.delete()
        return HttpResponseRedirect(reverse('students'))
    except Student.DoesNotExist:
        return HttpResponseNotFound("<h2>Студент не найден</h2>")


@login_required
def EditStudent(request, pk):
    try:
        student = Student.objects.get(pk=pk)
        if request.POST:
            student.full_name = request.POST.get("full_name")
            student.category = request.POST.get("category")
            student.specialty = request.POST.get("specialty")
            student.form = request.POST.get("form")
            student.phone_number = request.POST.get("phone_number")
            student.email = request.POST.get("email")
            student.date_start = request.POST.get("date_start")
            student.date_end = request.POST.get("date_end")
            student.save()
            return HttpResponseRedirect(reverse('students'))
        else:
            return render(request, "thesis/edit_student.html",
                          {"student": student, "category_student": Student.STUDENT_CATEGORY,
                           "student_specialty": Student.STUDENT_SPECIALITY,
                           "magistr_specialty": Student.MAGISTR_SPECIALITY, "student_form": Student.FORM_CATEGORY})
    except Student.DoesNotExist:
        return HttpResponseNotFound("<h2>Студент не найден</h2>")


@login_required
def CreateResearch(request):
    students = Student.objects.all()
    teachers = Teacher.objects.all()
    if request.POST:
        a = Research(
            topic=request.POST['topic'],
            purpose=request.POST['purpose'],
            objectives=request.POST['objectives'],
            results=request.POST['results'],
            scope=request.POST['scope'],
            organization=request.POST['organization'],
            explanation=request.POST['explanation'],
            stage=request.POST['stage'],
            student=Student.objects.get(id=request.POST['student_id']),
            teacher=Teacher.objects.get(id=request.POST['teacher_id']),
            date=request.POST['date_create'],
        )
        if request.POST['score'] == "":
            a.score = None
        else:
            a.score = request.POST['score']
        a.save()
        if request.FILES:
            a.docfile = request.FILES.get("docs")
            extension = os.path.splitext(a.docfile.name)[1]
            a.docfile.name = a.topic + extension
            a.save()
        return HttpResponseRedirect(reverse('works'))
    else:
        return render(request, "thesis/create_work.html", {"students": students, "teachers": teachers})


@login_required
def DeleteResearch(request, pk):
    try:
        research = Research.objects.get(pk=pk)
        research.docfile.delete()
        research.delete()
        return HttpResponseRedirect(reverse('works'))
    except Research.DoesNotExist:
        return HttpResponseNotFound("<h2>Исследование не найдено</h2>")


@login_required
def EditResearch(request, pk):
    try:
        research = Research.objects.get(pk=pk)
        students = Student.objects.all()
        teachers = Teacher.objects.all()
        if request.POST:
            research.topic = request.POST.get("topic")
            research.purpose = request.POST.get("purpose")
            research.objectives = request.POST.get("objectives")
            research.results = request.POST.get("results")
            research.scope = request.POST.get("scope")
            research.organization = request.POST.get("organization")
            research.explanation = request.POST.get("explanation")
            research.stage = request.POST.get("stage")
            research.student = Student.objects.get(
                id=request.POST.get('student_id'))
            research.teacher = Teacher.objects.get(id=request.POST.get('teacher_id'))
            if request.POST.get("score") == "":
                research.score = None
            else:
                research.score = request.POST.get("score")
            research.date = request.POST.get("date_create")
            research.save()
            if request.FILES:
                research.docfile.delete()
                research.docfile = request.FILES.get("docs")
                extension = os.path.splitext(research.docfile.name)[1]
                research.docfile.name = research.topic + extension
                research.save()
            return HttpResponseRedirect(reverse('works'))
        else:
            return render(request, "thesis/edit_work.html",
                          {"research": research, "students": students, "teachers": teachers})
    except Research.DoesNotExist:
        return HttpResponseNotFound("<h2>Исследование не найдено</h2>")
