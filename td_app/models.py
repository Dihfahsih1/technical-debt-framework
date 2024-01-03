# techdebt/models.py

from django.db import models

class Project(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    
    def __str__(self):
        return self.name
class TechnicalDebt(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    aspect = models.CharField(max_length=255, help_text="Identify the aspect of technical debt")
    description = models.TextField(help_text="Describe the technical debt")
    metric_value = models.FloatField(help_text="Enter metric value for measurement")
    impact_category = models.CharField(max_length=255, help_text="Categorize the impact of technical debt")
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.project
