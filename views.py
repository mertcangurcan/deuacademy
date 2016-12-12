from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.generic import View
from .models import Courses
from IPython import embed


# Create youer views here.

class Courses_view(View):
    def get(self,request):
        courses = Courses.course_list()
        course_list = []
        for course in courses:
            course = {'finish_date':course[0],'description': course[1], 'duration': course[2],'start_date': course[3], 'id':course[4],'coursename':course[5] }
            course_list.append(course)
        
        return render(request, 'courses/index.html',{'courses': course_list})
    def post(self,request):
        
        params = request.POST
        parameters = [params['finishdate'],params['description'],params['duration'],params['startdate'],params['coursename']]
        Courses.insert_course(parameters)

        return redirect('/academy/courses')


def delete_course(request,pk):
    Courses.delete_course(pk)
    return redirect('/academy/courses/')


def edit_course(request,pk):
    if request.method == 'GET':
        course = Courses.select_course(pk) 
        start_date = '%s-%s-%s' % (course[3].year, course[3].month, course[3].day)
        finish_date = '%s-%s-%s' % (course[0].year, course[0].month, course[0].day)
        course = {'finish_date':finish_date ,'description': course[1], 'duration': course[2],'start_date': start_date, 'id':course[4],'coursename':course[5] }
        return render(request, 'courses/form_edit.html', {'course':course})
    elif request.method == 'POST':
        params = request.POST
        parameters = [params['course_id'], params['finishdate'],params['description'],params['duration'],params['startdate'],params['coursename']]
        Courses.update_course(parameters)
        return redirect('/academy/course/%s' % pk)

def course(request,pk):
    course = Courses.select_course(pk)
    course = {'finish_date':course[0],'description': course[1], 'duration': course[2],'start_date': course[3], 'id':course[4],'coursename':course[5] }
    return render(request, 'courses/course.html',{'course': course})

def form(request):
    return render(request, 'courses/form.html')






""""

EXAMPLE CODE OF SIMPLE HTML RENDERING

# def index(request):
#     latest_question_list = Question.objects.order_by('-pub_date')[:5]
#     template = loader.get_template('polls/index.html')
#     context = {
#         'latest_question_list': latest_question_list,
#     }
#     return HttpResponse(template.render(context, request))

"""