#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author: <Macarena Reale Portelli>

class Persona(object):

    def __init__(self, dni, nombre="", edad=0):
        self.nombre = nombre
        self.edad = edad
        self.dni = dni

    def mostrar(self):
        print(f"nombre : {self.nombre} edad :{self.edad} dni : {self.dni}")


#TODO_edad


    def es_mayor_de_edad(self):
        if self.edad >= 18:
            return True
        else:
            return False
