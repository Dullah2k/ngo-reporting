from django.shortcuts import render, redirect
from django.db.models import Q
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import ReportForm, ReportPhotoForm
from .models import ReportPhoto
from .models import Report

@login_required
def create_report(request):
	if request.method == 'POST':
		report_form = ReportForm(request.POST)
		photo_form = ReportPhotoForm(request.POST, request.FILES)
		
		if report_form.is_valid() and photo_form.is_valid():
			report = report_form.save(commit=False)
			report.organization = request.user
			report.save()
			
			# Save photos
			for file in request.FILES.getlist('photos'):
				ReportPhoto.objects.create(
					report=report,
					photo=file,
					caption=photo_form.cleaned_data.get('caption', '')
				)
			
			messages.success(request, 'Report submitted successfully!')
			return redirect('reports:report_list')
	else:
		report_form = ReportForm()
		photo_form = ReportPhotoForm()

	return render(request, 'reports/create.html', {
		'report_form': report_form,
		'photo_form': photo_form,
	})

def report_list(request):
	reports = Report.objects.all()
	is_admin = request.user.is_staff
	
	if not is_admin:
		reports = reports.filter(organization=request.user)
	
	# Filtering parameters
	filters = {
		'year': request.GET.get('year'),
		'quarter': request.GET.get('quarter'),
		'status': request.GET.get('status'),
		'sector': request.GET.get('sector'),
		'ward': request.GET.get('ward'),
	}
	
	# Apply filters
	for key, value in filters.items():
		if value:
			reports = reports.filter(**{key: value})
	
	context = {
		'reports': reports,
		'is_admin': is_admin,
		'filter_values': request.GET,
		# Add these to make choices available in template
		'quarter_choices': Report.Quarter.choices,
		'status_choices': Report.Status.choices,
		'sector_choices': Report.Sector.choices,
		'ward_choices': Report.WardChoices.choices,
	}

	return render(request, 'reports/list.html', context)

