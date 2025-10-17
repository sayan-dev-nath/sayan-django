from django.shortcuts import render


# Create your views here.
def generate_qr(request):
    return render(request, "scanner/generate.html")


def scan_qr(request):
    return render(request, "scanner/scan.html")
