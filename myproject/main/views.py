from django.shortcuts import render


def profession(request):
    return render(request, "main/main-page.html")

def statistic(request):
    return render(request, "main/general-statistics.html")