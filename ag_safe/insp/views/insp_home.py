from django.shortcuts import render, redirect
from ..models import Inspections, User, Facility, Type

# HOME PAGE


def home_page(request):
    inspection_data = {}
    if 'username' in request.session:
        inspection_data['session_username'] = request.session.get('username')
        inspection_data['session_name'] = request.session.get('name')
        inspection_data['session_role'] = request.session.get('role')
        inspection_data['session_dir'] = request.session.get('ins_dir')
    else:
        inspection_data['session_username'] = ''
        return redirect('login')
    username = request.session.get('username')
    user_id = request.session.get('user_id')
    role = request.session.get('role')
    inspection_data['locations'] = []
    if role == 1:
        inspection = Inspections.objects.filter(supervisor=username)
    else:
        inspection = Inspections.objects.filter(user_id=user_id)
    for ins_data in inspection:
        inspection_data['locations'].append(ins_data.location)
    inspection_data['locations'] = list(dict.fromkeys(inspection_data['locations']))
    facility = Facility.objects.all()
    inspection_data['facility_data'] = facility
    ins_type = Type.objects.all()
    inspection_data['inspection_type'] = ins_type
    supervisor = User.objects.filter(role_id='1')
    inspection_data['supervisor_data'] = supervisor
    inspection_data['inspections'] = inspection
    users = User.objects.all()
    inspection_data['users'] = users
    return render(request, 'insp_module/inspection.html', inspection_data)

