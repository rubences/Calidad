#!/usr/bin/python3
# -*- coding: utf-8 -*-


"""
Módulo de prueba

El objetivo de este módulo es mostrar cómo
usar las herramientas relacionadas con la documentación
"""


__author__ = "Sébastien CHAZALLET"
__copyright__ = "Copyright 2012"
__credits__ = ["Sébastien CHAZALLET", "InsPyration.org", "Ediciones ENI"]
__license__ = "GPL"
__version__ = "1.0"
__maintainer__ = "Sébastien CHAZALLET"
__email__ = "sebastien.chazallet@laposte.net"
__status__ = "Production"


def cuadrado(x):
	"""Devuelve el cuadrado de x"""
	return x**2

def cubo(x):
	"""Devuelve el cubo de x"""

def potencia(x, y):
	"""Devuelve la potencia y de x"""
	return x**y

class Wrapper:
	"""Clase que permite hacer los cálculos de potencia"""
	def potencia(self, x, y):
		"""Método para el cálculo"""
		if y == 2:
			return cuadrado(x)
		elif y == 3:
			return cubo(x)
		else:
			return potencia(x, y)


