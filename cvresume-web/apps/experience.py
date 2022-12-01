from pprint import pprint
from rest_framework import serializers


from apps.models import WorkExperienceModel, EducationModel


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

