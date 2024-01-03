# techdebt/models.py

from django.db import models
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
from sklearn.preprocessing import LabelEncoder
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

    @staticmethod
    def train_model():
        # Load technical debt data
        tech_debts = TechnicalDebt.objects.all()

        # Prepare data
        X = tech_debts.values_list('metric_value', flat=True)
        y = tech_debts.values_list('impact_category', flat=True)

        # Encode impact categories
        label_encoder = LabelEncoder()
        y_encoded = label_encoder.fit_transform(y)

        # Split data into training and testing sets
        X_train, X_test, y_train, y_test = train_test_split(X, y_encoded, test_size=0.2, random_state=42)

        # Train a simple machine learning model (Random Forest for demonstration)
        model = RandomForestClassifier(n_estimators=100, random_state=42)
        model.fit(X_train.reshape(-1, 1), y_train)

        # Test the model
        y_pred = model.predict(X_test.reshape(-1, 1))
        accuracy = accuracy_score(y_test, y_pred)

        return model, accuracy

    # ... (other methods and fields)

