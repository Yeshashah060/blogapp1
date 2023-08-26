from django.shortcuts import render
from django.http import HttpResponse,HttpRequest
from.models import blog
# Create your views here.
def frontpage(request):
	return render(request,'front.html')

def homepage(request):
	return render(request,'home.html')

def addblog(request):
	return render(request,'addblog.html')

def savedata(request):
	bname = request.GET.get("bname")
	bb = request.GET.get("bb")

	b=blog(bname=bname,bb=bb)
	b.save()

	data = blog.objects.all()
	return render(request,'displayblog.html',{'data':data})


def displayblog(request):
	data = blog.objects.all()
	return render(request,'displayblog.html',{'data':data})

def deleteblog(request):
	id=request.GET['id']
	data = blog.objects.get(id=id)
	data.delete()
	data = blog.objects.all()
	return render(request,'displayblog.html',{'data':data})

def editblog(request):
	id=request.GET['id']
	data = blog.objects.get(id=id)
	return render(request,'edit.html',{'data':data})

def saveeditdata(request):
	id = request.GET['id']
	data = blog.objects.get(id=id)

	data.bname = request.GET['bname']
	data.bb = request.GET['bb']

	
	data.save()

	data = blog.objects.all()
	return render(request,'displayblog.html',{'data':data})


def dis(request):

	data = blog.objects.filter(bname="big boss ott2")
	return render(request,'dis.html',{'data':data })

# def saveeditdata(request):
# 	id = request.GET['id']
# 	data = blog.objects.get(id=id)

# 	data.bname = request.GET['bname']
# 	data.bb = request.GET['bb']

	
# 	data.save()

# 	data = blog.objects.all()
# 	return render(request,'displayblog.html',{'data':data})
# def edit(request):
# 	return render(request,"edit.html")

