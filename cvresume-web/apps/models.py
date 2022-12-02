import time

from django.conf import settings
from django.db import models
from PIL import Image, ImageFile
# Create your models here.
from django.template.defaultfilters import slugify
from django.utils import timezone
import re
def _slug_page(
	_name_text_field: str,
	_max_leng_url: int,
) -> str:
	_url: str = None
	_reg = (r'([\w]*[^\\\-;\\/ \\,\\><])')
	_url_line = str(re.findall(_reg, _name_text_field, flags=re.ASCII)) \
		            .replace(' ', '_').strip("][").replace("'", '') \
		            .replace(",", '')[: _max_leng_url]
	return (_url_line)


class TypeMenuChoise(models.TextChoices):
	'''
	TODO: The type title of menu
	'''

	PARENTS = "PARENTS", "Родительский"
	CHILDE = "CHILDE", "Дочернеий"

class PublicationChoise(models.TextChoices):
	'''
	TODO: The block will be publication or not.\
	 Used inside models a WorkExperienceModel and EducationModel
	'''
	PUBLIC = "PUBLIC", "Публикация"
	NOPUBLIC = 'NOPUBLIC', "----"

class TypePageChoices(models.TextChoices):
	'''
	TODO: The page view
	'''
	ARTICLE = "ARTICLE", "Запись"
	PAGE = "PAGE", "Страница"


class MenuModel(models.Model):

	type_page = models.TextField (
		max_length=50,
		choices=TypeMenuChoise.choices,
		default=TypeMenuChoise.PARENTS,
	)
	title = models.ForeignKey(
		'PagesModel',
		on_delete=models.CASCADE,
		related_name='pagesChild'

	)
	public = models.TextField(
		choices=PublicationChoise.choices,
		default=PublicationChoise.NOPUBLIC,
		help_text="Публикуем на странице или нет. По умолчанию, публикации нет",
		verbose_name="Публикация",
	)

	def __str__(self):
		return 'Страница: %s, тип: %s' % (self.title, self.type_page)

	class Meta:
		verbose_name = "Раздел меню"
		verbose_name_plural="Разделы меню"


class WorkExperienceModel(models.Model):
	name = models.ForeignKey(
			'PagesModel',
			verbose_name="Должность",
			on_delete=models.CASCADE,
			related_name='namePositionsMenu'
	)
	beginning_data = models.DateField(
		verbose_name='Начало обучения',
		help_text='Дата начала обучения',
	)
	complated_data = models.DateField(
		verbose_name="Окончание учёбы",
		help_text="Дата окончания обучения",
		blank=True,
	)
	preview_text = models.ForeignKey(
		"PagesModel",
		on_delete=models.CASCADE,
		blank=True,
		verbose_name="Краткое описание",
		help_text="Краткое описание в 80 символов",
		related_name='previewPositionsMenu'
	)

	public = models.TextField(
		choices=PublicationChoise.choices,
		default=PublicationChoise.NOPUBLIC,
		help_text="Публикуем на странице или нет. По умолчанию, публикации нет",
		verbose_name="Публикация",
	)

	def __str__(self):
		return "Начало: %s, Окончание %s" % (self.beginning_data,
		                                     self.complated_data,)

	class Meta:
		verbose_name = "Дата работы"
		verbose_name_plural = "Опыт работ"


class EducationModel(models.Model):
	title = models.ForeignKey(
		'PagesModel',
		on_delete=models.CASCADE,
		related_name='titlePositionsMenuExpe',
		help_text="Наименование курса",
	)
	beginning_data=models.DateField(
		verbose_name='Начало работы',
		help_text='Начало работы в должности',
	)

	complated_data=models.DateField(
		help_text='Окончание работы',
		blank=True,
	)
	preview_text = models.ForeignKey(
		"PagesModel",
		on_delete=models.CASCADE,
		blank=True,
		verbose_name="Краткое описание",
		help_text="Краткое описание в 80 символов",
		related_name='previewPositionsMenuExpe',
	)
	public = models.TextField(
		choices=PublicationChoise.choices,
		default=PublicationChoise.NOPUBLIC,
		help_text="Публикуем на странице или нет. По умолчанию, публикации нет",
		verbose_name="Публикация",
	)

	def __str__(self):
		return "Начало: %s, Окончание %s" % (self.beginning_data,
		                                     self.complated_data,)

	class Meta:
		verbose_name = "Образование"
		verbose_name_plural = "Образование"

class PagesModel(models.Model):
	type = models.CharField(
		max_length=50,
		choices=TypePageChoices.choices,
		default=TypePageChoices.PAGE,
		verbose_name="Тип страницы",
	)
	title=models.CharField(
		max_length=80,
		null=True,
		verbose_name="Название"
	)
	creator = models.ForeignKey(
		settings.AUTH_USER_MODEL,
		on_delete=models.CASCADE,
		verbose_name="Пользователь",
		help_text="Пользователь создал",
		related_name="correctUser"
	)
	preview_text=models.CharField(
		max_length=150,
		verbose_name="Краткое описание",
		help_text="Краткое описание не более 50 символов",
		blank=True
	)
	description=models.TextField(
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

	public = models.TextField(
		choices=PublicationChoise.choices,
		default=PublicationChoise.NOPUBLIC,
		help_text="Публикуем на странице или нет. По умолчанию, публикации нет",
		verbose_name="Публикация",
	)


	url_path = models.SlugField(
			max_length=50,
			verbose_name='url',
			help_text='Путь к странице',
			db_index=True,
			unique=True,
			null=True,
		)


	def __str__(self):
		return '%s' % (self.title, )

	def save(self, *args, **kwargs):
		if not self.id:
			# Newly created object, so set slug
			self.url_path = slugify(self.title)
		super(PagesModel, self).save(*args, **kwargs)

	class Meta:
		verbose_name  = "Страница",
		verbose_name_plural = "Страницы"


class PicturiesModel(models.Model):
	path = models.ImageField(
		max_length=80,
		upload_to='cvresume-web/files/pictures/%Y/%m/%d/',
	)
	date_created=models.DateTimeField(
		help_text='Дата загрузки',
	)


	def __str__(self):
		return '%s' % (self.path, )

	class Meta:
		verbose_name = "Путь к img"
		verbose_name_plural = "Путь к изображениям"

class MiddlePicturiesModel(models.Model):
	pages = models.ForeignKey(
		PagesModel,
		on_delete=models.CASCADE,
		related_name='imgPages',
	  )

	pathPictiries = models.ForeignKey(
		PicturiesModel,
		on_delete=models.CASCADE,
		related_name='imgPath',
	)

	def __str__(self):
		return 'Страница: %s и изображение: %s' % (self.pages, self.pathPictiries)

	class Meta:
		verbose_name = "Изображение не странице"
		verbose_name_plural = "Изображения страницы"


