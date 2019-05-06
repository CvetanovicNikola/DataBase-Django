
from django.shortcuts import render
from django.http import HttpResponse
from django.http import Http404
from django.http import HttpResponseNotFound
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from . models import Employee
from . serialize import EmployeeSerializer
from rest_framework.decorators import api_view


""" class EmployeeList(APIView):

    def get(self, request):
        employees = Employee.objects.all()
        serializer = EmployeeSerializer(employees, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = EmployeeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request):
        employee = Employee.objects.get()
        employee.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)



class EmployeeDetail(APIView):

    def get(self, request, lastname):
        try:
            employee = Employee.objects.filter(lastname=lastname)
            serializer = EmployeeSerializer(employee, many=True)
            return Response(serializer.data)
        except Employee.DoesNotExist:
            return HttpResponseNotFound("Employee not found")

    def post(self, request):
        serializer = EmployeeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, lastname):
        employee = Employee.objects.get(lastname=lastname)
        employee.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    def put(self, request, lastname):
        employee = Employee.objects.get(lastname=lastname)
        serializer = EmployeeSerializer(employee, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

 """
""" @api_view(['GET'])
def get_lastname(request):
    if request.method == 'GET':
        lastname = request.GET.get("lastname")
        try:
            employee = Employee.objects.filter(lastname=lastname)
            serializer = EmployeeSerializer(employee, many=True)
            return Response(serializer.data)
        except Employee.DoesNotExist:
            return HttpResponseNotFound("Employee not found")
    else:
        search(request) """


@api_view(['GET'])
def get_lastname(request):
    if request.method == 'GET':
        lastname = request.GET.get("lastname").capitalize()
        return get_employee(request, lastname)
    else:
        return search(request)


def get_employee(request, lastname):
    try:
        employee = Employee.objects.filter(lastname=lastname)
        if employee.count() == 0:
            return render(request, "not_found.html")
    except Employee.DoesNotExist:
        return render(request, "not_found.html")
    return render(request, "employee.html", {"employee": employee})


def view_all_employees(request):
    employees = Employee.objects.all()
    return render(request, "all_employees.html", {"employees": employees})


def home(request):
    return render(request, "home.html")


def insert(request):
    return render(request, "insert.html")


def search(request):
    return render(request, "search.html")
