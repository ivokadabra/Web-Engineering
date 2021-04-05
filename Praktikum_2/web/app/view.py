# coding: utf-8

import codecs
import os.path
import string

from mako.template import Template
from mako.lookup import TemplateLookup

# ----------------------------------------------------------


class View_cl(object):
    # ----------------------------------------------------------

    # -------------------------------------------------------
    def __init__(self):
        # -------------------------------------------------------
        self.lookup_o = TemplateLookup('webteams/templates/t')
    # -------------------------------------------------------
    def changeList_px(self, data_opl):
        # -------------------------------------------------------
       
     
       
            template_o = self.lookup_o.get_template('mitarbeiter.tpl')
            markup_s = template_o.render(data_o=data_opl)
            
            return markup_s
        
     


    def createList_px2(self, data_opl):
            # -------------------------------------------------------
      
            template_o = self.lookup_o.get_template('list_weiter.tpl')
            markup_s = template_o.render(data_o=data_opl)
            return markup_s






    def createMitList(self, data_opl):
            # -------------------------------------------------------
      
            template_o = self.lookup_o.get_template('mit.tpl')
           
            i=2
            print(str(i).decode("utf-8"))
            print(data_opl)

            markup_s = template_o.render(data_o=data_opl)
            return markup_s  


    def createWeiter(self, data_o,data_u,data_a,i,id,o):
            # -------------------------------------------------------
            print("create weiter")
            print(data_o)
            print(data_u)
            print(i)
            print(id)
            template_o = self.lookup_o.get_template('weiter.tpl')
            markup_s = template_o.render(data_o=data_o,data_u=data_u,data_a=data_a,ip=i,id=id,o=o)
            return markup_s 



    def create_zeige_mit(self, data_o,data_u,i):
            # -------------------------------------------------------
            print("create weiter")
          
            print(i)
            print(id)
            template_o = self.lookup_o.get_template('zeige_mit.tpl')
            markup_s = template_o.render(data_o=data_o,data_u=data_u,i=i)
            return markup_s     


    def create_brechen(self, data_o,data_u,i):
            # -------------------------------------------------------
            print("create weiter")
          
            print(i)
            print(id)
            template_o = self.lookup_o.get_template('anbrechen.tpl')
            markup_s = template_o.render(data_o=data_o,data_u=data_u,i=i)
            return markup_s                     


    def weit(self, data_o,data_u,i,id,p,l):
            # -------------------------------------------------------
           
            print("id")
            print(id)
            print(data_o)
            print(data_u)
            template_o = self.lookup_o.get_template('weiterbildung.tpl')
            markup_s = template_o.render(data_o=data_o,data_u=data_u,p=i,k=id,pp=p,opa=l,nomer=id)
            return markup_s                        
        
           
    
    def createAnzeigeList(self, data_opl,data_a,i,pesho,data_st,data_zer):
            # -------------------------------------------------------
            
            print(i)
            template_o = self.lookup_o.get_template('anzeigeM.tpl')
            print("baba")
            print(id)
            markup_s = template_o.render(data_o=data_a,data_u=data_opl,i=i,id=pesho,data_st=data_st,data_zer=data_zer)
            return markup_s


    def createAnzeigeList_2(self, data,i,d,data_o):
            # -------------------------------------------------------
            
            print(i)
            template_o = self.lookup_o.get_template('anzeigeW.tpl')
            print("baba")
            print(id)
            markup_s = template_o.render(data=data,pesho=i,key_s=d,data_o=data_o)
            return markup_s        

    def createStart(self):
        # -------------------------------------------------------
        
        template_o = self.lookup_o.get_template('start.tpl')
        markup_s = template_o.render(in_1=1, in_2=2)
        return markup_s


    def angemeldet(self):
        # -------------------------------------------------------
        
        template_o = self.lookup_o.get_template('angemeldet.tpl')
        markup_s = template_o.render()
        return markup_s  

    def sort_mit(self,l,length):
        # -------------------------------------------------------
        
        template_o = self.lookup_o.get_template('sort_mit.tpl')
        markup_s = template_o.render(data_o=l,length=length)
        return markup_s 



    def sort_mit_weit(self,data_o,data_u,lenght):
        # -------------------------------------------------------
        
        template_o = self.lookup_o.get_template('sort_mit_weit.tpl')
        markup_s = template_o.render(data_o=data_o,data_u=data_u,length=lenght)
        return markup_s      


    def sort_weiterbildung(self,l,length):
        # -------------------------------------------------------
        
        template_o = self.lookup_o.get_template('sort_weit.tpl')
        markup_s = template_o.render(data_o=l,length=length)
        return markup_s  


    def sort_zertifikate(self,l,length):
            # -------------------------------------------------------
        
        template_o = self.lookup_o.get_template('zertifikate_sort.tpl')
        markup_s = template_o.render(data_o=l,length=length)
        return markup_s      


    def sort_weiterbildung_mit(self,l,length):
            # -------------------------------------------------------
        
        template_o = self.lookup_o.get_template('sort_weit_mit.tpl')
        markup_s = template_o.render(data_o=l,length=length)
        return markup_s              
    
    
    
    def createForm_px(self, id_spl, data_opl):
        # -------------------------------------------------------
        template_o = self.lookup_o.get_template('form.tpl')
        markup_s = template_o.render(data_o=data_opl, key_s=id_spl)
        return markup_s


    def createForm_px2(self, id_spl, data_opl2):
        # -------------------------------------------------------
        template_o = self.lookup_o.get_template('form2.tpl')
        markup_s = template_o.render(data_o=data_opl2, key_s=id_spl)
        return markup_s 


    def createForm_qual(self, id_spl, data_opl2):
        # -------------------------------------------------------
        template_o = self.lookup_o.get_template('qualifikation_form.tpl')
        markup_s = template_o.render(data_o=data_opl2, key_s=id_spl)
        return markup_s 



    def start_seite(self, i_1, i_2):
        # -------------------------------------------------------
        template_o = self.lookup_o.get_template('start.tpl')
        markup_s = template_o.render(in_1=i_1, in_2=i_2)
        return markup_s 

    def teilnehmen(self,data_o,i):
        # -------------------------------------------------------
        template_o = self.lookup_o.get_template('teilnehmen.tpl')
        markup_s = template_o.render(data_o=data_o,id=i)
        return markup_s             

    # -------------------------------------------------------
    
    def readFile_p(self, fileName_spl):
        # -------------------------------------------------------
        content_s = ''
        with codecs.open(os.path.join('templates', fileName_spl), 'r', 'utf-8') as fp_o:
            content_s = fp_o.read()
        return content_s
# EOF