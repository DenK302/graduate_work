from django.db import models
from django.urls import reverse


# Create your models here.

class Research(models.Model):
    topic = models.CharField(max_length=500, null=False, help_text="Введите тему исследования")
    purpose = models.TextField(null=False, help_text="Введите цель исследования")
    objectives = models.TextField(null=False, help_text="Введите задачи исследования")
    results = models.TextField(null=False, help_text="Введите планируемые результаты")
    scope = models.CharField(max_length=100, null=False, help_text="Введите планируемую сферу внедрения")
    organization = models.CharField(max_length=100, null=False, help_text="Введите название организации для внедрения")
    explanation = models.TextField(null=True, blank=True, help_text="Введите пояснение по планам внедрения (необязательно)")
    stage = models.CharField(max_length=50, null=True, help_text="Введите стадию проработки вопроса о внедрении")
    student = models.OneToOneField('Student', on_delete=models.SET_NULL, null=True, help_text="ФИО студента")
    teacher = models.ForeignKey('Teacher', on_delete=models.SET_NULL, null=True, help_text="ФИО преподавателя")
    date = models.DateField(null=False, help_text="Дата начала работы")
    score = models.IntegerField(null=True, blank=True, help_text="Введите полученную отметку")
    docfile = models.FileField(null=True, blank=True, help_text="Пояснительная записка")

    def __str__(self):
        """
        String for representing the Model object (in Admin site etc.)
        """
        return self.topic

    def get_absolute_url(self):
        """
        Returns the url to access a particular book instance.
        """
        return reverse('work-detail', args=[str(self.id)])

    class Meta:
        verbose_name = 'Исследовательская работа'
        verbose_name_plural = 'Исследовательские работы'


class Student(models.Model):
    full_name = models.CharField(max_length=200, null=False, help_text="Введите ФИО студента")
    STUDENT_CATEGORY = (
        ('С', 'Студент'),
        ('М', 'Магистрант'),
        ('А', 'Аспирант'),
    )
    category = models.CharField(max_length=1, choices=STUDENT_CATEGORY, default='С', help_text='Категория студента')
    STUDENT_SPECIALITY = (
        ('ИСТЭ', 'Инженер- программист-эколог'),
        ('ИСТЗ', 'Инженер-программист'),
        ('ПОД', 'Эколог. Инженер по охране окружающей среды'),
        ('ЭТЭМ', 'Инженер-энергоменеджер'),
        ('ЯРБ', 'Инженер'),
        ('МФ', 'Медицинский физик'),
    )
    MAGISTR_SPECIALITY = (
        ('ЭК', 'Экология'),
        ('МБД', 'Медико-биологическое дело'),
        ('МФ', 'Медицинская физика'),
        ('БИ', 'Биоинформатика'),
    )
    specialty = models.CharField(max_length=4, choices=(STUDENT_SPECIALITY + MAGISTR_SPECIALITY), default='ИСТЭ',
                                     help_text="Выберите специальность студента", null=True, blank=True)
    FORM_CATEGORY = (
        ('Б', 'Дневная, бюджетная'),
        ('П', 'Дневная, платная'),
        ('З', 'Заочная'),
    )
    form = models.CharField(max_length=1, choices=FORM_CATEGORY, null=True, blank=True, help_text="Выберите форму обучения студента")
    phone_number = models.CharField(max_length=18, null=True, blank=True, help_text="Введите номер телефона студента")
    email = models.CharField(max_length=30, null=True, blank=True, help_text="Введите электронную почту студента")
    kurs = models.CharField(max_length=1, null=True, blank=True, help_text="Введите курс обучения")  # можно добавить список из 4 и 5 курса
    date_start = models.DateField(null=False, help_text="Дата начала обучения")
    date_end = models.DateField(null=False, help_text="Дата окончания обучения")

    def __str__(self):
        """
        String for representing the Model object (in Admin site etc.)
        """
        return self.full_name

    def get_absolute_url(self):
        """
        Returns the url to access a particular book instance.
        """
        return reverse('student-detail', args=[str(self.id)])

    class Meta:
        verbose_name = 'Студент'
        verbose_name_plural = 'Студенты'


class Teacher(models.Model):
    full_name = models.CharField(max_length=200, null=False, help_text="Введите ФИО руководителя")
    degree = models.CharField(max_length=50, null=False, help_text="Введите степень руководителя")
    title = models.CharField(max_length=20, null=True, blank=True, help_text="Введите звание руководителя")
    phone_number = models.CharField(max_length=18, null=True, blank=True, help_text="Введите номер телефона руководителя")
    email = models.CharField(max_length=30, null=True, blank=True, help_text="Введите электронную почту руководителя")

    def __str__(self):
        """
        String for representing the Model object (in Admin site etc.)
        """
        return self.full_name

    def get_absolute_url(self):
        """
        Returns the url to access a particular book instance.
        """
        return reverse('teacher-detail', args=[str(self.id)])

    class Meta:
        verbose_name = 'Преподаватель'
        verbose_name_plural = 'Преподаватели'
