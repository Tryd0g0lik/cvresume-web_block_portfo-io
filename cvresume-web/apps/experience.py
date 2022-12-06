from pprint import pprint
from rest_framework import serializers


from apps.models import WorkExperienceModel, EducationModel, MenuModel
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




class Experience_db():

	def db_pulication(self) -> dict:
		"""
		TODO: receives filtered data of the db tables WorkExperienceModel\
		 and EducationModel
		:return: type dictionary
		"""
		experience_public = WorkExperienceModel.objects.filter(public='PUBLIC')
		education_public = EducationModel.objects.filter(public='PUBLIC')

		public_expe = []
		public_edu = []
		for exp in experience_public: public_expe.append(exp)
		for edu in education_public: public_edu.append(edu)

		return {
			'experince': public_expe,
			'education': public_edu	}

	def main_menu(self):
		page = []
		respons_position_menu = MenuModel.objects.filter(public='PUBLIC')

		for _position in respons_position_menu:

			page.append({"type_page": _position.type_page,
			             "title": _position.title,
			             "slug": _position.title.url_path,
			             "preview_text": _position.title.preview_text,
			             "description": _position.title.description,
			             "date_created": _position.title.date_created,
			             "date_change": _position.title.date_change,
			             } )
		return {'page': page}





# class Create_menu():
# 	def receive_data(self):
# 		MenuModel.project.
