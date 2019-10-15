from django.shortcuts import render
from django.http import JsonResponse
# Create your views here.
from api.tasks import send_email

def home(request):
    test = {'value': 'True'}
    mytask = send_email.apply_async()
    
    # import pdb; pdb.set_trace()
    # if mytask.status == 'SUCCESS':
    #     return 'True'
    # import pdb; pdb.set_trace()
    data = {
        'name': 'Vitor',
        'location': 'Finland',
        'is_active': True,
        'count': 28
    }
    return JsonResponse(data)
    