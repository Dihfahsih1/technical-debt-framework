# techdebt/views.py

from django.shortcuts import render, get_object_or_404, redirect
from .models import Project, TechnicalDebt
from .forms import ProjectForm, TechnicalDebtForm

def project_list(request):
    projects = Project.objects.all()
    return render(request, 'techdebt/project_list.html', {'projects': projects})

def project_detail(request, project_id):
    project = get_object_or_404(Project, pk=project_id)
    tech_debts = TechnicalDebt.objects.filter(project=project)
    total_tech_debt = tech_debts.count()

    # Calculate average metric value for all technical debts in the project
    avg_metric_value = tech_debts.aggregate(avg_metric=models.Avg('metric_value'))['avg_metric']

    return render(request, 'techdebt/project_detail.html', {
        'project': project,
        'tech_debts': tech_debts,
        'total_tech_debt': total_tech_debt,
        'avg_metric_value': avg_metric_value,
    })

def add_project(request):
    if request.method == 'POST':
        form = ProjectForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('project_list')
    else:
        form = ProjectForm()
    return render(request, 'techdebt/add_project.html', {'form': form})

def add_technical_debt(request, project_id):
    project = get_object_or_404(Project, pk=project_id)

    if request.method == 'POST':
        form = TechnicalDebtForm(request.POST)
        if form.is_valid():
            technical_debt = form.save(commit=False)
            technical_debt.project = project
            technical_debt.save()
            return redirect('project_detail', project_id=project_id)
    else:
        form = TechnicalDebtForm()

    return render(request, 'techdebt/add_technical_debt.html', {'form': form, 'project': project})

def early_repayment_guidance(request, project_id):
    project = get_object_or_404(Project, pk=project_id)
    tech_debts = TechnicalDebt.objects.filter(project=project)

    # Implement logic to guide teams on early repayment based on identified patterns
    # For example, identify technical debts with high impact and suggest early repayment strategies

    high_impact_tech_debts = tech_debts.filter(impact_category='High Impact')
    
    return render(request, 'techdebt/early_repayment_guidance.html', {
        'project': project,
        'tech_debts': tech_debts,
        'high_impact_tech_debts': high_impact_tech_debts,
    })
