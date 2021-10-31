from django.shortcuts import render
from django.contrib import messages
from .models import Carousel
from .forms import CarouselModelForm


# Create your views here.

    # User:
def index(request):
    context = dict()
    context['images'] = Carousel.objects.filter(
        status="published",
    ).exclude(cover_image="")
    # context["images"] = images
    return render(request, "home/index.html", context)

    # Admin:
def carousel_create(request):
    context = dict()
    context["form"] = CarouselModelForm
    item = Carousel.objects.first()
    context["form"] = CarouselModelForm(instance=item)

    if request.method == "POST":
        print(request.POST)
        # print(request.FILES["cover_image"])
        
        # create code is deleted
        form = CarouselModelForm(request.POST, request.FILES)
        print(form)
        
        if form.is_valid():
            form.save()

        messages.success(request,"Bir şeyler eklendi ama ne oldu bilemiyorum")
    return render(request, "manage/carousel_create.html", context)

def carousel_list(request):
    context = dict()
    # kaft_clone.com/manage/carousel/1/edit
    context["item"] = Carousel.objects.get(pk=pk).order_by("-pk")
    return render(request, "manage/carousel_list.html", context)

def carousel_update(request, pk):
    # Bu ismi oluşturun...
    context = dict()
    # kaft_clone/manage/carousel/1/edit
    # item = Carousel.objects.first()
    # context["form"] = CarouselModelForm(instance=item)
    item = Carousel.objects.get(pk=pk)
    context["form"] = CarouselModelForm(instance=item)
    return render(request, "manage/corousel_form.html", context)

    # stuff not checked
    if form.is_valid():
        form.save()
    
    messages.success(request, "manage/carousel_form.html", context)

