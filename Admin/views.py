from django.shortcuts import render
from .models import Admin
# Create your views here.

def regisadmin(request):


    if request.method == 'POST':
        nama = request.POST['namalengkap']
        NoTelp = request.POST['notelp']
        NoHP = request.POST['nohp']
        Provinsi = request.POST['provinsi']
        kota = request.POST['kota']
        Alamat = request.POST['alamat']
        KodePos = request.POST['kodepos']
        Email = request.POST['email'] 
        # untuk menghubungkan antara model dengan view ( mode = view request.POST)
        admin = Admin.objects.create(
            NamaLengkap = nama, 
            NoTelp = NoTelp, 
            NoHP = NoHP,
            Provinsi = Provinsi,
            kota = kota,
            Alamat = Alamat,
            KodePos = KodePos,
            Email = Email
        )

    

    return render(request, 'Admin/Tambah.html')

def showadmin(request):
    daftaradmin = Admin.objects.all()
    
    context ={
        'daftaradmin' : daftaradmin,
    }
    return render(request, 'Admin/Admin.html', context)