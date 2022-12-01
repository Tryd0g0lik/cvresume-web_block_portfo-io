from django.contrib import admin

from apps.models import EducationModel, MiddlePicturiesModel, WorkExperienceModel, MenuModel, PagesModel, \
	PicturiesModel

#
# class MiddlePicturiesInline(admin.StackedInline):
# 	model = MiddlePageWExperience
# 	extra = 0

class PagesInline(admin.StackedInline):
	model = PagesModel
	extra = 0

@admin.register(MenuModel)
class MenuAdmin(admin.ModelAdmin):
	fields = [
		'id_pages',
		'type_page',
		'delete',
		]


	list_display = [
		"id",
		'type_page',
		'id_pages',

	]
	list_filter = [
		'type_page',
	]
	ordering = [
		'id_pages',
	]


@admin.register(EducationModel)
class EducationAdmin(admin.ModelAdmin):
	fields = [
		'title',
		'beginning_data',
		'complated_data',
		"preview_text",
		"public",
	]

	list_display = [
		'id',
		'title',
		'beginning_data',
		'complated_data',
		"preview_text",
		"public",
	]

	list_filter = ['id',
		'title',
		'beginning_data',
		'complated_data']

	ordering = ['title',]


@admin.register(WorkExperienceModel)
class WorkExperienceAdmin(admin.ModelAdmin):
	# inlines = [MiddlePicturiesInline, ]
	fields = [

		'name',
		'beginning_data',
		'complated_data',
		'preview_text',
		"public",
	]
	list_display = [
		'id',
		'name',
		'beginning_data',
		'complated_data',
		'preview_text',
		"public",
	]

	ordering = ['beginning_data']

	list_filter = [

		'beginning_data',
		'complated_data',
	]


@admin.register(PagesModel)
class PagesAdmin(admin.ModelAdmin):
	field = [
		'title',
		'type',
		'title',

		'preview_text',
		'date_created',
		'date_change',

		'from_menu',
		'url_path'
		'creator',
	]
	list_filter = [
		'type',
		'creator',
		'from_menu',
	]
	list_display = [
		'type',
		'title',
		'creator',
		'preview_text',
		'date_created',
		'date_change',
		'from_menu',
		'url_path'
	]

	# inlines = [MiddlePicturiesInline, ]

@admin.register(PicturiesModel)
class PicturiesAdmin(admin.ModelAdmin):
	fields = [
		'path',
		'date_created',
	]

	list_display = [
		'id',
		'path',
		'date_created',
	]

	list_filter = ['date_created',]

