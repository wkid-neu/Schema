from django.shortcuts import render
import json


# Create your views here.
def map_index(request):
    if request.session.get('is_login', None):
        return render(request, "display/address.html")

    else:
        return render(request, "login/nologin.html")


def enter(request):
    return render(request, "display/enter.html")

def form(request):
    return render(request,"display/form.html")

def test(request):
    address_point = address_info.objects.all()
    address_longitude = []
    address_latitude = []
    address_data = []
    for i in range(len(address_point)):
        address_longitude.append(address_point[i].longitude)
        address_latitude.append(address_point[i].latitude)
        address_data.append(address_point[i].data)

    return render(request, 'display/address.html',
                  {'address_longitude': json.dumps(address_longitude),
                   'address_latitude': json.dumps(address_latitude), 'address_data': json.dumps(address_data)})
