from django.shortcuts import render, redirect


# define your third view here
def DashBoard(request):
    template_name = "academic_feedback_sys/dashboard.html"
    return render(request, template_name)
