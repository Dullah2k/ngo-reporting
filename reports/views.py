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
	
	# Filtering logic
	if request.GET.get('year'):
		reports = reports.filter(year=request.GET['year'])
	if request.GET.get('quarter'):
		reports = reports.filter(quarter=request.GET['quarter'])
	if request.GET.get('sector'):
		reports = reports.filter(sector=request.GET['sector'])
	
	context = {
		'reports': reports,
		'is_admin': is_admin,
		'filter_values': request.GET,
	}
	return render(request, 'reports/list.html', context)

