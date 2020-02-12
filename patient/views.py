from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.contrib import messages
from hospital.models import Hospital
from helpers import search_results, get_data, build_time_slots, get_slots


def new_appointment(request):
    context = {
        'user': request.user
    }
    if(request.GET.get('search', None) is not None):
        query = request.GET.get('search')
        context['results'] = search_results(query)
        context['query'] = query

    return render(request, 'patient/new.html', context)


def select_slot(request):
    if request.method == 'POST':
        doctor_id = request.POST.get('doctor_id')
        hospital_id = request.POST.get('hospital_id')
        specialization_id = request.POST.get('specialization_id')

        if(not doctor_id or not hospital_id or not specialization_id):
            return JsonResponse({'error': 'Incorrect parameters'})
        request.session['booking'] = {
            'doctor_id': doctor_id,
            'hospital_id': hospital_id,
            'specialization_id': specialization_id
        }
        return redirect('app:patient:select_slot')
    context = request.session['booking']
    return render(request, 'patient/slot.html', context)


def payment(request):
    return render(request, 'patient/payment.html')


def patient_appointments(request):
    return render(request, 'patient/appointments.html')


def patient_profile(request):
    if(request.method == 'POST'):
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        mobile = request.POST.get('mobile')
        user = request.user
        user.first_name = first_name
        user.last_name = last_name
        user.mobile = mobile
        user.save()
        messages.success(request, 'Profile details have been updated')
    context = {
        'user': request.user
    }
    return render(request, 'patient/profile.html', context)


def search_results_json(request):
    query = request.GET.get('query', '')
    return JsonResponse(search_results(query), safe=False)


def get_data_json(request):
    return JsonResponse(get_data(request.GET.get('query'), request.GET.get('obj_type')))


def index(request):
    return render(request, 'patient/index.html')


def get_slots_json(request):
    hospital_id = request.GET.get('hospital_id')
    doctor_id = request.GET.get('doctor_id')
    date = request.GET.get('date')
    if(not hospital_id or not doctor_id):
        return JsonResponse({
            'error': 'Missing parameters. Provide hospital_id and doctor_id'
        })
    slots = get_slots(hospital_id, doctor_id, date)
    return JsonResponse(slots, safe=False)
