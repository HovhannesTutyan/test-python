import json

json
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from main.models import StudentData

def HomePage(request):
    students = StudentData.objects.all()
    return render(request,"main/homepage.html", {'students':students})
@csrf_exempt
def InsertStudent(request):
    name=request.POST.get('name')
    email=request.POST.get('email')
    gender=request.POST.get('gender')

    try:
        student=StudentData(name=name, email=email, gender=gender)
        student.save()
        student_data={'id':student.id, 'created_at':student.created_at, "error":False, 'errorMessage':'Student Added Successfully'}
        return JsonResponse(student_data, safe=False)
    except:
        student_data={'error':True, 'errorMessage':'Failed to Add'}
        return JsonResponse(student_data, safe=False)

@csrf_exempt  #request works without csrf_token
def update_all(request):
    data = request.POST.get("data")
    dict_data = json.loads(data) #calling json_loads(json_string) method to convert json to dictionary.
    # print(dict_data[0]['id'])
    try:
        for dict_single in dict_data:
            student = StudentData.objects.get(id=dict_single['id'])
            student.name = dict_single['name']
            student.email = dict_single['email']
            student.gender = dict_single['gender']
            student.save()
        student_data = {"error":False, "errorMessage":"Updated Successfully"}
        return JsonResponse(student_data, safe=False)
    except:
        student_data = {"error":True, "errorMessage":"Failed to upload data"}
        return JsonResponse(student_data, safe=False)

@csrf_exempt
def delete_data(request):
    id=request.POST.get("id")
    try:
        student = StudentData.objects.get(id=id)
        student.delete()
        student_data = {"error": False, "errorMessage": "Deleted Successfully"}
        return JsonResponse(student_data, safe=False)
    except:
        student_data = {"error": True, "errorMessage": "Failed to delete data"}
        return JsonResponse(student_data, safe=False)

