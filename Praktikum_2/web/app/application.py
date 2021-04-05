# coding: utf-8
import cherrypy
from .database import Database_cl
from .view import View_cl
from .database2 import Database_cl2
from .dataid import DataId_cl
from .dataid2 import DataId_cl2
##from .dataid_status import DataId_cls
from .database_status import Database_cls
from .data_o import Data
from .databasemit import Database_clm
from .dataid_mit import DataId_clm
from .databaseweit import Database_clw
from .dataid_weit import DataId_clw
from .database_qual import Database_clq
from .dataid_qual import DataId_clq
from .database_qual_in_weit import Database_clqiw
from .dataid_qual_in_weit import DataId_clqiw



import json

# ----------------------------------------------------------


class Application_cl(object):
    # ----------------------------------------------------------

    # -------------------------------------------------------
    def __init__(self):
        # -------------------------------------------------------
        self.db_o = Database_cl()
        self.db_o2 = Database_cl2()
        self.di_o1 = DataId_cl()
        self.di_o2 = DataId_cl2()
        self.view_o = View_cl()
        
        self.db_os = Database_cls()
        self.di_os = Database_cls()
        self.db_om = Database_clm()
        self.di_om = DataId_clm()
        self.db_ow = Database_clw()
        self.di_ow = DataId_clw()
        self.db_osq = Database_clq()
        self.di_osq = DataId_clq()
        self.db_oqiw= Database_clqiw()
        self.di_oqiw=DataId_clqiw()
    

        self.data = Data()



    @cherrypy.expose
    # -------------------------------------------------------
    def sort_mit_weit(self,data):
        #erste schleife sucht die 
        #ID der mitarbeiter
        #zweite nimmt alle Weitebildungen an dennen die Mitarbeiter teilnimmt

       data_o=[]
       data_u=[]
       length=int(self.di_o1.read_px())
       for i in range(1,length+2):
         if self.db_o.read_px(str(i))!=None:  
           if self.db_o.read_px(str(i))[0] in data:
               break
       length_weit=len(self.db_o2.read_px())
       for k in range(length_weit+2):
        if self.db_o2.read_px(str(k))!=None:
           if str(k) in self.db_om.read_px(str(i)):
               data_o.append(self.db_o2.read_px(str(k)))
               position=self.db_om.read_px(str(i)).index(str(k))
               data_u.append(self.db_os.read_px(str(i))[position])
       
      
        

       return self.view_o.sort_mit_weit(data_o,data_u,len(data_o))


    @cherrypy.expose
    # -------------------------------------------------------
    def sort_weit_mit(self,data):
      #
       data_o=[]
      #suchen der Nummer der Weiterbildung
       length=int(self.di_o2.read_px())
       for i in range(1,length+2):
          if  self.db_o2.read_px(str(i))!=None:
            if self.db_o2.read_px(str(i))[0] in data:
               break
    #selektion welcher Mitarbeiter erfolg abgeschlossen ist
       nummer=i
       length=int(self.di_om.read_px())
       for k in range(1,length+2):
           if self.db_o.read_px(str(k))!=None and str(nummer) in self.db_om.read_px(str(k)):
               position=self.db_om.read_px(str(k)).index(str(nummer))
               if self.db_os.read_px(str(k))[position]=="erfolg":
                   data_o.append(self.db_o.read_px(str(k)))
        

       return self.view_o.sort_weiterbildung_mit(data_o,len(data_o))

    @cherrypy.expose
    # -------------------------------------------------------
    def sort_mitarbeiter(self):
        #selektion aller Mitarbeiter 
        l = []
        length=int(self.di_o1.read_px())
        for i in range(1,length+2):
            if self.db_o.read_px(str(i))!=None:
              l.append(self.db_o.read_px(str(i)))
       #Sortierung alpfabetisch im bezug der Name 
        l.sort(key=lambda x: x[1])
        length=len(l)

        return self.view_o.sort_mit(l,length)


    @cherrypy.expose
    # -------------------------------------------------------
    def sort_weiterbildung(self):
        #Selektiert alpfabetisch der Weiterbildungen

        l = []
        length=int(self.di_o2.read_px())
        for i in range(1,length+2):
          if self.db_o2.read_px(str(i))!=None:
            l.append(self.db_o2.read_px(str(i)))

        l.sort(key=lambda x: x[0])
        length=len(l)
        return self.view_o.sort_weiterbildung(l,length)  


    @cherrypy.expose
    # -------------------------------------------------------
    def sort_zertifikate(self):
        #Selektiert alpfabetisch der Weiterbildungen

        l = []
        length=int(self.di_o2.read_px())
        for i in range(1,length+2):
          if self.db_o2.read_px(str(i))!=None:
            l.append(self.db_o2.read_px(str(i)))

        l.sort(key=lambda x: x[6])
        length=len(l)
        return self.view_o.sort_zertifikate(l,length)        



    def mit_list(self, id_w, id_m):
        # -------------------------------------------------------
        #data zeigt die Mitarbeiterliste ,wo die ID seiner Weiterbildungen gespeichert werden
        #data_w umgekehert von data
        data = self.db_om.read_px(id_m)
        data_w = self.db_ow.read_px(id_w)
        data_o = []
        data_u = []

       #wenn data glecih None ist dann eine neune Mitarbeiter Objekt(der Id von Weiterbildungen enthählt) erschaffen
        if data == None:
       
         data_o.append(id_w)
         self.db_om.create_px(data_o)
       #sonst wird data zu data_o übergeben und nachher wird die ID der neune Weiterbildung hinzugefügt
        else:
               data_o = data

               data_o.append(str(id_w))
              
               self.db_om.update_px(str(id_m), data_o)
       #dasselbe Prozedur wie oben aber für die Weiterbildungen ,die ID von Mitarbeiter enthalten
        if data_w == None:
         
            data_u.append(id_m)
            self.db_ow.create_px(data_u)
           
        else:
            data_u = data_w
            data_u.append(str(id_m))

            self.db_ow.update_px(str(id_w), data_u)
       #
        
        #einlesen der status der Mitarbieter mit id_m 
        #wenn solche List leer ist ,dann wird eine neuen gemacht
        #sonst wird "teilnehmen " hinzugefügt und dann die update Funktion gewählt
        d=self.db_os.read_px(id_m)
       
        
        if(d!=None):  
           d.append("teilnehmen")
          
           self.db_os.update_px(id_m,d)
          
           
        else:
         
           d=[]
           d.append("teilnehemen")
           self.db_os.create_px(d)

        return  self.baba(id_m)

       
    def angemeldet(self):
        return self.view_o.angemeldet()

    
    @cherrypy.expose
    # -------------------------------------------------------
    def mit_id(self, id_w, id_m):
        print(id_m)
        print(id_w)

        return self.mit_list(id_w, id_m)

   

    @cherrypy.expose
    # -------------------------------------------------------
    def index_2(self):
        # -------------------------------------------------------
       
        return self.createList_p()

    @cherrypy.expose
    # -------------------------------------------------------
    def index_3(self):
        # -------------------------------------------------------
      
        return self.createList_p2()

    @cherrypy.expose
    # -------------------------------------------------------
    def alt(self):
        # ----------------------the_app = app() ---------------------------------
      
        return self.createList_p()

    @cherrypy.expose
    def add_qual(self,data,id):
        # ----------------------the_app = app() ---------------------------------
        
        return self.createForm_qual(data,id)    

    @cherrypy.expose
    # -------------------------------------------------------
    def status_alt(self, data,mit):
        # -------------------------------------------------------
      #counter nimmt die Max ID der Weiterbildungen
      #data ist die Weiterbildung und mit diesen Schleife kann man sehen
      #welche ID diese Weiterbildung hat
       counter=int(self.di_o2.read_px())
       for i in range(1,counter+2):
         if self.db_o2.read_px(str(i))!=None:  
           if self.db_o2.read_px(str(i))[0] in data:
               break
                 
       #dann wird die position diese Weiterbildung an Welcher stelle 
       #inder Mitarbeiterliste gespeuchert wird
       #dann wird die alte status entfernt und eine neue hinzugefügt
       position=self.db_om.read_px(mit).index(str(i))

       data=self.db_os.read_px(mit)
       data.pop(position)
       data.insert(position,"stoniert")
       self.db_os.update_px(mit,data)
        

       return self.createweiter(mit)



    @cherrypy.expose
    def mitarbeiter(self):
        # -------------------------------------------------------

        return self.createMitList()

    @cherrypy.expose
    def weit(self):
        # -------------------------------------------------------
        
        return self.createWeitList()

    @cherrypy.expose
    def brechen(self,data_o):
        # -------------------------------------------------------
        
        c=int(self.di_o2.read_px())
       
        for l in range(1,c+2):
            if self.db_o2.read_px(str(l))!= None and self.db_o2.read_px(str(l))[0] in data_o:
                break

        nummer=l
        data=[]
        counter=int(self.di_o1.read_px())
        for i in range(1,counter+2):
           
          if str(i) in self.db_ow.read_px(str(nummer)):            
            if self.db_o.read_px(str(i))!=None:
                data.append(self.db_o.read_px(str(i)))
            

        j=len(data)
        
        return self.view_o.create_brechen(data,data_o,j)     


    @cherrypy.expose
    def zeige_mit(self,data_o):
        # -------------------------------------------------------
        #c in der MaxID der Witerbildungen
        #data_o ist der Array der Weiterbildung
        #mit dieser Schleife sucht man welche INdex diese Weiterbildugn hat
        c=int(self.di_o2.read_px())
       
        for l in range(1,c+2):
            if self.db_o2.read_px(str(l))!= None and self.db_o2.read_px(str(l))[0] in data_o and  self.db_o2.read_px(str(l))[1] in data_o:
                ppppp=self.db_o2.read_px(str(l))[0]
                break

        
        data=[]
        #mit der nächste Schleife Selektiert man die Mitarbeiter deren Status 
        #verändert wird
        counter=int(self.di_o1.read_px())
        for i in range(1,counter+2):

          if str(i) in self.db_ow.read_px(str(l)):            
            if self.db_o.read_px(str(i))!=None:
                data.append(self.db_o.read_px(str(i)))
           

        j=len(data)
        return self.view_o.create_zeige_mit(data,data_o,j)    

    @cherrypy.expose
    # -------------------------------------------------------
    def add(self):
        # -------------------------------------------------------
        return self.createForm_p()


    @cherrypy.expose
    # -------------------------------------------------------
    def change_status(self,id,data_u,p,data_o):
        # -------------------------------------------------------
        #data_o ist array der Mitarbeiter
        #data_u Array der Weiterbildung
        #id ist id der Mitarbeiter
        #P ist 
        #erste Schleife entnimmt die ID der Mitarbeiter
        #zweite der Id der Weiterbildung
        counter=int(self.di_o1.read_px())
        for k in range(1,counter+2):
            if self.db_o.read_px(str(k)):
               if self.db_o.read_px(str(k))[0] in data_o:
                break
        
        mit_id=k

        counter=int(self.di_o2.read_px())
        for i in range(1,counter+2):
            if self.db_o2.read_px(str(i))and self.db_o2.read_px(str(i))[0] in data_u:
                break

        variable=i
       
        
      
        position=self.db_om.read_px(str(k)).index(str(variable))
        data=self.db_os.read_px(str(k))
        data.pop(position)
        if int(p)==1:
         data.insert(position,"erfolg")
        elif int(p)==2:
            data.insert(position,"kein erfolg")
        else:
             data.insert(position,"abbrechen")
             self.db_os.update_px(str(k),data)
             return self.brechen(data_u)
        self.db_os.update_px(str(k),data)
           
                
        return self.zeige_mit(data_u)


    @cherrypy.expose
    # -------------------------------------------------------
    def add2(self):
        # -------------------------------------------------------
        return self.createForm_p2()

    # -----------------------------
    @cherrypy.expose
    def delete(self, id):
        #die Mitarbeiter mit diesem ID wird gelöscht 
    
        self.db_o.delete_px(id)
        
        raise cherrypy.HTTPRedirect('/')

    @cherrypy.expose
    def delete_2(self, id):
        self.db_o2.delete_px(id)
        
        raise cherrypy.HTTPRedirect('/')

# ------------------------------------

    @cherrypy.expose
    # -----------------------------------------------------
    def baba(self,i):
       
     return self.create(i)

    @cherrypy.expose
    # -------------------------------------------------------
    def anzeigen_weit(self, id_spl, data_o):
       

        return self.createAnzeigeList_2(id_spl)

    @cherrypy.expose
    # -------------------------------------------------------
    def index(self):
        index_1 = len(self.db_o.read_px())             #lesen der Teilnehmer Anzahl
        index_2 = len(self.db_o2.read_px())            #lesen Weiterbildung Anzahl
        return self.start_seite(index_1, index_2)

    @cherrypy.expose
    # -------------------------------------------------------
    def edit(self, id_spl):
        # -------------------------------------------------------
        return self.createForm_p(id_spl)

    @cherrypy.expose
    # -------------------------------------------------------
    def w(self, id):
        # -------------------------------------------------------
        print("w")
        print(id)
        return self.createweiter(id)

    @cherrypy.expose
    def edit_2(self, id_spl):
        # -------------------------------------------------------
        return self.createForm_p2(id_spl)

    @cherrypy.expose
    # -------------------------------------------------------
    def save(self, id_spa, name1_spa, vorname1_spa, akad_spa, tat_spa):
        # -------------------------------------------------------
        #data speichert die Eingabe Information 
        #im Bezug darauf ob die ID shon vorhanden ist wird entweder update oder create gewählt
        id_s = id_spa
        data_a = [name1_spa, vorname1_spa, akad_spa, tat_spa]
        if id_s != "None":
            self.db_o.update_px(id_s, data_a)
        else:
            self.db_o.create_px(data_a)
        return self.createList_p()

    @cherrypy.expose
    def save2(self, id_spa, bezeichnung_spa, von_spa, bis_spa, beschreibung_spa, max_spa, min_spa,zer_besch,zer_bez):
        # -------------------------------------------------------
         #data speichert die Eingabe Information 
        #im Bezug darauf ob die ID shon vorhanden ist wird entweder update oder create gewählt
        id_s = id_spa
       
        data_a2 = [bezeichnung_spa, von_spa, bis_spa, beschreibung_spa,
                   max_spa, min_spa,zer_besch,zer_bez]
        if id_s != "None":
            self.db_o2.update_px(id_s, data_a2)
        else:
            self.db_o2.create_px(data_a2)
       
        return self.createList_p2()



    @cherrypy.expose
    # -------------------------------------------------------
    def save_qual(self, id_w,beschreibung_qual,bis_qual):
        #speichert information über Qualifikation

        data=[beschreibung_qual,bis_qual]
       
        if id_w != "None":
           data_o=[]
           data_o=self.db_oqiw.read_px(id_w)

           variable=len(self.db_osq.read_px())
           #wird für Erschaffung von die einzelnen Qualifikationen genutzt
           #wenn keine Qualifikationen vorhanden sind dann wird create genutzt
           #sonst wird die neue Data hinzugefügt und mit update Aktualiesiert
           if variable==0:

                self.db_osq.create_px(data)
           elif self.db_osq.read_px(str(variable)):
                  self.db_osq.create_px(data)
           else:
                self.db_osq.update_px(variable,data)    
           #wird für die Erschafung von die Qualfikationen in den Weiterbildungen genutzt
           if data_o==None:
                data_o=[]
                data_o.append(data)
                self.db_oqiw.create_px(data_o)
           else:    
             data_o.append(data)
             self.db_oqiw.update_px(id_w,data_o)
        
        else:
            self.db_osq.create_px(data)
            self.db_oqiw.create_px(data)
            counter=len(self.db_osq.read_px())
        return self.createAnzeigeList_2(id_w)

    @cherrypy.expose
    # -------------------------------------------------------
    def default(self, *arguments, **kwargs):
        # -------------------------------------------------------
        msg_s = "unbekannte Anforderung: " + \
            str(arguments) + \
            ' ' + \
            str(kwargs)
        raise cherrypy.HTTPError(404, msg_s)
    default.exposed = True

    # -------------------------------------------------------
    def createList_p(self):
        # -------------------------------------------------------
        #leses alle Mitarbeiter und an den template übergeben
        data_o = self.db_o.read_px()
        return self.view_o.changeList_px(data_o)

    def createList_p2(self):
        # -------------------------------------------------------
        #lesen von alle Weiterbildungen 
        data_o = self.db_o2.read_px()
       
        return self.view_o.createList_px2(data_o)

    def createMitList(self):
        # -------------------------------------------------------
        #erstellt List mit der Mitarbeiter und Link zu deren Namen
        data_o = self.db_o.read_px()
        return self.view_o.createMitList(data_o)


   


    def pro_2(self):
        data_o = []
        proba = int(self.di_o2.read_px())

        i = 1
        for i in range(proba+2):
            if self.db_o2.read_px(str(i)) != None and self.db_o2.read_px(str(i))[1] < "2020-11-22" and self.db_o2.read_px(str(i))[2] > "2020-11-22":
                data_o.append(self.db_o2.read_px(str(i)))

        self.data.setListType(data_o)
        return data_o

    def pro_3(self):
        data_o = []
        proba = int(self.di_o2.read_px())
        for i in range(proba+2):
            if self.db_o2.read_px(str(i)) != None and self.db_o2.read_px(str(i))[1] > "2020-11-22":
                data_o.append(self.db_o2.read_px(str(i)))

        return data_o

    def pro_4(self):
        data_o = []
        proba = int(self.di_o2.read_px())
        for i in range(proba+2):
            if self.db_o2.read_px(str(i)) != None :
              if self.db_o2.read_px(str(i))[1] < "2020-11-22": 
                if self.db_o2.read_px(str(i))[2] < "2020-11-22":
                 data_o.append(self.db_o2.read_px(str(i)))

        return data_o





















    
    def createweiter(self, id):
      
      #id ist nummer Mitarbeiter
    
        data_u=[]
        p=[]
        proba=[]
    
        i=len(p)
        data_o=[]
        #lesen der Max ID der Weiterbildungen
        counter=int(self.di_o2.read_px())
        for l in range(1,counter+2):
             #prüft ob die Weiterbildung shon be dieser Mitarbeiter gespecihert wird
             #wenn das der Fall ist wurde die position gesucht und im Bezug darauf die 
             #status entnommen
          if self.db_o2.read_px(str(l))!=None:   
            if  str(l) in self.db_om.read_px(id):
               data_o.append(self.db_o2.read_px(str(l)))
               result= self.db_om.read_px(id).index(str(l))
               p.append(self.db_os.read_px(id)[result])
              
        #goschonimmet die maxID des 
        #prüft ob solche Weiterbildung existiert und ob die geplannt ist
        gosho=len(self.db_o2.read_px())
        for k in range(1,gosho+2):
         if self.db_o2.read_px(str(k)) !=None and self.db_o2.read_px(str(k))[1] > "2020-11-22" :
           data_u.append(self.db_o2.read_px(str(k)))
          
        #wenn data_u None ist wird die Default Wert genommen
        # l Länge von geplannten Weiterbildung
        #i Länge von die andere Weiterbildungnen
        if data_u==[]:
            l=0
            data_u=self.db_o2.getDefault_px()
        else:l=len(data_u) 
        i=len(data_o)  
       
        return self.view_o.weit(data_u,data_o,i, id,p,l)





    def createWeitList(self):
        # -------------------------------------------------------
        #pro_2 selektiert die laufenden Weiterbildungen
        #pro_3 die geplannten Witerbildungen
        #pro_4 die abgeschlossen Weiterbildungen
        data_o = self.pro_2()
        print(data_o)
        data_u = self.pro_3()
        print(data_u)
        data_a = self.pro_4()
        print(data_a)
        i = len(data_o)
        print(i)
        i_2 = len(data_u)
        i_3 = len(data_a)
        return self.view_o.createWeiter(data_o, data_u, data_a, i, i_2, i_3)





    


    def create(self, pesho):
        # -------------------------------------------------------
       #pesho ist variable für die id des Mitarbeiter
        data_zer=[] #list für die zertifikaten
        data = self.db_om.read_px(pesho) #liest der von den List ,welche Weiterbildung ID in dieser Mitarbeiter mir variable pescho vorhanden sind
      
        data_st=[] #list für status
       
        if data == None:
            data = self.db_om.getDefault_px() #wenn die liste leer ist ,wird eine default wert entnehmen
        
        else:
            data = [] 
            #die Anzahl der Weiterbildungen wird entnehmen und wird mit 1 inkrmentiert damit man auf die letzte elemen zugreifen kann
            #und nochmal mit 1 falls die maxId der Weiterbildungen nicht zurecht aktualiesiert ist
            for i in range(int(self.di_o2.read_px())+2): 
                #erste if überprüft ob diese Weiterbildung vothanden ist 
                #zweite prüft ob der Mitarbeiter für diese Weiterbildung angemeldet ist
                if self.db_o2.read_px(str(i)) != None and str(i) in self.db_om.read_px(pesho):
                    #Wenn dass der Fall ist wird diese Weiterbildung gespeichert
                    data.append(self.db_o2.read_px(str(i)))
                    #dann wird die position wo die Weiterbildung in der Mitarbeiterliste gespeichert wird
                    #dann wird die status gespeichert weil die Reihenfolge dasselbe ist
                    position=self.db_om.read_px(pesho).index(str(i))
                    if self.db_os.read_px(pesho):
                      data_st.append(self.db_os.read_px(pesho) [position])
                    #wenn der Status erfolg ist dann wird die Name der Zertifikate gezeigt
                    #Sonst wird "noch keine Zertifikate geschrieben"
                      if self.db_os.read_px(pesho)[position]=="erfolg":
                         data_zer.append(self.db_o2.read_px(str(i))[6])
                      else:
                         data_zer.append("noch keine")    
                    else:
                        data_zer.append("noch keine") 
         #counter zeigt die die Größe von den gespeichrte Daten               
        if(data == self.db_om.getDefault_px()):
           
            counter = 0
        else:
            counter = len(data)
        #in data_o werden alle andere Weiterbildungen gezeigt an dennen die Mitarbeiter sicha anmelden kann
        data_o = self.db_o2.read_px()
       
       
        return self.view_o.createAnzeigeList(data, data_o, counter, pesho,data_st,data_zer)

    def createAnzeigeList_2(self, id):
        # -------------------------------------------------------
        #data_o liest die Qualifikationen in Weiterbildung mit ID
        #data_p liest die Weiterbildungen wo auch die Zertifikate gespeichert werden
        data_o=self.db_oqiw.read_px(str(id))
        data_p=self.db_o2.read_px(str(id))
        #wenn es diese Weitebildung keine Qualifikationen hat dann wird die Default wert genommen
        #i ist der Anzahl der Qualifikationen
        if data_o==None or data_o==0:
            data=self.db_osq.getDefault_px()
            i=0
        else:
            i=len(self.db_oqiw.read_px(id))
            

            
            
        return self.view_o.createAnzeigeList_2(data_o,i,id,data_p)

    # -------------------------------------------------------
    def createStart(self, id_spl=None):
        # -------------------------------------------------------
        if id_spl != None:
            data_o = self.db_o.read_px(id_spl)
        else:
            data_o = self.db_o.getDefault_px()
        return self.view_o.createStart()

    def createForm_p(self, id_spl=None):
        # -------------------------------------------------------
        #wenn die id ist anders als None wird die mitarbeiter mot diesen nummer
        #gelesen ,sonst wird die Default Frome genommen
        if id_spl != None:
            data_o = self.db_o.read_px(id_spl)
        else:
            data_o = self.db_o.getDefault_px()
        return self.view_o.createForm_px(id_spl, data_o)

    def createForm_p2(self, id_spl=None):
        # -------------------------------------------------------
        #wenn die id ist anders als None wird die mitarbeiter mot diesen nummer
        #gelesen ,sonst wird die Default Frome genommen
        if id_spl != None:
            data_o2 = self.db_o2.read_px(id_spl)
        else:
            data_o2 = self.db_o2.getDefault_px()
        return self.view_o.createForm_px2(id_spl, data_o2)


    def createForm_qual(self,data,id_spl=None):
        # -------------------------------------------------------
        #wenn die id ist anders als None wird die mitarbeiter mot diesen nummer
        #gelesen ,sonst wird die Default Frome genommen
        #zweite if prüft ob die Qualifikation existiert ,wenn das nicht der Fall ist wird eine Default Wert genommen
        if id_spl != None:
            data_o = self.db_osq.read_px(id_spl)
            if data_o==None:
                data_o=self.db_osq.getDefault_px()
        else:
            data_o = self.db_osq.getDefault_px()
        return self.view_o.createForm_qual(id_spl, data_o)



    def start_seite(self, index_1, index_2):
        # -------------------------------------------------------

        return self.view_o.start_seite(index_1, index_2)

  


# EOF
