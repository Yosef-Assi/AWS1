from django.shortcuts import render,HttpResponse,redirect
import random 	
from datetime import datetime

def root(request):
    request.session.set_expiry(300)
    
    if 'gold' not in request.session or 'activities' not in request.session:
        request.session['gold'] = 0
        request.session['activities'] = []
        
    return render(request,"index.html")
def show(request):
    request.session['my_list'] = []
    if request.POST['hide']=='farm':
        rand=random.randint(10,20) 
        request.session['rand']=rand
        request.session['gold']+=request.session['rand']
        request.session['activities'].append('You are earned a' +" "+request.POST['hide']+ ' and earned ' +     str(rand)   +" "+ '(' + str(datetime.now().strftime("%b-%d-%Y %H:%M-%p")) + ')')

    elif request.POST['hide']=='cave':
        rand=random.randint(10,20) 
        request.session['rand']=rand
        request.session['my_list'].append(rand)
        request.session.save()
        request.session['gold']+=request.session['rand']
        request.session['activities'].append('You are earned a' +" "+request.POST['hide']+ ' and earned ' +     str(rand)   +" "+ '(' + str(datetime.now().strftime("%b-%d-%Y %H:%M-%p")) + ')')

    elif request.POST['hide']=='house':
        rand=random.randint(10,20) 
        request.session['rand']=rand
        request.session['gold']+=request.session['rand']
        request.session['activities'].append('You are earned a' +" "+request.POST['hide']+ ' and earned ' +     str(rand)   +" "+ '(' + str(datetime.now().strftime("%b-%d-%Y %H:%M-%p")) + ')')

    elif request.POST['hide']=='quest':
        rand=random.randint(10,20) 
        request.session['rand']=rand
        request.session['gold']+=request.session['rand']
        rand=random.randint(-50,50) 
        request.session['rand']=rand
        request.session['gold']+=request.session['rand']
        if rand >= 0:
            request.session['activities'].append('Entered a Quest and earned ' + str(rand) +' gold' + ' ' + '(' + str(datetime.now().strftime("%b-%d-%Y %H:%M-%p")) + ')')
        else:
            request.session['activities'].append('Entered a Quest and lost ' + str(rand) + ' gold... Ouch...' + ' ' + '(' + str(datetime.now().strftime("%b-%d-%Y %H:%M-%p")) + ')')
    return redirect('/gold')
