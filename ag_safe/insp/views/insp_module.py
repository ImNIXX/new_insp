from django.core.files import File
from django.core.serializers import json
from django.http import HttpResponse, JsonResponse
from ..models import Inspections, Type
from datetime import date
import os
import os.path
import time
from pathlib import Path
from django.conf import settings

# INSPECTION INSERT


def insert_inspection(request):
    inspection_title = request.POST.get('inspection_title', None)
    facility = request.POST.get('facility', None)
    stakeholders = request.POST.get('stakeholders', None)
    inspection_type = request.POST.get('inspection_type', None)
    location = request.POST.get('location', None)
    category = request.POST.get('category', None)
    operating_area = request.POST.get('operating_area', None)
    supervisor = request.POST.get('supervisor', None)
    user_id = request.session.get('user_id')
    inspection_add = Inspections(title=inspection_title, facility=facility, stakeholders=stakeholders, type=inspection_type, location=location, category=category, operating_area=operating_area, datetime=date.today(), status='0', user_id=user_id, supervisor=supervisor )
    inspection_add.save()
    inspection_data = {'id': inspection_add.id, 'type': inspection_add.type, 'date': inspection_add.datetime, 'title': inspection_add.title, 'location': inspection_add.location, }
    return JsonResponse(inspection_data)

# GET INSPECTION DATA


def get_inspection(request):
    inspection_id = request.POST.get('inspection_id', None)
    inspection_id = int(inspection_id) / 9304
    inspections = Inspections.objects.get(id=inspection_id)
    inspection_data = {'id': inspections.id, 'title': inspections.title, 'facility': inspections.facility, 'stakeholders': inspections.stakeholders, 'type': inspections.type, 'location': inspections.location, 'category': inspections.category, 'operating_area': inspections.operating_area, 'supervisor': inspections.supervisor, 'approve': inspections.approve}
    return JsonResponse(inspection_data)

# UPDATE INSPECTION DATA


def update_inspection(request):
    inspection_id = request.POST.get('inspection_id', None)
    inspection_id = int(inspection_id)/9304
    inspection_title = request.POST.get('title', None)
    facility = request.POST.get('facility', None)
    stakeholders = request.POST.get('stakeholders', None)
    inspection_type = request.POST.get('type', None)
    location = request.POST.get('location', None)
    category = request.POST.get('category', None)
    operating_area = request.POST.get('operating_area', None)
    supervisor = request.POST.get('supervisor', None)
    # GET INSPECTION
    ins_data = Inspections.objects.get(id=inspection_id)
    if ins_data.type == inspection_type:
        insp_type = '0'
    else:
        insp_type = '1'
    if ins_data.approve != 'true':
        update_data = Inspections.objects.filter(id=inspection_id).update(title=inspection_title, facility=facility, stakeholders=stakeholders, type=inspection_type, location=location, category=category, operating_area=operating_area, supervisor=supervisor)
        ins_data = Inspections.objects.get(id=inspection_id)
        inspection_data = {'id': ins_data.id, 'title': ins_data.title, 'facility': ins_data.facility, 'stakeholders': ins_data.stakeholders, 'type': ins_data.type, 'location': ins_data.location, 'category': ins_data.category, 'operating_area': ins_data.operating_area, 'supervisor': ins_data.supervisor, 'insp_type_status': insp_type, 'status': 'inspection update'}
        if update_data:
            return JsonResponse(inspection_data)
    else:
        inspection_data = {'status': 'inspection approved'}
        return JsonResponse(inspection_data)

# DRAFT DATA


def drafts(request):
    draft_id = request.POST.get('draft_id', None)
    draft_data = Type.objects.get(id=draft_id)
    draft_html = {'draft_name': draft_data.type, 'draft_html': draft_data.draft_html, 'draft_slug': draft_data.type_slug}
    return JsonResponse(draft_html)


def insert_draft(request):
    inspection_id = request.POST.get('inspection_id', None)
    inspection_id = int(inspection_id)/9304
    draft_html = request.POST.get('draft_html', None)
    draftname = request.POST.get('draftname', None)
    draft_name = request.POST.get('inspection_type', None)
    ins_data = Inspections.objects.get(id=inspection_id)
    if ins_data.draft_name != '':
        print(inspection_id)
        ins_dir = ins_data.draft_directory
        draft_name = ins_data.draft_slug
        draft_file = settings.MEDIA_ROOT + "/insp_draft_dir/" + ins_dir + "/" + draft_name
        os.remove(draft_file)
    ts = int(time.time())
    file_name = str(ts)+draft_name+'.html'
    ins_dir = request.session['ins_dir']
    path_name = settings.MEDIA_ROOT + "/insp_draft_dir/"+ins_dir
    with open(path_name+"/"+str(ts)+draft_name+'.html', 'w') as f:
        myfile = File(f)
        myfile.write(draft_html)
    myfile.closed
    f.closed
    Inspections.objects.filter(id=inspection_id).update(draft_slug=file_name, draft_directory=ins_dir, draft_name=draftname)
    insp_data = Inspections.objects.get(id=inspection_id)
    insp_draft = {'draft_name': insp_data.draft_name, 'draft_slug': insp_data.draft_slug,'draft_dir': insp_data.draft_directory}
    return JsonResponse(insp_draft)


def update_draft(request):
    inspection_id = request.POST.get('inspection_id', None)
    inspection_id = int(inspection_id) / 9304
    draft_html = request.POST.get('draft_html', None)
    ins_data = Inspections.objects.get(id=inspection_id)
    print(ins_data.approve)
    if ins_data.approve != 'true':
        draft_slug = ins_data.draft_slug
        ins_dir = request.session['ins_dir']
        path_name = settings.MEDIA_ROOT + "/insp_draft_dir/" + ins_dir
        with open(path_name + "/" + draft_slug, 'w') as f:
            myfile = File(f)
            myfile.write(draft_html)
        myfile.closed
        f.closed
        return HttpResponse('update')
    else:
        return HttpResponse('approved')


# DELETE INSPECTION


def delete_inspection(request):
    inspection_id = request.POST.get('inspection_id', None)
    inspection_id = int(inspection_id) / 9304
    ins_data = Inspections.objects.get(id=inspection_id)
    if ins_data.approve != 'true':
        ins_dir = ins_data.draft_directory
        draft_name = ins_data.draft_slug
        draft_file = settings.MEDIA_ROOT + "/insp_draft_dir/"+ins_dir+"/"+draft_name
        my_file = Path(draft_file)
        if my_file.is_file():
            os.remove(draft_file)
        del_data = Inspections.objects.filter(id=inspection_id).delete()
        if del_data[0] == 1:
            return HttpResponse('1')
        else:
            return HttpResponse('0')
    else:
        return HttpResponse('0')


# INSPECTION APPROVE

def insp_approve(request):
    insp_id = request.POST.get('insp_id')
    insp_approve = request.POST.get('insp_approve')
    inspection_id = int(insp_id) / 9304
    Inspections.objects.filter(id=inspection_id).update(approve=insp_approve)
    return HttpResponse('Hello')


# INSPECTION SEARCH


def insp_search(request):
    search_key = request.POST.get('search_key', None)
    insp_data = Inspections.objects.filter(title__contains=search_key)
    print(insp_data.count())
    insp_response = {}
    for i in range(insp_data.count()):
        insp_response[i] = {'title': insp_data[i].title, 'date': insp_data[i].datetime, 'category': insp_data[i].category, 'draft_name': insp_data[i].draft_name}
    return JsonResponse(insp_response)


# INSPECTION FILTER

def insp_filter(request):
    operating_area = request.POST.get('operating_area', None)
    facility = request.POST.get('facility', None)
    location = request.POST.get('location', None)
    category = request.POST.get('category', None)
    type = request.POST.get('type', None)
    filter_data = {'operating_area': operating_area, 'facility': facility, 'location': location, 'category': category, 'type': type}
    asd = list(dict.fromkeys(filter_data))
    print(asd)
    return HttpResponse('Hello')