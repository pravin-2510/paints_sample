from django.shortcuts import render
from home.models import Contact

# Create your views here.
def home(request):
    return render(request, 'home/index.html')
def product(request):
    return render(request, 'home/product.html')
def broucher(request):
    return render(request, 'home/broucher.html')
def aboutus(request):
    return render(request, 'home/about.html')
def contact(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        subject = request.POST['subject']
        content = request.POST['content']
        if ((len(name)>3 and len(name)<30) or (len(email)>6 and len(email)<30) or (len(phone)>3 and len(phone)<13) or (len(subject)>8 and len(subject)<70) or (len(content)>10 and len(content)<300)):
            contact = Contact(name=name, email=email, phone=phone, subject=subject, content=content)
            contact.save()
    return render(request, 'home/contact.html')
def product1(request):
    return render(request, 'home/product_1.html')
def product2(request):
    return render(request, 'home/product_2.html')
def product3(request):
    return render(request, 'home/product_3.html')
def product4(request):
    return render(request, 'home/product_4.html')
def product5(request):
    return render(request, 'home/product_5.html')