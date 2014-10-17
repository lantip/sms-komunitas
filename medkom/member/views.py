from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from accounts.decorators import admin_required
from member.models import Usia, StatusSosial, Person, TemaInformasi, GolonganDarah
from message.models import Queue, Log
from member.forms import AgeForm, StatusSosialForm, SearchForm

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
    import json, collections
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
    operator = [
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
    return render_to_response("message/statistik.html",
                              {
                                "pekerjaan":json.dumps(pekerjaan),
                                "informasi": json.dumps(informasi),
                                "usia": json.dumps(prsn),
                                "golongandarah": json.dumps(gldrh),
                                "sms": sms,
                                "operator": json.dumps(operator),
                                "active": json.dumps(pma)
                               },
                              context_instance=RequestContext(request))