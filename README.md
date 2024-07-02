Django Project steps<br/>

## For starting Server<br/>
********>python manage.py runserver<br/>
         Press Ctr +C to exit from runnig server<br/>

*Create Django Project: django-admin startproject project_name<br/>
*Change directory to Django Project : cd project_name<br/>
*Create Django Application : python manage.py startapp application_name<br/>
*Add/Install Application to Django Project(application_name to Project_name)<br/>
 *Open settings.py <br/>
 *Add application_name<br/>
     INSTALLED_APPS=['django.contrib.admin'.'course']<br/>
 * Save settings.py<br/>

*Write view function inside Application Views.py<br/>
   *Open view.py<br/>
   *Import HttpResponse class from django.htt module<br/>
      *from django.http import HttpResponse<br/>
   *Write view Function<br/>
      def learn_django(request):<br/>
         return HttpResponse("Hello Django")<br/>

* save views.py file<br/>

#then define the url in inner project urls.py file<br/>
#import view file<br/>
from application_name import Views<br/>
  *path('djangodj',views.learn_django)   #here djangodj is a ulr when we hit this url in web brwser it will<br/>
                                          rediirect to learn_django function and show in a web  page hello<br/> Django<br/>


#for Home url<br/>

Write a view function in view.py<br/>
   def index(request);<br/>
     return HttpResponse("Hello Home Page")<br/>

in urls.py set url<br/>
   path(' ',views.index)<br/>