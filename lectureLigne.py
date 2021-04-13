#!/usr/bin/env python
# -*- coding:utf-8 -*-

import sys
from LectureFichier import *

taille=0
nombreComptes=0
nombreAutres=0
typeElement="pseudogene"
nomFichier = sys.argv[1]
try:
  nomFichierEcriture = sys.argv[2]
except:
  nomFichierEcriture="numeros_d_accession.txt"  


fEcrit=open(nomFichierEcriture,"w")
fichier = Files(nomFichier)
toutesLignes=fichier.Lecture()
for ligne in toutesLignes :
  position=ligne.split("\t")
  try:
    if (position[2]==typeElement)
      nombreComptes=nombreComptes+1
      informations=position[9].split(";")
      numAccession=informations[0].split(":")
      
      fEcrit.write(informations[1]+"/n")
      fEcrit.write(position[0]+"\n")
  except:
    pass
nombreTotal=nombreComptes+nombreAutres
print ("Il y a "+str(nombreComptes)+" "+str(typeElement)+"s")
fEcrit.close()
