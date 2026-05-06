from django.shortcuts import render
from .models import Doctor
# Create your views here.

def doctor_list(request):
    query = request.GET.get('q')
    if query : 
        doctors = Doctor.objects.filter(
            name__icontains = query
        ) | Doctor.objects.filter(
            specialization__name__icontains = query
        ) | Doctor.objects.filter(
            location__icontains = query
        )
    else : 
        doctors = Doctor.objects.all()

    context = {'doctors' : doctors,'search_term' : query}
    return render(request,'doctors/doctor_list.html',context)