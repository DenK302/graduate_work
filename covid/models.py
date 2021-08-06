from django.db import models
from django.urls import reverse


# Create your models here.

class Employer(models.Model):
    fullname = models.CharField(max_length=200, null=False, help_text="ФИО сотрудника")
    birthdate = models.CharField(max_length=20, null=True, blank=True, help_text="Дата рождения")
    liveplace = models.TextField(null=False, help_text="Место жительства")
    employers_department = (
        ('1', 'Административно-хозяйственная часть'),
        ('2', 'Аспирантура'),
        ('3', 'Библиотека'),
        ('4', 'деканат факультета мониторинга окружающей среды'),
        ('5', 'деканат факультета повышения квалификации и переподготовки'),
        ('6', 'деканат факультета экологической медицины'),
        ('7', 'Директорат'),
        ('8', 'кафедра дополнительного образования'),
        ('9', 'кафедра иммунологии'),
        ('10', 'кафедра информационных технологий в экологии и медицине'),
        ('11', 'кафедра лингвистических дисциплин и межкультурных коммуникаций'),
        ('12', 'кафедра общей биологии и генетики'),
        ('13', 'кафедра общей и медицинской физики'),
        ('14', 'кафедра социально-гуманитарных наук и устойчивого развития'),
        ('15', 'кафедра физического воспитания'),
        ('16', 'кафедра экологического мониторинга и менеджмента'),
        ('17', 'кафедра экологической медицины и радиобиологии'),
        ('18', 'кафедра экологической химии и биохимии'),
        ('19', 'кафедра энергоэффективных технологий'),
        ('20', 'кафедра ядерной и радиационной безопасности'),
        ('21', 'Научно-исследовательский сектор'),
        ('22', 'Отдел бухгалтерского учета, отчетности и финансирования'),
        ('23', 'Отдел воспитательной работы с молодежью'),
        ('24', 'Отдел закупок и материально-технического снабжения'),
        ('25', 'Отдел кадровой и организационной работы'),
        ('26', 'Отдел международных связей'),
        ('27', 'Отдел технических средств обучения и коммуникаций'),
        ('28', 'Планово-экономический сектор'),
        ('29', 'Спортивный клуб'),
        ('30', 'учебная лаборатория экологической биотехнологии'),
        ('31', 'Учебно-методическая лаборатория инновационных технологий образования'),
        ('32', 'учебно-методическая лаборатория экологического образования'),
        ('33', 'Учебно-методический отдел'),
        ('34', 'Учебный корпус (ул.Ботаническая, 15)'),
        ('35', 'Учебный корпус № 1 (Долгобродская, 23)'),
        ('36', 'Факультет экологической медицины')
    )
    department = models.CharField(max_length=2, null=False, choices=employers_department, default=None, help_text="Подразделение")
    position = models.CharField(max_length=200, null=False, help_text="Должность")
    datefirst = models.DateField(null=True, blank=True, help_text="Дата первой вакцинации")
    datesecond = models.DateField(null=True, blank=True, help_text="Дата второй вакцинации")
    sertification = models.BooleanField(help_text="Наличие сертификата", default=False)
    sertificateid = models.CharField(max_length=40, help_text="", null=True, blank=True)
    vactinationplace1 = models.CharField(max_length=100, null=True, blank=True, help_text="Место первой вакцинации")
    vactinationplace2 = models.CharField(max_length=100, null=True, blank=True, help_text="Место второй вакцинации")
    vactinationfull = models.BooleanField(help_text="Полная вакцинация", default=False)
    wantmake = models.BooleanField(help_text="Желает ли сделать", default=False)
    wantmaketype = models.CharField(max_length=50, help_text="Тип прививки", null=True, blank=True)
    contraindications = models.CharField(max_length=100, help_text="Противопоказания", null=True, blank=True)

    def __str__(self):
        """
        String for representing the Model object (in Admin site etc.)
        """
        return self.fullname

    def get_absolute_url(self):
        """
        Returns the url to access a particular book instance.
        """
        return reverse('employer-detail', args=[str(self.id)])

    class Meta:
        verbose_name = 'Работник'
        verbose_name_plural = 'Работники'
