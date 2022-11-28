from django.contrib import admin

from apps.models import EducationModel, MenuModel, WorkExperienceModel, PagesModel, MiddlePicturiesModel, MiddlePages


@admin.register(EducationModel)
class EducationAdmin(admin.ModelAdmin):
	fields = [
		'title',
		'beginning_data',
		'complated_data'
	]
	list_display = [
		'id',
		'title',
		'beginning_data',
		'complated_data'
	]
	list_filter = ['id',
		'title',
		'beginning_data',
		'complated_data']

	ordering = ['title',]

@admin.register(MenuModel)
class MenuAdmin(admin.ModelAdmin):
	fields = [
		'id',
		'type_page',
		'id_pages',

	]

	list_display = [

		'type_page',
		'id_pages',

	]
	list_filter = [
		'type_page',
	]
	ordering = [
		'type_page',
	]


@admin.register(WorkExperienceModel)
class WorkExperienceAdmin(admin.ModelAdmin):
	fields = [
		'id',
		'title',
		'beginning_data',
		'complated_data',
		'preview_text',
	]
	list_display = [
		'title',
		'beginning_data',
		'complated_data',
		'preview_text',
	]
	filter = ['title',]
	ordering = ['beginning_data']

	list_filter = [
		'title',
		'beginning_data',
		'complated_data',
	]


@admin.register(PagesModel)
class PagesAdmin(admin.ModelAdmin):
	field = [
		'id',
		'type',
		'title',
		'creator',
		'preview_text',
		'date_created',
		'date_change',
		'from_menu',
		'url_path'
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

@admin.register(MiddlePicturiesModel)
class MiddlePicturiesAdmin(admin.ModelAdmin):
	fields = [
		'id',
		'pages',

	]

	list_display =[
		'pages',

	]

	list_filter = [
		'pages',
	]


@admin.register(MiddlePages)
class MiddlePagesAdmin(admin.ModelAdmin):
	fields = ['pages', ]

