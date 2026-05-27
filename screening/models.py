from django.db import models


class Patient(models.Model):
    RISK_CHOICES = (
        ('LOW', 'Low Risk'),
        ('MEDIUM', 'Medium Risk'),
        ('HIGH', 'High Risk'),
    )

    gender = models.CharField(max_length=10)

    age = models.IntegerField()

    bmi = models.FloatField()

    blood_pressure = models.FloatField()

    glucose_level = models.FloatField()

    family_history = models.BooleanField(default=False)

    risk_level = models.CharField(
        max_length=20,
        choices=RISK_CHOICES,
        blank=True,
        null=True
    )

    recommendation = models.TextField(blank=True, null=True)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Patient {self.id} - {self.risk_level}"