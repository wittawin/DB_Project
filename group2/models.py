#-*- coding: utf-8 -*-
from django.db import models
from login.models import *


class Department(models.Model):
    #code
    Department_ID = models.IntegerField(primary_key=True, max_length=10)
    Department_Name = models.CharField( max_length=100 )
    def __unicode__(self):
        return str(self.Department_ID )+"  "+  str(self.Department_Name )

class Course(models.Model):
    #code
    Course_ID = models.IntegerField(primary_key=True, max_length=10)
    Course_Name = models.CharField( max_length=100 )
    Department_ID = models.ForeignKey(Department)
    Credit = models.CharField( max_length=10 )
    Describe = models.CharField( max_length=1000, blank=True )
    def __unicode__(self):
        return str(self.Course_ID )
	
class Section(models.Model):
    Section = models.IntegerField(max_length=10)
    Course_ID = models.ForeignKey(Course)
    classroom = models.CharField(max_length=20)
    st_endTime = models.CharField(max_length=11)
    Teacher_ID = models.ForeignKey(Teacher)
    
    dateChoices = (
    ('M', 'Monday'),
    ('T', 'Tuesday'),
    ('W', 'Wednesday'),
    ('H', 'Thursday'),
    ('F', 'Friday'),
    ('S', 'Saturday')
    )
    date = models.CharField(max_length=1, choices=dateChoices)
    def __unicode__(self):
        return " Course "+str(self.Course_ID )+" Section "+str(self.Section)+" Time "+  str(self.st_endTime)+"  Teacher_ID "+  str(self.Teacher_ID)
	
class Grade(models.Model):
    #code
    std_id = models.ForeignKey(Student)
    Course_ID = models.ForeignKey(Course)
    year        = models.IntegerField(max_length=10)
    term        = models.IntegerField(max_length=1)
    gradeChoices = (
    ('0', ' '),
    ('1', 'A'),
    ('2', 'B+'),
    ('3', 'B'),
    ('4', 'C+'),
    ('5', 'C'),
    ('6', 'D+'),
    ('7', 'D'),
    ('8', 'F'),
    ('9', 'Fa'),
    ('10', 'Fe'),
    ('11', 'S'),
    ('12', 'U'),
    ('13', 'I'),
    ('14', 'Ip'),
    ('15', 'W'),
    ('16', 'AUD'),
    )
    Grade = models.CharField( max_length=3, choices=gradeChoices , default = '0')
    Section = models.ForeignKey(Section)
    def __unicode__(self):
        return "Student "+str(self.std_id )+" Course "+str(self.Course_ID )+" Section "+str(self.Section)+" Year "+  str(self.year)+"  Term "+  str(self.term)



class Teacher_Course(models.Model):
    #code
    shortname = models.ForeignKey(Teacher)
    Course_ID = models.ForeignKey(Course)
    Section = models.ForeignKey(Section)
    def __unicode__(self):
        return str(self.shortname  )+"  "+  str(self.Course_ID )+"  "+  str(self.Section )

	
class scheme(models.Model):
    Course_ID = models.ForeignKey(Course)
    schemeChoices = (
    ('0', 'ไม่มีในหลักสูตร'),  
    ('1', 'ปริญญาโท_หลักสูตร2ปี_แผน_ก_เเบบ_ก_2_ปกติ'),
    ('2', 'ปริญญาโท_หลักสูตร2ปี_แผน_ก_เเบบ_ก_2_สหกิจศึกษา'),
    ('3', 'ปริญญาเอก_หลักสูตร3ปี_แบบ_1.1'),
    ('4', 'ปริญญาเอก_หลักสูตร3ปี_แบบ_2.1'),
    ('5', 'ปริญญาเอก_หลักสูตร4ปี_แบบ_1.2'),
    ('6', 'ปริญญาเอก_หลักสูตร4ปี_แบบ_2.2')
    )
    scheme = models.CharField(max_length=1, choices=schemeChoices)
    def __unicode__(self):
        return str(self.Course_ID)+"  "+  str(self.scheme)
		
class viyanipon_adviser(models.Model):
    #code
    std_id = models.CharField(primary_key=True, max_length=13)
    teach_name = models.CharField(max_length=6)
    adviser = models.CharField(max_length=50)
    def __unicode__(self):
        return str(self.std_id)+"  "+  str(self.adviser)
		
class viyanipon_name(models.Model):
    std_id = models.CharField(primary_key=True, max_length=13)
    viyaniponh_name = models.CharField(max_length=6)
    name_thai = models.CharField(max_length=200)
    name_eng = models.CharField(max_length=200)
    def __unicode__(self):
        return str(self.std_id)+"  "+  str(self.name_eng)


class viyanipon_project(models.Model):
    std_id = models.CharField(primary_key=True, max_length=13)
    project_name = models.CharField(max_length=6)
    name_day = models.IntegerField(max_length=2)
    name_month = models.CharField(max_length=50)
    name_year = models.IntegerField(max_length=4)
    def __unicode__(self):
        return str(self.std_id)+"  "+  str(self.name_day)+"  "+  str(self.name_month)+"  "+  str(self.name_year)
		
class viyanipon_test(models.Model):
    std_id = models.CharField(primary_key=True, max_length=13)
    test = models.CharField(max_length=6)
    test_day = models.IntegerField(max_length=2)
    test_month = models.CharField(max_length=50)
    test_year = models.IntegerField(max_length=4)
    def __unicode__(self):
        return str(self.std_id)+"  "+  str(self.test_day)+"  "+  str(self.test_month)+"  "+  str(self.test_year)
		
class viyanipon_testend(models.Model):
    std_id = models.CharField(primary_key=True, max_length=13)
    testend = models.CharField(max_length=6)
    testend_day = models.IntegerField(max_length=2)
    testend_month = models.CharField(max_length=50)
    testend_year = models.IntegerField(max_length=4)
    def __unicode__(self):
        return str(self.std_id)+"  "+  str(self.testend_day)+"  "+  str(self.testend_month)+"  "+  str(self.testend_year)