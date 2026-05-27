from django.shortcuts import (
    render,
    redirect,
    get_object_or_404
)

from .forms import PatientForm
from .models import Patient

import joblib
import numpy as np


model = joblib.load('diabetes_model.pkl')


METRICS = {
    'accuracy': '87%',
    'precision': '84%',
    'recall': '91%',
    'specificity': '82%',
    'auc': '0.89',
}


def generate_recommendation(risk):

    if risk == 'LOW':

        return (
            'Lifestyle advice and routine follow-up.'
        )

    elif risk == 'MEDIUM':

        return (
            'Repeat glucose testing and counselling.'
        )

    return (
        'Immediate referral to secondary healthcare.'
    )


def home(request):

    form = PatientForm()

    if request.method == 'POST':

        form = PatientForm(request.POST)

        if form.is_valid():

            patient = form.save(commit=False)

            gender = (
                1 if patient.gender == 'Male'
                else 0
            )

            features = np.array([[
                gender,
                patient.age,
                patient.bmi,
                patient.blood_pressure,
                patient.glucose_level,
                patient.family_history
            ]])

            prediction = model.predict(features)[0]

            patient.risk_level = prediction

            patient.recommendation = (
                generate_recommendation(
                    prediction
                )
            )

            patient.save()

            return redirect(
                'result',
                patient.id
            )

    context = {
        'form': form
    }

    return render(
        request,
        'home.html',
        context
    )


def result(request, patient_id):

    patient = get_object_or_404(
        Patient,
        id=patient_id
    )

    context = {
        'patient': patient
    }

    return render(
        request,
        'result.html',
        context
    )


def history(request):

    patients = Patient.objects.all().order_by(
        '-created_at'
    )

    context = {
        'patients': patients
    }

    return render(
        request,
        'history.html',
        context
    )


def patient_detail(request, patient_id):

    patient = get_object_or_404(
        Patient,
        id=patient_id
    )

    context = {
        'patient': patient
    }

    return render(
        request,
        'patient_detail.html',
        context
    )


def metrics(request):

    context = {
        'metrics': METRICS
    }

    return render(
        request,
        'metrics.html',
        context
    )


def about(request):

    return render(
        request,
        'about.html'
    )