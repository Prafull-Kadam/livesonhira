from django.shortcuts                      import render
from django.contrib.auth.decorators        import login_required
from django.contrib.admin.views.decorators import staff_member_required
from django_app.models import profile
from django_app.forms  import profileforms
from uuid              import uuid4
from os                import path
from sample_project    import settings
from random            import choice
import requests
from django.core.urlresolvers       import reverse
from django.views.decorators.csrf   import csrf_exempt
from django.views.generic.edit      import FormView
from django.views.generic.base      import View


# Create your views here.
def login(request):
    return render(request, 'login.html')

def indexpage(request):
    return render(request, 'indexpage.html')

def biography(request):
    return render(request, 'biography.html')

@login_required
def profilepage(request):
    if not request.user.is_staff:
        return render(request, 'lockscreen.html')
    else:
        obj = profile.objects.all()
        return render(request, 'profilepage.html',{'msg_count': obj.count(), 'video_count': '7'})

@login_required
def messageDelete(request, id):
    if not request.user.is_staff:
        return render(request, 'lockscreen.html')
    else:
        try:
            if id.isalpha:
                id = int(id)
            obj = profile.objects.get(id=id)
            obj.delete()
        except:
            pass 
        obj = profile.objects.all()
        details = [obj.profile_details() for obj in profile.objects.all()][::-1]      
        return render(request, 'cards-view.html', {'details': details})

@login_required
def desplay_message(request):
    if request.method == 'GET':
        obj = profile.objects.all()
        details = [obj.profile_details() for obj in profile.objects.all()][::-1]
        return render(request, 'cards-view.html', {'details': details})
    else:
        return render(request, 'lockscreen.html')

def makewish(request):
    return render(request, 'form.html', {'message': 'Upload Birthday Wishes'})

def videos(request):
    return render(request, 'videos.html')

def user_validator(data):
    if not data['fname'].strip():
        return False, "First name mandatory"

    if not data['lname'].strip():
        return False, "Last name mandatory"

    if data['mobile_no'].strip():
        if data['mobile_no'].strip() in [obj.mobile_no for obj in profile.objects.all()][::-1]:
            return False, "Mobile number already registered, Please try with another number"
        elif len(data['mobile_no'].strip()) != 10 or not data['mobile_no'].strip().isdigit():
            return False, "Invalid mobile number:"+str(data['mobile_no'].strip())+", try again"
        else:
            return True, ""
    else:
        return False, "Mobile number mandatory"
    

def upload_file(request):
    if request.method == 'POST':
        data = request.POST.copy()
        status, msg = user_validator(data)
        if not status:
            return render(request, 'form.html', {'message': msg, 'data': data})
        pic_path = None
        if 'picture' in request.FILES:
            pic = request.FILES['picture'].read()
            pic_path = "/static/images/uploads/"+str(uuid4())+'.jpg'
            open(path.join('django_app', pic_path.lstrip('/')), 'wb').write(pic)

        
        obj = profile()
        if data['fname'].strip():
            obj.first_name = data['fname']
            obj.last_name  = data['lname']
            obj.city       = data['city']
            obj.taluka     = data['taluka']
            obj.district   = data['district']
            obj.message    = data['message']
            obj.mobile_no  = data['mobile_no']
            obj.email      = data['email']
            obj.picture    = pic_path
            obj.save()
            if data['fname'].isalpha():
                lang = "eng"
            else:
                lang = "mr"

            return render(request, 'thanks.html', {'lang': lang, 'name': data['fname'], 'number': choice([1,2,3])})
        else:
            return render(request, 'form.html', {'message': 'Upload Birthday Wishes '})
    else:
        return render(request, 'form.html', {'message': 'Upload Birthday Wishes '})

