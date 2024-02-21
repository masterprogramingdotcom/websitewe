from django.shortcuts import render, redirect
from django.contrib import messages
from django.views import View
from home.models import Contact

# Create your views here.


class HomeView(View):
    def get(self, request, *args, **kwargs):
        return render(request, "home/index.html")

    def post(self, request, *args, **kwargs):
        try:
            data = request.POST
            Contact.objects.create(
                name=data.get("name"),
                email=data.get("email"),
                number=data.get("number"),
                services=data.get("services"),
                message=data.get("message"),
            )
            messages.success(request, "Successfully Submit Your Request, Please Wait...")
            return redirect('/')
        except Exception as e:
            messages.info(request, "Something Went Wrong!, Please try again...")
            return redirect('/')
