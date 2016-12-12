from django.db import models
from deuacademy.settings import CUR, connection
from IPython import embed
# Create your models here.



class Courses(models.Model):
    

    def course_list():
        CUR.callproc('list_course')
        connection.commit()
        course = CUR.fetchall()
        return course
    def select_course(pk):
        CUR.callproc('select_course',[pk,])
        connection.commit()
        course = CUR.fetchone()
        return course
    def insert_course(liste):
        CUR.callproc('insert_course',liste)
        connection.commit()
    def delete_course(pk):
        CUR.callproc('delete_course',[pk,])
        connection.commit()
    def update_course(liste):
        CUR.callproc('update_course',liste)
        connection.commit()
    