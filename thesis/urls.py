from . import views
from django.conf.urls import include, url

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^works/$', views.ResearchListView.as_view(), name='works'),
    url(r'^work/(?P<pk>\d+)$', views.ResearchDetailView.as_view(), name='work-detail'),
    url(r'^students/$', views.StudentListView.as_view(), name='students'),
    url(r'^student/(?P<pk>\d+)$', views.StudentDetailView.as_view(), name='student-detail'),
    url(r'^teachers/$', views.TeacherListView.as_view(), name='teachers'),
    url(r'^teacher/(?P<pk>\d+)$', views.TeacherDetailView, name='teacher-detail'),
    url(r'^works/teacher/(?P<pk>\d+)$', views.TeacherWorksView, name='teacher-works'),
    url(r'^teachers/create/$', views.CreateTeacher, name='create-teacher'),
    url(r'^teachers/delete/(?P<pk>\d+)$', views.DeleteTeacher, name='delete-teacher'),
    url(r'^teachers/edit/(?P<pk>\d+$)', views.EditTeacher, name='edit-teacher'),
    url(r'^students/create/$', views.CreateStudent, name='create-student'),
    url(r'^students/delete/(?P<pk>\d+)$', views.DeleteStudent, name='delete-student'),
    url(r'^students/edit/(?P<pk>\d+$)', views.EditStudent, name='edit-student'),
    url(r'^works/create/$', views.CreateResearch, name='create-work'),
    url(r'^works/delete/(?P<pk>\d+)$', views.DeleteResearch, name='delete-work'),
    url(r'^works/edit/(?P<pk>\d+$)', views.EditResearch, name='edit-research'),
    url(r'^teachers/search/$', views.SearchTeacherView.as_view(), name='search_teacher_results'),
    url(r'^students/search/$', views.SearchStudentView.as_view(), name='search_student_results'),
    url(r'^works/search/$', views.SearchResearchView.as_view(), name='search_work_results'),
]
