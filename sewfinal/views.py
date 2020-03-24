from django.shortcuts import render
from django.http import JsonResponse
from .forms import pfm, operations, orders, obgen
from .models import SubCategory,  SuperCategory, FabricDetails
from .models import Attributes, Components, StyleDetails,Obgenerate
from .models import OrderDetails
from django.shortcuts import render, get_object_or_404, redirect
from django.forms import formset_factory,modelformset_factory
# Create your views here.

cate = 0


def form1(request):
    if request.POST.get('category'):
        global cate

        category = request.POST.get('category')
        cate = category
        print(category)

        sub = SubCategory.objects.filter(category=category).order_by("name")
        print(sub)
        sub = [s.name for s in sub]

        return JsonResponse({"sub": sub})


    elif request.POST.get('subcategory'):

        subcategory = request.POST.get('subcategory')
        print(cate)
        print(subcategory)
        x = SubCategory.objects.filter(name=subcategory, category=cate).values_list('id', flat=True)
        print(x[0])
        superc = SuperCategory.objects.filter(sub_category=x[0], category=cate)
        superc = [s.name for s in superc]
        print(superc)

        return JsonResponse({"superc": superc})

    form = pfm(request.POST or None)

    if form.is_valid():
        print('abc')

    if request.GET:
        pfmno = request.GET.get('pf')
        fat = request.GET.get('factory')
        fab = request.GET.get('fabric')
        was = request.GET.get('wash')
        cate = request.GET.get('category')
        scate = request.GET.get('subcategory')
        pcate = request.GET.get('supercategory')
        st = request.GET.get('styletype')

        fd = FabricDetails(pfmno=pfmno, factory=fat, fabric=fab, wash=was, category=cate, subcategory=scate,
                           supercategory=pcate, styletype=st)
        fd.save()

    context = {
        "responseform": form
    }

    return render(request, 'responseform.html', context)


def form2(request):
    if request.POST.get('component'):
        comp = request.POST.get('component')
        print(comp)
        sub = Attributes.objects.filter(comp=comp).order_by("name")
        sub = [s.name for s in sub]
        return JsonResponse({"sub": sub})

    form = operations(request.POST or None)

    if form.is_valid():
        print('abc')

        form1.Cleaned_data = form.cleaned_form1.Cleaned_data
        pn = form1.Cleaned_data["pfmno"]
        s = form1.Cleaned_data["styleno"]
        c = form1.Cleaned_data["comp"]
        a = form1.Cleaned_data["attribute"]
        o = form1.Cleaned_data["operations"]
        com = form1.Cleaned_data["complexity"]
        spi = form1.Cleaned_data["spi"]
        sl = form1.Cleaned_data["stitch_length"]
        tc = form1.Cleaned_data["thread_consumption"]
        ma = form1.Cleaned_data["machine_auto"]
        wa = form1.Cleaned_data["work_aid"]
        smv = form1.Cleaned_data["smv"]
        al = form1.Cleaned_data["allowance"]
        sam = form1.Cleaned_data["sam"]
        ct = form1.Cleaned_data["ct"]
        g = form1.Cleaned_data["grade"]

        ca = Components.objects.filter(id=c).order_by('comp').values_list('comp', flat=True)

        print(ca[0])
        z = ca[0];
        print(pn, s, z, a, o, com, spi, sl, tc, ma, wa, smv, al, sam, ct, g)

        sd = StyleDetails.objects.create(pfmno=pn, styleno=s, comp=z, attribute=a, operations=o, complexity=com,
                                         spi=spi, stitch_length=sl, thread_consumption=tc,
                                         machine_auto=ma, work_aid=wa, smv=smv, allowance=al, sam=sam, ct=ct, grade=g)
        sd.save()
        print('abc')

    pfmnos = FabricDetails.objects.all()

    context = {
        "operations": form,
        "pfmnos": pfmnos,
    }

    return render(request, 'operations.html', context)


def form3(request):
    if request.POST.get('category'):
        global cate

        category = request.POST.get('category')
        cate = category
        print(category)

        sub = SubCategory.objects.filter(category=category).order_by("name")
        print(sub)
        sub = [s.name for s in sub]

        return JsonResponse({"sub": sub})


    elif request.POST.get('subcategory'):

        subcategory = request.POST.get('subcategory')
        print(cate)
        print(subcategory)
        x = SubCategory.objects.filter(name=subcategory, category=cate).values_list('id', flat=True)
        print(x[0])
        superc = SuperCategory.objects.filter(sub_category=x[0], category=cate)
        superc = [s.name for s in superc]
        print(superc)

        return JsonResponse({"superc": superc})

    elif request.POST.get('component'):

        comp = request.POST.get('component')
        print(comp)
        sub = Attributes.objects.filter(comp=comp).order_by("name")
        sub = [s.name for s in sub]
        return JsonResponse({"sub": sub})

    form = orders(request.POST or None)
    context = {
        "orderdetails": form,
    }

    return render(request, 'orderdetails.html', context)


def is_valid_queryparam(param):
    return param != '' and param is not None


def orderform(request):
    context = {}
    global obgenformset
    global count
    count = 0
    allopp= []
    global fd
    global qs
    qs=FabricDetails.objects.all()
    if request.method == 'POST' and count == 0:
        form1 = orders(request.POST)
        if form1.is_valid:
            form1.save(commit=True)
            odno = form1.cleaned_data['orderno']
            stno = form1.cleaned_data['styleno']
            lno = form1.cleaned_data['lineno']
            odqno = form1.cleaned_data['order_quantity']
            cpc=form1.cleaned_data['capacity']
            tgt = form1.cleaned_data['target']
            minps = form1.cleaned_data['mins_shift']
            expskill = form1.cleaned_data['expected_skill_level']
            fb=form1.cleaned_data['fabric']
            wsh=form1.cleaned_data['wash']
            ctg=form1.cleaned_data['category']
            subctg=form1.cleaned_data['subcategory']
            stype=form1.cleaned_data['styletype']
            cp=form1.cleaned_data['comp']
            atr=form1.cleaned_data['attribute']

            if is_valid_queryparam(fb):
                qs= qs.filter(fabric=fb)

            if is_valid_queryparam(wsh):
                qs = qs.filter(wash=wsh)

            if is_valid_queryparam(ctg):
                qs= qs.filter(category=ctg)

            if is_valid_queryparam(subctg):
                qs = qs.filter(subcategory=subctg)

            if is_valid_queryparam(stype):
                qs = qs.filter(styletype=stype)
            print(qs)

            for q in qs:
                print(q.pfmno)
                fd = StyleDetails.objects.filter(pfmno=q)
                if is_valid_queryparam(cp):
                    fd = fd.filter(comp=cp)

                if is_valid_queryparam(atr):
                    fd = fd.filter(attribute=atr)

                allopp.append(fd)
            print(allopp)
            sz=0
            for opp in allopp:
                sz=sz+1
            print(sz)
            obgenformset = modelformset_factory(Obgenerate, fields='__all__', extra=sz)
            context['allopp'] =allopp
            context['orderno']=odno
            context['styleno'] =stno
            context['target']=tgt
            context['expskill']=expskill
            context['minps']=minps
            formset = obgenformset()
            context['formset'] = formset
            count=count+1
            return render(request,"orderformgen.html",context)

    if request.method == "POST":
        formset = obgenformset(request.post or None)
        for form in formset.form:
            form.save()




    form1 = orders()
    context['form1'] = form1
    return render(request, "orderformgen.html", context)










# Create your views here.
