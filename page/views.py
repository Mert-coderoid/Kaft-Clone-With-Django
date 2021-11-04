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
def carousel_list(request):
    context = dict()
    # kaft_clone.com/manage/carousel/1/edit
    context["carousel"] = Carousel.objects.all().order_by("-pk")
    return render(request, "manage/carousel_list.html", context)

def carousel_update(request, pk):
        # Bu ismi oluşturun...
    context = dict()
        # kaft_clone/manage/carousel/1/edit
    # item = Carousel.objects.first()
    # context["form"] = CarouselModelForm(instance=item)
    context = Carousel.objects.get(pk=pk)
    return render(request, "manage/corousel_form.html", context)

def carousel_create(request):
    context = dict()
    context["form"] = CarouselModelForm()
    # item = Carousel.objects.first()
    # context["form"] = CarouselModelForm(instance=item)

    if request.method == "POST":
        print(request.POST)
        print(request.FILES.get("cover_image"))

        # create code is deleted
        form = CarouselModelForm(request.POST, request.FILES)
        print(f"\n form \n")

        if form.is_valid():
            form.save()

        messages.success(request,"Bir şeyler eklendi ama ne oldu bilemiyorum")
    return render(request, "manage/carousel_create.html", context)


