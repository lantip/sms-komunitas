from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from accounts.decorators import admin_required
from member.models import Usia, StatusSosial, Person, TemaInformasi, GolonganDarah, Family, Agama, StatusPerkawinan
from member.models import Pekerjaan, PendidikanTerakhir, HubunganKeluarga
from message.models import Queue, Log
from member.forms import AgeForm, StatusSosialForm, SearchForm
from wilayah.models import Desa, Dusun, Kampung, RT
from rest_framework import status, generics
from rest_framework.decorators import api_view
from rest_framework.response import Response
from member.serializers import PersonSerializer, LargeResultsSetPagination, StandardResultsSetPagination
from member.serializers import FamilySerializer, GolonganDarahSerializer
import json
from datetime import datetime
from django.views.decorators.csrf import csrf_exempt
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import AllowAny
from django_remote_forms.forms import RemoteForm
from message.forms import (DeleteMessagesForm, BroadcastForm,
                           SettingBroadcastForm, ReplyForm, SearchForm)
from django.core.serializers.json import DjangoJSONEncoder
from message.views import _get_queryset, _send_sms, _write_log, _send_single_sms, _write_single_log

class person_list(generics.ListCreateAPIView):
    authentication_classes = (SessionAuthentication, BasicAuthentication)
    permission_classes = (AllowAny,)
    serializer_class = PersonSerializer
    pagination_class = StandardResultsSetPagination
    def get_queryset(self):
        queryset = Family.objects.all()
        nokk = self.request.query_params.get('no_kk', None)
        nik = self.request.query_params.get('nik', None)
        goldar = self.request.query_params.get('goldar', None)
        sex = self.request.query_params.get('sex', None)
        agama = self.request.query_params.get('agama', None)
        hub = self.request.query_params.get('hubungan_keluarga', None)
        if nokk:
            queryset = queryset.filter(family__nomor_kk=nokk)
        if nik:
            queryset = queryset.filter(nomor_nik=nik)
        if goldar:
            queryset = queryset.filter(golongan_darah__golongan_darah=goldar)
        if sex:
            if 'laki' in sex:
                queryset = queryset.filter(jenis_kelamin=0)
            else:
                queryset = queryset.filter(jenis_kelamin=1)
        if agama:
            queryset = queryset.filter(agama__agama=agama)
        return queryset

class family_list(generics.ListCreateAPIView):
    authentication_classes = (SessionAuthentication, BasicAuthentication)
    permission_classes = (AllowAny,)
    serializer_class = FamilySerializer
    pagination_class = StandardResultsSetPagination
    def get_queryset(self):
        queryset = Family.objects.all()
        nokk = self.request.query_params.get('no_kk', None)
        if nokk:
            queryset = queryset.filter(nomor_kk=nokk)
        return queryset

@csrf_exempt
def receive_json(request):
    if request.method == "POST":
        jsondata = json.loads(request.body)
        for js in jsondata:
            if 'desa' in js:
                try:
                    desa = Desa.objects.get(nama_desa=js['desa'])
                except:
                    desa = Desa()
                    desa.nama_desa = js['desa']
                    desa.save()
            else:
                desa = None
            if 'dusun' in js and desa:
                try:
                    dusun = Dusun.objects.get(nama_dusun=js['dusun'])
                except:
                    dusun = Dusun()
                    dusun.nama_desa = desa
                    dusun.nama_dusun = js['dusun']
                    dusun.save()
            else:
                dusun = None
            if 'kampung' in js and dusun:
                try:
                    kampung = Kampung.objects.get(nama_kampung=js['kampung'])
                except:
                    kampung = Kampung()
                    kampung.nama_dusun = dusun
                    kampung.nama_kampun = js['kampun']
                    kampung.save()
            else:
                kampung = None
            if 'rt' in js:
                try:
                    rt = RT.objects.get(nama_rt=js['rt'])
                except:
                    rt = RT()
                    rt.nama_rt = js['rt']
                    rt.save()
            else:
                rt = None

            try:
                fam = Family.objects.get(nomor_kk=js['nokk'])
            except:
                fam = Family()
                fam.nomor_kk = js['nokk']
                if desa:
                    fam.alamat_desa = desa
                if dusun:
                    fam.alamat_dusun = dusun
                if kampung:
                    fam.alamat_kampung = kampung
                if rt:
                    fam.alamat_rt = rt
                fam.save()
            for anggota in js['anggota_keluarga']:
                try:
                    person = Person.objects.get(family=fam, nomor_nik=anggota['nik'], nama_lengkap=anggota['nama'])
                except:
                    person = Person()
                    person.family = fam
                    person.nomor_nik = anggota['nik']
                    person.nama_lengkap = anggota['nama']
                    if 'laki' in anggota['jenis_kelamin']['name'].lower():
                        person.jenis_kelamin = 0
                    else:
                        person.jenis_kelamin = 1
                    person.tempat_lahir = anggota['tempat_lahir']
                    dtm = datetime.strptime(anggota['tanggal_lahir'], '%Y-%m-%d')
                    person.tanggal_lahir = dtm.date()
                    try:
                        goldar = GolonganDarah.objects.get(golongan_darah=anggota['golongan_darah']['name'])
                    except:
                        goldar = GolonganDarah()
                        goldar.golongan_darah = anggota['golongan_darah']['name']
                        goldar.save()
                    person.golongan_darah = goldar
                    try:
                        agama = Agama.objects.get(agama=anggota['agama']['name'])
                    except:
                        agama = Agama()
                        agama.agama = anggota['agama']['name']
                        agama.save()
                    person.agama = agama
                    try:
                        kawin = StatusPerkawinan.objects.get(status_perkawinan=anggota['status_kawin']['name'])
                    except:
                        kawin = StatusPerkawinan()
                        kawin.status_perkawinan = anggota['status_kawin']['name']
                        kawin.save()
                    person.status_perkawinan = kawin
                    try:
                        pendidikan = PendidikanTerakhir.objects.get(pendidikan_terakhir=anggota['pendidikan']['name'])
                    except:
                        pendidikan = PendidikanTerakhir()
                        pendidikan.pendidikan_terakhir = anggota['pendidikan']['name']
                        pendidikan.save()
                    person.pendidikan_terakhir = pendidikan
                    try:
                        pekerjaan = Pekerjaan.objects.get(pekerjaan=anggota['pekerjaan']['name'])
                    except:
                        pekerjaan = Pekerjaan()
                        pekerjaan.pekerjaan = anggota['pekerjaan']['name']
                        pekerjaan.save()
                    person.pekerjaan = pekerjaan
                    try:
                        hubkel = HubunganKeluarga.objects.get(hubungan_keluarga=anggota['hubungan_keluarga']['name'])
                    except:
                        hubkel = HubunganKeluarga()
                        hubkel.hubungan_keluarga = anggota['hubungan_keluarga']['name']
                        hubkel.save()
                    person.hubungan_keluarga = hubkel
                    person.save()
        hasil = '{"status":"'+stat+'","msg": "'+result+'"}'
        return HttpResponse(hasil, content_type="application/json")
    else:
        result = '{"status":"ERROR","msg": "Forbidden"}'
        return HttpResponse(result, content_type="application/json")

@csrf_exempt
def newmessage(request):
    from django.middleware.csrf import CsrfViewMiddleware
    csrf_middleware = CsrfViewMiddleware()
    response_data = {}
    if request.method == 'GET':
        # Get form definition
        form = BroadcastForm()
    elif request.raw_post_data:
        request.POST = json.loads(request.raw_post_data)
        # Process request for CSRF
        csrf_middleware.process_view(request, None, None, None)
        form_data = request.POST.get('data', {})
        form = BroadcastForm(form_data)
        if form.is_valid():
            message = form.cleaned_data["message"]

            #Send Member
            if form.cleaned_data["member"]:
                queryset = _get_queryset(form)
                if queryset:
                    persons = Person.objects.filter(queryset)
                else:
                    persons = Person.objects.all()

                _send_sms(persons, message)
                _write_log(persons, message)

            #Send External Receiver
            if form.cleaned_data["external"]:
                if form.cleaned_data["extra_phones"]:
                    phones = form.cleaned_data["extra_phones"].split(',')
                    for phone in phones:
                        _send_single_sms(phone, message)
                        _write_single_log(message)

            #Send Non Member Receiver
            if form.cleaned_data["nonmembers"]:
                if form.cleaned_data["non_member"]:
                    phones = form.cleaned_data["non_member"]
                    for phone in phones:
                        person = nonmember.objects.get(id=int(phone.id))
                        _send_single_sms(phone, message)
                        _write_single_log(message,None,person)

            #Send Member Ulang Tahun
            if form.cleaned_data["ultah"]:
                if form.cleaned_data["ultah_today"]:
                    phones = form.cleaned_data["ultah_today"]
                    for phone in phones:
                        person = Person.objects.get(id=phone.id)
                        _send_single_sms(phone, message)
                        _write_single_log(message,None,person)

    remote_form = RemoteForm(form)
    # Errors in response_data['non_field_errors'] and response_data['errors']
    response_data.update(remote_form.as_dict())

    response = HttpResponse(
        json.dumps(response_data, cls=DjangoJSONEncoder),
        content_type="application/json"
    )

    # Process response for CSRF
    csrf_middleware.process_response(request, response)
    return response

@login_required
def home(request):
    if request.method == "POST":
        form = SearchForm(request.POST)
        person_list = ''
        if form.is_valid():
            q = form.cleaned_data["q"]
            person_list = Person.objects.filter(nama_lengkap__contains=q)
    else:
        form = SearchForm()
        person_list = Person.objects.all()
        
    paginator = Paginator(person_list, 5)
    page = request.GET.get('page')
    try:
        persons = paginator.page(page)
    except PageNotAnInteger:
        persons = paginator.page(1)
    except EmptyPage:
        persons = paginator.page(paginator.num_pages)
        
    return render_to_response('member/member.html',
                              {"persons":persons, "form":form,},
                              context_instance=RequestContext(request))

@login_required
def view_member(request,member_id):
    person = get_object_or_404(Person, pk=member_id)
    
    return render_to_response("member/view_member.html",
                              {"person":person, },
                              context_instance=RequestContext(request))

@admin_required
def settings_age(request):
    if request.method == 'POST':
        form = AgeForm(request.POST)
        if form.is_valid():
            form.save()
            
            return HttpResponseRedirect(reverse('setting_age'))
    else:
        form = AgeForm()
        
    ages = Usia.objects.all()
    
    return render_to_response('member/settings_age.html',
                              {"ages": ages, "form": form, },
                              context_instance=RequestContext(request))

@admin_required
def view_age(request, age_id):
    age = get_object_or_404(Usia, pk=age_id)
    if request.method == "POST":
        form = AgeForm(request.POST, instance=age)
        if form.is_valid():
            form.save()
            
            return HttpResponseRedirect(reverse('setting_age'))
    else:
        form = AgeForm(instance=age)
        
    return render_to_response("member/view_age.html",
                              {"age": age, "form": form, },
                              context_instance=RequestContext(request))

@admin_required
def delete_age(request, age_id):
    if request.method == 'POST':
        age = get_object_or_404(Usia, pk=request.POST.get("age-id"))
        age.delete()
        
    return HttpResponseRedirect(reverse('setting_age'))

@admin_required
def settings_social(request):
    if request.method == 'POST':
        form = StatusSosialForm(request.POST)
        if form.is_valid():
            form.save()
            
            return HttpResponseRedirect(reverse('setting_social'))
    else:
        form = StatusSosialForm()
        
    statuses = StatusSosial.objects.all()
    
    return render_to_response('member/settings_social.html',
                              {"statuses": statuses, "form": form,},
                              context_instance=RequestContext(request))

@admin_required
def view_social(request, sos_id):
    social = get_object_or_404(StatusSosial, pk=sos_id)
    
    if request.method == 'POST':
        form = StatusSosialForm(request.POST, instance=social)
        if form.is_valid():
            form.save()
            
            return HttpResponseRedirect(reverse('setting_social'))
    else:
        form = StatusSosialForm(instance=social)
        
    return render_to_response("member/view_social.html",
                              {"social": social, "form": form, },
                              context_instance=RequestContext(request))

@admin_required
def delete_social(request, sos_id):
    if request.method == 'POST':
        soc = get_object_or_404(StatusSosial, pk=request.POST.get('sos-id'))
        soc.delete()
        
    return HttpResponseRedirect(reverse('setting_social'))



def query_operator(opr):
    OPERATOR = {
    "TELKOMSEL" : [
    "+62811",    
    "+62812",  
    "+62813",     
    "+62821",
    "+62822",
    "+62823",     
    "+62852",     
    "+62853",
    ],
    "INDOSAT" : [
    "+62814",     
    "+62815",     
    "+62816",     
    "+62855",     
    "+62856",     
    "+62857",     
    "+62858",  
    ],   
    "XL" : [
    "+62817",     
    "+62818",     
    "+62819",     
    "+62878",     
    "+62877",     
    "+62859",             
    "+62879",
    ],     
    "THREE" : [
    "+62896",     
    "+62897",     
    "+62898",     
    "+62899"
    ],
    "AXIS" : [
    "+62831", 
    "+62838"
    ],
    "LAINNYA" : [
    "+62274",
    "+62881",     
    "+62882", 
    "+62883",
    "+62884",
    "+62887",    
    "+62888",     
    "+62889",
    "+62828"
    ]
        
    }    
    ttl = 0
    for item in OPERATOR[opr]:
        from django.db import connection
        cursor = connection.cursor()
        cursor.execute("SELECT Count(*) FROM inbox WHERE SenderNumber like %s", [item+"%"])
        row = cursor.fetchone()
        cursor.close()
        ttl = int(ttl) + int(row[0])
    return ttl

@login_required
def statistics(request):
    from django.db.models import Count, Q, Sum
    from datetime import datetime, timedelta
    import json
    import utils as collections
    person = Person.objects.values('pekerjaan').filter(pekerjaan__isnull=False).annotate(dcount=Count('pekerjaan')).order_by('-dcount')[:6]
    total = Person.objects.all().count()
    suma = 0
    pekerjaan = []
    for p in person:
        from member.models import Pekerjaan 
        emp = Pekerjaan.objects.get(pk=p['pekerjaan'])
        pekerjaan.append({'label': emp.pekerjaan.title(), 'value': p['dcount']})
        suma = suma + int(p['dcount'])
    sisa = total - suma
    pekerjaan.append({'label': 'Lainnya', 'value': sisa})


    person = Person.objects.values('tema_informasi').filter(tema_informasi__isnull=False).annotate(dcount=Count('tema_informasi')).order_by('-dcount')[:6]
    informasi = []
    for p in person:
        info = TemaInformasi.objects.get(pk=p['tema_informasi'])
        informasi.append({'label': info.tema_informasi.title(), 'value': p['dcount']})

    usia = Usia.objects.all()
    today = datetime.today()
    prsn = []
    for u in usia:
        end = today - timedelta(days=365 * int(u.umur_min))
        start = today - timedelta(days=365 * int(u.umur_max))
        p = Person.objects.filter(tanggal_lahir__gte=start,tanggal_lahir__lte=end).count()
        prsn.append({'label':u.name, 'value':p})


    goldar = GolonganDarah.objects.all()
    gldrh = []
    for g in goldar:
        p = Person.objects.filter(golongan_darah=g).count()
        gldrh.append({'label':g.golongan_darah, 'value':p})


    start = today - timedelta(days=30)
    smsout = Log.objects.extra({'published':"date(date)"}).filter(date__gte=start).values('published').annotate(total=Count('id'))
    smsin = Queue.objects.extra({'published':"date(date)"}).filter(date__gte=start).values('published').annotate(total=Count('id'))
    data = {}
    for out in smsout:
        data[out['published'].strftime("%m/%d")] = { 'out' : out['total'] }
    for sin in smsin:
        try:
            data[sin['published'].strftime("%m/%d")]['in'] = sin['total']
        except:
            data[sin['published'].strftime("%m/%d")] = {'in': sin['total']}
    import time
    tlkmsl = query_operator("TELKOMSEL")
    indst = query_operator("INDOSAT")
    xls = query_operator("XL")
    three = query_operator("THREE")
    axis = query_operator("AXIS")
    lain = query_operator("LAINNYA")
    oprtr = [
        { 'label' : 'TELKOMSEL', 'value': tlkmsl },
        { 'label' : 'INDOSAT', 'value': indst},
        { 'label' : 'XL', 'value': xls},
        { 'label' : 'THREE', 'value': three},
        { 'label' : 'AXIS', 'value': axis},
        { 'label' : 'LAINNYA', 'value': lain}
    ]

    most_active = Log.objects.values('persons').exclude(persons=None).annotate(dcount=Count('persons')).order_by('-dcount')[:6]
    pma = []
    for pp in most_active:
        if pp['persons']:
            nama = Person.objects.get(id=pp['persons'])
            pma.append({'label': nama.nama_lengkap,'value': pp['dcount']})

    sms = collections.OrderedDict(sorted(data.items()))

    txt = Log.objects.all()
    xcld = ["kita","tes","test","iso","tak","wis","wib.","bn2013","atas","mas","mbak","simak","kirim","sek","bro","idul","fitri","adha","lahir","bathin","bathin","kesalahan","tanya","jawab","smsangkringan","smskomunitas","angkringan","dari","dr","ini","itu","karena","krn","bahwa","bhw","yang","yg","ke","untuk","utk","oleh","saya","sy","aku","anda","mereka","mrk","sehingga","shg","hingga","hanya","cuma","hny","satu","pertama","dua","kedua","tiga","ketiga","empat","keempat","lima","kelima","enam","keenam","tujuh","ketujuh","delapan","kedelapan","sembilan","kesembilan","sepuluh","kesepuluh","1","2","3","4","5","6","7","8","9","0","seperti","spt","bisa","akan","mau","biasa","tujuan","nanti","kemarin","besok","pagi","siang","sore","malam","mlm","selamat","slmt","ulang","tahun","th","thn","mohon","maaf","hari","hr","tanggal","tgl","jam","wib","jadilah","selalu","kekasih","terhebat","seperti","lagu","anji","yuk","aktifkan","iringnya","cuma","rp0","1","per3hr","sms","ketik","anji","808","berlaku","perpanjangan","rp.3190","per7hr","invite","ulang","pinku","yaa","pin","mksih","apa","siapa","bagaimana","bgm","bgmn","mana","dimana","kemana","cara","terima","kasih","terimakasih","thx","trmksh","telah","tlh","sudah","sdh","menjadi","mjd","pelanggan","indosat","kenalan","tanpa","batas","dan","bonus","gratis","nelpon","telpon","telepon","telp","alamat","60","menit","hub","hubungi","*955*1","lalu","ya/ok","topup","pulsa","rp","rupiah","berhasil","via","atm","bri","kode","trx","1006191302714505","pulsa","saat","ini","menggunakan","pakai","memakai","pakai","keluar","masuk","msk","selesai","mulai","indosat","telkomsel","telkom","xl","im3","nomor","nomer","no","ya","yes","memasuki","masa","tenggang","isi","ulang","hari","&dapatkan","dpt","sms","kesesama","2hari","hanya","diberikan1x","info","100.gp471","jangan","lewatkan","promo","ketik","ya","919","gratis","telp","seharian","sesama","cuma","terakhir","mau","punya","barang","artis","tablet","voucher","belanja","aktfkan","iring","di*808*18","kumpulkan","poin","tukar","hadiah","pilihanmu","www.indosat.com/iring80818","pelanggan","&","+","dsb","dll","harap","mohon","minta","penawaran","kak","kok","asalamualaikum","wrwb","swt","otw","www","aq","bapak","bpk","ibu","sdr","yth","ybs","akan","dan","oleh","ada","nek","ya","ya?","kiri","dengan","kalau","kalo","lha","lah","kan","2014","2013","2015","ring","edisi","lewat","gang","pak"]
    tt = {}
    for msg in txt:
        psn = msg.message.split()
        for k in psn:
            if len(k) > 2:
                if k.lower().strip().replace('#','') not in xcld:
                    try:
                        tt[k] = tt[k] + 1
                    except:
                        tt[k] = 1
    import operator
    sorted_tt = sorted(tt.items(), key=operator.itemgetter(1))
    sorted_tt.reverse()
    cloud_text = sorted_tt[:52]

    return render_to_response("message/statistik.html",
                              {
                                "pekerjaan":json.dumps(pekerjaan),
                                "informasi": json.dumps(informasi),
                                "usia": json.dumps(prsn),
                                "golongandarah": json.dumps(gldrh),
                                "sms": sms,
                                "operator": json.dumps(oprtr),
                                "active": json.dumps(pma),
                                "cloud" : cloud_text
                               },
                              context_instance=RequestContext(request))