from django import forms

from django_ace import AceWidget
from .models import Lesson, Code_Template

class LessonForm(forms.ModelForm):
	class Meta:
		model = Lesson
		fields = '__all__'

		#model.lesson_code = 'static/code_templates/Python_Example_2.txt'

		widgets = {
			'lesson_code':AceWidget(mode='python',theme='twilight'),
		}

		form = {
			'template':'TemplateForm',
		}

class TemplateForm(forms.ModelForm):
	class Meta:
		model = Code_Template
		fields = '__all__'

		widgets = {
			'template_code':AceWidget(mode='python',theme='twilight'),
		}