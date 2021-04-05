# coding: utf-8

import os
import os.path
import codecs
import json

from . import dataid_mit

#----------------------------------------------------------
class Database_clm(object):
#----------------------------------------------------------

   #-------------------------------------------------------
   def __init__(self):
   #-------------------------------------------------------
      self.data_o = None
      self.maxId_o = dataid_mit.DataId_clm()
      self.readData_p()
      

   #-------------------------------------------------------
   def create_px(self, data_opl):
   #-------------------------------------------------------
      print("create_px")
      print("*****************")
      print(data_opl)
      id_s = self.maxId_o.create_px()
      print(id_s)
      self.data_o[str(id_s)] = data_opl
      print(self.data_o[str(id_s)])
      print("*****************")
      self.saveData_p()
      return str(id_s)

   #-------------------------------------------------------
   def read_px(self, id_spl = None):
   #-------------------------------------------------------
      data_o = None
      if id_spl == None:
         data_o = self.data_o
      else:
         if id_spl in self.data_o:
               data_o = self.data_o[id_spl]
      return data_o
   


   
   #-------------------------------------------------------
   def update_px(self, id_spl, data_opl):
   #-------------------------------------------------------
      print("update_px")
      status_b = False
      if id_spl in self.data_o:
         print(data_opl)
         print(id_spl)
         print(self.data_o)
         self.data_o[id_spl] = data_opl
         print(self.data_o[id_spl])
         self.saveData_p()
         status_b = True
      return status_b

   #-------------------------------------------------------
   def delete_px(self, id_spl):
   #-------------------------------------------------------
      status_b = False
      if self.data_o.pop(id_spl, None) != None:
         self.saveData_p()
         status_b = True
      return status_b

   #-------------------------------------------------------
   def getDefault_px(self):
   #-------------------------------------------------------
       return ['', '', '','']

   #-------------------------------------------------------
   def readData_p(self):
   #-------------------------------------------------------
      try:
         fp_o = codecs.open( 'webteams/data/mit_id.json', 'r', 'utf-8')
      except:
         self.data_o = {}
         self.saveData_p()
      else:
         with fp_o:
            self.data_o = json.load(fp_o)
      return

   #-------------------------------------------------------
   def saveData_p(self):
   #-------------------------------------------------------
      with codecs.open('webteams/data/mit_id.json', 'w', 'utf-8') as fp_o:
         json.dump(self.data_o, fp_o, indent=3)
   
   




# EOF