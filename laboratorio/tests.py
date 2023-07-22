from django.test import TestCase
from .models import Laboratorio

# Create your tests here.

''' ## para ver si arroja =>> en consola y si conecta
class LaboratorioTest(TestCase):
	@classmethod
	def setUpTestData(cls):
		cls.x = 1
	def test_nombre_correcto(self):
		print("Prueba =>>", self.x)
'''
class LaboratorioTest(TestCase):
	@classmethod
	def setUpTestData(cls):
		print("setup")
		cls.laboratorio = Laboratorio(nombre = "Lab x",
		    ciudad= "BioBio",
		    pais = "Chile")
		cls.laboratorio.save()  # # se guarda en DB
	def test_nombre_correcto(self):
		print("setup")
		#en el setup se creo un Laboratorio	# ahora al consultar debe existir UN laboratorio
		labs = Laboratorio.objects.all()
		print("numero de labs:", labs.count())
		self.assertEquals(labs.count(), 1)
		self.assertNotEquals(labs.count(), 2)
		self.assertEquals(labs.first().nombre, "Lab x")

	def test_crear_retorna_status_200(self):
# envio una petición POST a /laboratorio/labratorio/create Retorna status200 y crea
# crea un nuevo laboratorio
		response = self.client.post("/laboratorio/laboratorio/create", {
				  "nombre": "Lab z",
				  "ciudad": "Octava Region",
				  "pais" : "Chile"
		}, follow = True)
		self.assertEquals(response.status_code, 200)
		labs = Laboratorio.objects.all()
		self.assertEquals(labs.count(), 2)
		self.assertEquals(labs.last().nombre, "Lab z")
		self.assertTemplateUsed(response, "laboratorio_list.html")
