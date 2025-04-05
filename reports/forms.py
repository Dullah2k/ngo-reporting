from django import forms
from .models import Report, ReportPhoto

class ReportForm(forms.ModelForm):
	class Meta:
		model = Report
		exclude = ['organization', 'district', 'status', 'approved_by', 'created_at', 'updated_at']
		widgets = {
			'year': forms.NumberInput(attrs={'min': 2020, 'max': 2030}),
			'summary': forms.Textarea(attrs={'rows': 4}),
			'outcomes': forms.Textarea(attrs={'rows': 3}),
		}

class ReportPhotoForm(forms.ModelForm):
	class Meta:
		model = ReportPhoto
		fields = ['photo', 'caption']
		widgets = {
			'caption': forms.TextInput(attrs={'placeholder': 'Optional photo description'}),
		}