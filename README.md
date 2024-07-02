Django Project steps

## For starting Server
********>python manage.py runserver
         Press Ctr +C to exit from runnig server

*Create Django Project: django-admin startproject project_name
*Change directory to Django Project : cd project_name
*Create Django Application : python manage.py startapp application_name
*Add/Install Application to Django Project(application_name to Project_name)
 *Open settings.py 
 *Add application_name
     INSTALLED_APPS=['django.contrib.admin'.'course']
 * Save settings.py

*Write view function inside Application Views.py
   *Open view.py
   *Import HttpResponse class from django.htt module
      *from django.http import HttpResponse
   *Write view Function
      def learn_django(request):
         return HttpResponse("Hello Django")

* save views.py file

#then define the url in inner project urls.py file
#import view file
from application_name import Views
  *path('djangodj',views.learn_django)   #here djangodj is a ulr when we hit this url in web brwser it will
                                          rediirect to learn_django function and show in a web  page hello Django


#for Home url

Write a view function in view.py
   def index(request);
     return HttpResponse("Hello Home Page")

in urls.py set url
   path(' ',views.index)