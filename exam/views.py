




import bcrypt
from django.shortcuts import  redirect, render 
from django.contrib import messages

from .models import *
# Create your views here.


def main(request):
    # context={
    # "all":User.objects.all()
    # }
    return render(request,"login.html")

def dashbord(request):
    if 'userid' in request.session:
        # add=
        context={
            'trees':Trees.objects.all(),
            # 'adder':add
            'user':User.objects.get(id=request.session['userid'])
        }
        return render(request,'dashbord.html',context)
    else:
        return render(request,"massege.html")


def regist(request):

    errors = User.objects.basic_validator(request.POST)

    for key, value in errors.items():
        messages.error(request, value)
        return redirect('/')
    else:
        first_name=request.POST['firstname']
        last_name =request.POST['lastname']
        email=request.POST['email']
        password=request.POST['pass']
        pw_hash=bcrypt.hashpw(password.encode(),bcrypt.gensalt()).decode()
        confirm_PW=request.POST['confirm']

        User.objects.create(first_name=first_name,last_name=last_name,email=email,password=pw_hash,confirm_PW=confirm_PW)
        user1=User.objects.last()
        request.session['email']=request.POST['email']
        request.session['pass']=pw_hash
        request.session['userid']=user1.id

        return redirect("/")

def mytree(requset):

    user=User.objects.get(id=requset.session['userid'])
    context={
        'user':user,
        'useruploder':user.added_by.all()
    }
    return render(requset,'mytrees.html',context)

def login(request):
    user=User.objects.filter(email=request.POST['email1'])
    if user :
        logged_user=user[0]
        # request.session['user']=User.objects.filter(email=request.POST['email1'])
        # to get user by email ...
        if bcrypt.checkpw(request.POST['pass1'].encode(),logged_user.password.encode()):
            request.session['userid']=logged_user.id
            return redirect("/dashbord")
        else:
            
            return render(request,"massege.html")
    
    return render(request,"massege.html")

def details(requset,id):
    user=User.objects.get(id=requset.session['userid'])
    tree=Trees.objects.get(id=id)
    context={
        'user':user,
        'tree':tree,
        'vistor':tree.visetors.all(),
        'last':tree.visetors.last()
    }
    return render(requset,'details.html',context)

def addvistor(request,id):
    user=User.objects.get(id=request.session['userid'])
    tree=Trees.objects.get(id=id)
    tree.visetors.add(user)
    return redirect('/details/'+str(id))

def edit(request,id):
    context={
        'user':User.objects.get(id=request.session['userid']),
        'tree':Trees.objects.get(id=id)
    }
    return render(request,'edit.html',context)


def update(request,id):
    tree=Trees.objects.get(id=id)
    tree.specise=request.POST['pecise1']
    tree.location=request.POST['location1']
    tree.reason=request.POST['reason1']
    tree.created_at=request.POST['date1']
    tree.save()
    return redirect('/mytree')


def delete(request,id):
    user=User.objects.get(id=request.session['userid'])
    c=Trees.objects.get(id=id)
    c.delete()

    return redirect('/dashbord')

def addtree(request):
    context={
        'user':User.objects.get(id=request.session['userid'])
    }
    return render(request,'planttree.html',context)

    
def forplantree(request):

    user=User.objects.get(id=request.session['userid'])
    Trees.objects.create(specise=request.POST['pecise'],
    location=request.POST['location'],reason=request.POST['reason'],addedby=user,created_at=request.POST['date'])

    return redirect('/dashbord')


def logout (request):
    del request.session['userid']

    return redirect('/')

# def books(request):
#     context={
#         'user':User.objects.get(id= request.session['userid']),
#         'books':Book.objects.all()
#         # 'cd':
#     }
#     return render(request,"books.html",context)

# def favoritbook(request):
#     errors = Book.objects.basic(request.POST)
#     if len(errors) > 0 :
#         for key, value in errors.items():
#             messages.error(request, value)
#         return redirect('/books')
#     else:
#         user=User.objects.get(id=request.session['userid'])
#         Book.objects.create(title=request.POST['title'],desc=request.POST['desc'],uploder=user)
#         Book.objects.get(title=request.POST['title']).userlike.add(user)
#         return redirect("/books")

# def loggedin(request):

#     if request.session['userid']:
#         return redirect("/first")        
#     else:
#         return redirect('/')

# def addtofav(request,id):

#     user=User.objects.get(id=request.session['userid'])
#     Book.objects.get(id=id).userlike.add(user)

     
#     return redirect("/books")


# def bookshow(request,id):
#     context={

#         'show': Book.objects.get(id=id),
#         'user':User.objects.get(id= request.session['userid']),
        

#     }
#     return render(request,"bookshow.html",context)

# def addtofavsho(request,id):
#     user=User.objects.get(id=request.session['userid'])
#     Book.objects.get(id=id).userlike.add(user)

     
#     return redirect("/bookshow/"+str(id))



# def delfav(request,id):
#     s=User.objects.get(id=request.session['userid'])
#     Book.objects.get(id=id).userlike.remove(s)
#     return redirect('/bookshow/'+str(id))


# def edit(request):
#     # user=Book.objects.get(id=id).update(title=request.POST['uptitle'],desc=request.POST['descrip'])
#     if request.POST['edit']=='update':
#         bo=Book.objects.get(id=request.POST['hid'])
#         bo.title=request.POST['uptitle']
#         bo.desc=request.POST['descrip']
#         bo.save()
#         return redirect('/bookshow/'+str(request.POST['hid']))

#     elif request.POST['edit']=='delete':
#         user=Book.objects.get(id=request.POST['hid'])
#         user.delete()
#         return redirect('/books')




# def goback(reqeast):
#     return redirect('/')

# def showall(request):
#     u=User.objects.get(id=request.session['userid'])
#     context={
#         'user':User.objects.get(id=request.session['userid']),
        
#         'var1':u.likedbooks.all(),
#         # 'd': r.userlike.all(),
#         'showallb':Book.objects.all() 
#     }
#     return render(request,"showall.html",context)




# def gotobooks(request):
#     return redirect("/books")





# def success(request):
#     if 'userid' in request.session:
#         context={
#             'name1':User.objects.last()
#         }
#         return render(request,"result.html",context)
#     else:
#         return redirect('/')