import time

from django.conf import settings
from django.db import models

# Create your models here.
from django.utils import timezone


class TypeMenuChoise(models.TextChoices):
	'''
	TODO: The type title of menu
	'''

	PARENTS = "PARENTS", "Родительский"
	CHILDE = "CHILDE", "Дочернеий"

class MenuModel(models.Model):
	type_page=models.TextChoices(
		choices=TypeMenuChoise.choices,
		default=TypeMenuChoise.PARENTS,
	)
	id_pages=models.ForeignKey(
		'PagesModel',
		on_delete=models.CASCADE,
	)
	id_parents_pages = models.ForeignKey(
		'PagesModel',
		on_delete=models.CASCADE,
	)

	def __str__(self):
		return 'Страница: %s, тип: %s' % (self.id_pages, self.type_page)

	class Meta:
		verdose_name = "Заголовок"
		verbose_name_plural="Заголовки страницы"


class WorkExperienceModel(models.Nodel):
	beginning_data = models.DateField(
		verbose_name='Начало обучения',
		help_text='Дата начала обучения',
	)
	complated_data = models.DateField(
	verbose_name="Окончание учёбы",
	help_text="Дата окончания обучения",
	blank=True,
	)
	preview_text = models.TextField(
		max_length=100,
		blank=True,
		help_text="Превью описание"
	)

	def __str__(self):
		return "Начало: %s, Окончание %s" % (self.beginning_data,
		                                     self.complated_data,)

	class Meta:
		verbose_name = "Дата работы"
		verbose_name_plural = "Опыт работ"


class EducationModel(models.Model):
	beginning_data=models.DateField(
		verbose_name='Начало работы',
		help_text='Начало работы в должности',
	)
	complated_data=models.DateField(
		help_text='Окончание работы',
		blank=True,
	)

	def __str__(self):
		return "Начало: %s, Окончание %s" % (self.beginning_data,
		                                     self.complated_data,)

	class Meta:
		verbose_name = "Дата обучения"
		verbose_name_plural = "Сроки обучения"


class TypePageChoices(models.TextChoices):
	'''
	TODO: The page view
	'''
	ARTICLE = "ARTICLE", "Запись"
	PAGE = "PAGE", "Страница"

class PagesModel(models.Model):
	type = models.TextField(
		choices=TypePageChoices.choices,
		default=TypePageChoices.PAGE,
		verbose_name="Тип страницы",
	)
	title=models.TextField(
		max_length=70,
		null=True,
	)
	creator = models.ForeignKey(
		settings.AUTH_USERMODEL,
		on_delete=models.CASCADE,
		verbose_name="Пользователь",
		help_text="Пользователь создал",
	)
	preview_text=models.TextField(
		verbose_name="Краткое описание",
		help_text="Краткое описание не более 50 символов",
		blank=True
	)
	description=models.CharField(
		max_length=2000,
		verbose_name="Содержание",
		blank=True,
	)
	date_created=models.DateTimeField(
		auto_now=True,
		verbose_name="Создана",
	)

	date_change=models.DateTimeField(
		auto_now_add=True,
		verbose_name="Отредактирована",
	)
	from_menu=models.BooleanField(
		null=True,
		verbose_name="Указать в меню"
	)

	def __str__(self):
		return '%s' % (self.title, )

	class Meta:
		verbose_name  = "Страница",
		verbose_name_plural = "Страницы"


class PicturiesModel(models.Model):
	path = models.ImageField(
		max_length=80,
		width_field='Width',
		height_feild='Height',
		upload_to='files/pictures/%Y/%m/%d/',
	)
	date_created=models.DateTimeField(
		help_text='Дата загрузки',
	)

	def __str__(self):
		return '%s' % (self.path, )

	class Meta:
		verbose_name="Путь к img"
		verbose_name_plural="Путь к изображениям"