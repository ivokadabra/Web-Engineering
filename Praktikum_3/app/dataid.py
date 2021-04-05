# coding: utf-8

import os
import os.path
import codecs
import json



#----------------------------------------------------------
class DataId_cl(object):
#----------------------------------------------------------

   #-------------------------------------------------------
   def __init__(self):
   #-------------------------------------------------------
      self.maxId_i = 0
      self.readMaxId_p()
      

   #-------------------------------------------------------
   def create_px(self):
   #-------------------------------------------------------
      self.maxId_i += 1
      self.saveMaxId_p()
      return str(self.maxId_i)

   #-------------------------------------------------------
   def read_px(self):
   #-------------------------------------------------------
      return str(self.maxId_i)

   #-------------------------------------------------------
   def readMaxId_p(self):
   #-------------------------------------------------------
      try:
         fp_o = codecs.open( 'data/maxid.json', 'r', 'utf-8')
      except:
         self.maxId_i = 0
         self.saveMaxId_p()
      else:
         with fp_o:
            self.maxId_i = json.load(fp_o)
      return

   #-------------------------------------------------------
   def saveMaxId_p(self):
   #-------------------------------------------------------
      with codecs.open( 'data/maxid.json', 'w', 'utf-8') as fp_o:
         json.dump(self.maxId_i, fp_o)



class StatusId_cl(object):
    #----------------------------------------------------------

   #-------------------------------------------------------
   def __init__(self):
   #-------------------------------------------------------
      self.maxId_i = 0
      self.readMaxId_p()
      

   #-------------------------------------------------------
   def create_px(self):
   #-------------------------------------------------------
      self.maxId_i += 1
      self.saveMaxId_p()
      return str(self.maxId_i)

   #-------------------------------------------------------
   def read_px(self):
   #-------------------------------------------------------
      return str(self.maxId_i)

   #-------------------------------------------------------
   def readMaxId_p(self):
   #-------------------------------------------------------
     try:
         fp_o = codecs.open( 'data/statusid.json', 'r', 'utf-8')
     except:
         self.maxId_i = 0
         self.saveMaxId_p()
     else:
         with fp_o:
            self.maxId_i = json.load(fp_o)
     return self.maxId_i

   #-------------------------------------------------------
   def saveMaxId_p(self):
   #-------------------------------------------------------
      with codecs.open( 'data/statusid.json', 'w', 'utf-8') as fp_o:
         json.dump(self.maxId_i, fp_o)         


class DataId_mit_weit_cl(object):
#----------------------------------------------------------

   #-------------------------------------------------------
   def __init__(self):
   #-------------------------------------------------------
      self.maxId_i = 0
      self.readMaxId_p()
      

   #-------------------------------------------------------
   def create_px(self):
   #-------------------------------------------------------
      self.maxId_i += 1
      self.saveMaxId_p()
      return str(self.maxId_i)

   #-------------------------------------------------------
   def read_px(self):
   #-------------------------------------------------------
      return str(self.maxId_i)

   #-------------------------------------------------------
   def readMaxId_p(self):
   #-------------------------------------------------------
      try:
         fp_o = codecs.open( 'data/maxid.json', 'r', 'utf-8')
      except:
         self.maxId_i = 0
         self.saveMaxId_p()
      else:
         with fp_o:
            self.maxId_i = json.load(fp_o)
      return 

   #-------------------------------------------------------
   def saveMaxId_p(self):
   #-------------------------------------------------------
      with codecs.open( 'data/maxid.json', 'w', 'utf-8') as fp_o:
         json.dump(self.maxId_i, fp_o)



class DataId_weit_cl(object):
    #----------------------------------------------------------

   #-------------------------------------------------------
   def __init__(self):
   #-------------------------------------------------------
      self.maxId_i = 0
      self.readMaxId_p()
      

   #-------------------------------------------------------
   def create_px(self):
   #-------------------------------------------------------
      self.maxId_i += 1
      self.saveMaxId_p()
      return str(self.maxId_i)

   #-------------------------------------------------------
   def read_px(self):
   #-------------------------------------------------------
      return str(self.maxId_i)

   #-------------------------------------------------------
   def readMaxId_p(self):
   #-------------------------------------------------------
      try:
         fp_o = codecs.open( 'data/weit.id.json', 'r', 'utf-8')
      except:
         self.maxId_i = 0
         self.saveMaxId_p()
      else:
         with fp_o:
            self.maxId_i = json.load(fp_o)
      return self.maxId_i

   #-------------------------------------------------------
   def saveMaxId_p(self):
   #-------------------------------------------------------
      with codecs.open( 'data/weit.id.json', 'w', 'utf-8') as fp_o:
         json.dump(self.maxId_i, fp_o)


class Dataid_Qual_cl(object):
    #----------------------------------------------------------

   #-------------------------------------------------------
   def __init__(self):
   #-------------------------------------------------------
      self.maxId_i = 0
      self.readMaxId_p()
      

   #-------------------------------------------------------
   def create_px(self):
   #-------------------------------------------------------
      self.maxId_i += 1
      self.saveMaxId_p()
      return str(self.maxId_i)

   #-------------------------------------------------------
   def read_px(self):
   #-------------------------------------------------------
      return str(self.maxId_i)

   #-------------------------------------------------------
   def readMaxId_p(self):
   #-------------------------------------------------------
      try:
         fp_o = codecs.open( 'data/qual.id.json', 'r', 'utf-8')
      except:
         self.maxId_i = 0
         self.saveMaxId_p()
      else:
         with fp_o:
            self.maxId_i = json.load(fp_o)
      return self.maxId_i

   #-------------------------------------------------------
   def saveMaxId_p(self):
   #-------------------------------------------------------
      with codecs.open( 'data/qual.id.json', 'w', 'utf-8') as fp_o:
         json.dump(self.maxId_i, fp_o)         


# EOF