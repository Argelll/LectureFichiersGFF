#!/usr/bin/env python
# -*- coding:utf-8 -*-

import gzip
import logging

#Files hérite de la classe object
class Files(object):
  def __init__(self, File):
    self.File = File
    
  def Lecture(self):
    try:
      if self.File.lower().endswith(('.gz', '.gzip')):
        fp = gzip.open(self.File)
      else: 
        fp = self.File
    except:
      printf("un des fichiers proposés n'es pas en .gz ou .gzip")    
    
    fichier=open(fp,"r")
    fichierEntier = fichier.read()
    fichierDecoupe=fichierEntier.split("\n")
    return fichierDecoupe
    fichier.close()
    f.close()
