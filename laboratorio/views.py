from django.shortcuts import render
from .models import Laboratorio
from laboratorio.forms import LaboratorioForm
from django.http import HttpResponseRedirect, Http404

def v_laboratorio_create(request):
	if request.method == 'POST':
		form = LaboratorioForm(request.POST)
		if form.is_valid():
			form.save()
			return HttpResponseRedirect('/')

	context = {
			  'form': LaboratorioForm()
	}

	return render(request, 'laboratorio_create.html', context)
##
# ##-----------------------------------------------------------
def v_laboratorio_edit(request, laboratorio_id):
	try:
		context = {
				  'labo': Laboratorio.objects.get(id = laboratorio_id)
		}

	except:
		raise Http404
	if request.method == 'POST':
		form = LaboratorioForm(request.POST, instance=context['labo']) ##acá le pedimos que lo actualz
		if form.is_valid():
			form.save()
			return HttpResponseRedirect("/")
##	#context ya existe
	context['form'] = LaboratorioForm(instance=context['labo'])
	return render(request, 'laboratorio_edit.html', context)
##
# ##-----------------------------------------------------------
def v_laboratorio_list(request):
	from django.contrib.sessions.models import Session
	context = {
			  ##'nvisitas': Session.objects.all().count(), para cuando es contar con inicios de sesion
			  'nvisitas': 0,
			  'listar': Laboratorio.objects.all()
	}

	nvisits = request.session.get('num_visits', 0) #consulta
	request.session['num_visits'] = nvisits + 1 # guarda variable de session
	context['nvisitas'] = nvisits + 1 #muestra la info en html


	return render(request, 'laboratorio_list.html', context)

##
# ##-----------------------------------------------------------
def v_laboratorio_delete(request, laboratorio_id):
	contchesu = {
		'lav':Laboratorio.objects.get(id = laboratorio_id)
	}
	if request.method=='POST':
		contchesu['lav'].delete()
		return HttpResponseRedirect('/')

	return render(request, 'laboratorio_delete.html', contchesu )

