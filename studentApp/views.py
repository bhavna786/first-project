from django.shortcuts import render
from django.http import HttpResponse
from .models import Student

# Create your views here.
def student_show(request):
	# x = []
	# for i in range(10):		
	# 	x.append(i)
	# print('hi how are \
	# 	you')
	# a = 34;print(a)		
	# b = "hello"
	# print('hey %s your value is %s' %(a,b))	
	# print("hi daivik {0} are you {1}".format(a,b))

	# return HttpResponse("<h1> Data Flair Django Tutorials</h1> The Digits are {0}".format(x))	

	student = Student.objects.order_by('roll_no')
	return render(request,'student_show.html',{'student':student})









	


