# coding: utf-8

# Demonstrator / keine Fehlerbehandlung

import cherrypy

from .database import Database_Qual_cl, Database_Qual_in_weit_cl, Database_Status_cl, Database_Mitarbeiter_cl, Database_weit_mit_cl
from .database import Database_mit_weit_cl
from .database import Database_weit_cl
from .dataid import DataId_cl, DataId_weit_cl
from .dataid import Dataid_Qual_cl
from .view import View_cl
import codecs
import json

from app import dataid


# Method-Dispatching!

# Übersicht Anforderungen / Methoden


class COUNT_Total(object):
    exposed=True
    def __init__(self):
        self.mit=DataId_cl()
        self.weit=DataId_weit_cl()
        self.view_o = View_cl()
        self.mitt=Database_Mitarbeiter_cl()

    def GET(self,id=None):
       mitarbeiter=len(self.mitt.read_px())
       weiterbildung=self.weit.read_px()
       result=[]
       result.append(mitarbeiter)
       result.append(weiterbildung)
       return self.view_o.createList_px(result)       






class WEIT_IN_STATUS(object):
    
    exposed = True  # gilt für alle Methoden

    def __init__(self):

        # spezielle Initialisierung können hier eingetragen werden
        self.db_o = Database_weit_cl()
        self.view_o = View_cl()
        self.status = Database_Status_cl()
        self.mit_weit = Database_mit_weit_cl()
        self.di_o = DataId_weit_cl()
        self.mit = Database_Mitarbeiter_cl()
        self.weit = DataId_weit_cl()
        self.mitid = DataId_cl()
        self.weit_mit = Database_weit_mit_cl()

    def GET(self, id=None):

        retVal_s = self.getDetail_p(id)

        return retVal_s

    def POST(self, data):

        fp_o = codecs.open('data/erfolgid.json', 'r', 'utf-8')
        mit = json.load(fp_o)
        proba = self.mit_weit.read_px()
        for k in range(0, int(self.mitid.read_px())):
    
            if proba[k] != None:
                if int(str(proba[k]["mit_id"])) == int(mit):
                    proba = proba[k]
                    break
        indeX = proba["weiterbildung"].index(data[0])

        proba_status = self.status.read_px()
        i = 0
        for i in range(0, int(self.mitid.read_px())):
            if str(proba_status[i]["mit_id"]) == str(mit):
                proba_status = proba_status[i]
                break

        proba_status["status"].pop(indeX)
        if str(data[2]) == "e":
            proba_status["status"].insert(indeX, "erfolg")
        elif str(data[2]) == "k":
            proba_status["status"].insert(indeX, "kein erfolg")
        elif str(data[2]) == "s":
            proba_status["status"].insert(indeX, "stoniert")
        elif str(data[2]) == "a":
            proba_status["status"].insert(indeX, "angebrochen")

        proba = self.status.read_px()
        proba.pop(i)
        proba.insert(i, proba_status)
        with codecs.open('data/status.json', 'w', 'utf-8') as fp_o:
            json.dump(proba, fp_o, indent=3)

        return

    def PUT(self, data):

        self.db_o.update_px(data)

        return

    def DELETE(self, id):

        self.db_o.delete_px(id)
        self.status.delete_px(id)
        self.mit_weit.delete_px(id)
        return

    def getList_p(self):

        temp = []
        before = []

        temp = self.db_o.read_px()

        for i in range(0, int(self.di_o.read_px())):
            temp = self.db_o.read_px(str(i))

            if temp["id"] != None:

                if temp["col2"] < "2021-01-14" and temp["col3"] < "2021-01-14":
                    before.append(temp)

        return self.view_o.createList_px(before)

    def getDetail_p(self, id_spl):
        fp_o = codecs.open('data/erfolgid.json', 'w', 'utf-8')
        json.dump(id_spl, fp_o)

        mit_weit=self.mit_weit.read_px()
        weitId=self.di_o.read_px()
        weiterbildung=self.db_o.read_px()
        result=[]
        for i in range(0,len(mit_weit)+1):
            if str(id_spl)==str(mit_weit[i]["mit_id"]):
               mit_weit=mit_weit[i]
               break

        for k in range(0,int(weitId)+1):
            if str(k) in mit_weit["weiterbildung"]:
                for j in range(0,len(weiterbildung)+1):
                    if str(weiterbildung[j]["id"])==str(k):
                      result.append(weiterbildung[j])
                      break

        return self.view_o.createDetail_px(result)












class Erfolg(object):

    exposed = True  # gilt für alle Methoden

    def __init__(self):

        # spezielle Initialisierung können hier eingetragen werden
        self.db_o = Database_weit_cl()
        self.view_o = View_cl()
        self.status = Database_Status_cl()
        self.mit_weit = Database_mit_weit_cl()
        self.di_o = DataId_weit_cl()
        self.mit = Database_Mitarbeiter_cl()
        self.weit = DataId_weit_cl()
        self.mitid = DataId_cl()
        self.weit_mit = Database_weit_mit_cl()

    def GET(self, id=None):

        retVal_s = self.getDetail_p(id)

        return retVal_s

    def POST(self, data):

        proba = self.mit_weit.read_px()
        for k in range(0, int(self.mitid.read_px())):

            if proba[k] != None:
                if int(str(proba[k]["mit_id"])) == int(str(data[0])):
                    proba = proba[k]
                    break
        fp_o = codecs.open('data/erfolgid.json', 'r', 'utf-8')
        weit = json.load(fp_o)
        indeX = proba["weiterbildung"].index(weit)

        proba_status = self.status.read_px()
        i = 0
        for i in range(0, int(self.mitid.read_px())):
            if str(proba_status[i]["mit_id"]) == str(data[0]):
                proba_status = proba_status[i]
                break

        proba_status["status"].pop(indeX)
        if str(data[2]) == "e":
            proba_status["status"].insert(indeX, "erfolg")
        elif str(data[2]) == "k":
            proba_status["status"].insert(indeX, "kein erfolg")
        elif str(data[2]) == "s":
            proba_status["status"].insert(indeX, "stoniert")
        elif str(data[2]) == "a":
            proba_status["status"].insert(indeX, "angebrochen")

        proba = self.status.read_px()
        proba.pop(i)
        proba.insert(i, proba_status)
        with codecs.open('data/status.json', 'w', 'utf-8') as fp_o:
            json.dump(proba, fp_o, indent=3)

        return

    def PUT(self, data):

        self.db_o.update_px(data)

        return

    def DELETE(self, id):

        self.db_o.delete_px(id)
        self.status.delete_px(id)
        self.mit_weit.delete_px(id)
        return

    def getList_p(self):

        temp = []
        before = []

        temp = self.db_o.read_px()

        for i in range(0, int(self.di_o.read_px())):
            temp = self.db_o.read_px(str(i))

            if temp["id"] != None:

                if temp["col2"] < "2021-01-14" and temp["col3"] < "2021-01-14":
                    before.append(temp)

        return self.view_o.createList_px(before)

    def getDetail_p(self, id_spl):

        fp_o = codecs.open('data/erfolgid.json', 'w', 'utf-8')
        json.dump(id_spl, fp_o)

        data = self.weit_mit.read_px()
        weiterbildung = []
        mitarbeiter = []
        proba = self.mitid.read_px()
        for i in range(0, int(self.mitid.read_px())):
            if len(self.db_o.read_px()) != 0:
                proba = data[i]["weiterbildung"]
                if str(data[i]["weiterbildung"]) == str(id_spl):
                    weiterbildung = data[i]
                    break
        c = 0
        for i in range(0, int(self.mitid.read_px())+1):
            if str(i) in weiterbildung["mit"]:
                proba = self.mit.read_px()
                for k in range(0, int(self.mitid.read_px())):
                    if proba[k]["id"] == str(i):
                        c = k
                        break
                mitarbeiter.append(self.mit.read_px(str(c)))

        return self.view_o.createDetail_px(mitarbeiter)


class Hronologisch_weit(object):

    exposed = True  # gilt für alle Methoden

    def __init__(self):

        # spezielle Initialisierung können hier eingetragen werden
        self.db_o = Database_weit_cl()
        self.view_o = View_cl()
        self.status = Database_Status_cl()
        self.mit_weit = Database_mit_weit_cl()
        self.di_o = DataId_weit_cl()
        self.mit_weit = Database_mit_weit_cl()

    def GET(self, id=None):

        retVal_s = self.getDetail_p(id)

        return retVal_s

    def POST(self, data):

        self.db_o.create_px(data)

        return

    def PUT(self, data):

        self.db_o.update_px(data)

        return

    def DELETE(self, id):

        self.db_o.delete_px(id)
        self.status.delete_px(id)
        self.mit_weit.delete_px(id)
        return

    def getDetail_p(self, id_spl):

        data_o = []
        data = []
        proba = self.mit_weit.read_px()

        for k in range(0, len(self.mit_weit.read_px())+1):
            if str(proba[k]["mit_id"]) == str(id_spl):
                data_o = self.mit_weit.read_px(k)
                break

        for i in range(0, int(self.di_o.read_px())+1):
            if str(i) in data_o["weiterbildung"]:
                proba = self.db_o.read_px()
                for k in range(0, len(proba)+1):
                    if str(proba[k]["id"]) == str(i):
                        data.append(self.db_o.read_px(i))
                        break

        data.sort(key=lambda x: x["col2"])

        return self.view_o.createDetail_px(data)


class Erfolg_teihnemher(object):

    exposed = True  # gilt für alle Methoden

    def __init__(self):

        # spezielle Initialisierung können hier eingetragen werden
        self.db_o = Database_weit_cl()
        self.view_o = View_cl()
        self.status = Database_Status_cl()
        self.mit_weit = Database_mit_weit_cl()
        self.di_o = DataId_weit_cl()
        self.mit_weit = Database_mit_weit_cl()
        self.weit_mit = Database_weit_mit_cl()
        self.mit = Database_Mitarbeiter_cl()
        self.mit_id = DataId_cl()

    def GET(self, id=None):

        #retVal_s = self.getDetail_p(id)
        weit_mit = self.weit_mit.read_px()
        mit = self.mit.read_px()
        mit_weit = self.mit_weit.read_px()
        # status=self.status.read_px()
        result = []
        for k in range(0, len(weit_mit)+1):
            if str(weit_mit[k]["weiterbildung"]) == str(id):
                for i in range(0, int(self.mit_id.read_px())+1):
                    if str(i) in weit_mit[k]["mit"]:
                        for j in range(0, len(mit_weit)+1):
                            if mit_weit[j]["mit_id"] == str(i):
                                indeX = mit_weit[j]["weiterbildung"].index(str(id))
                                if str(self.status.read_px(j)["status"][indeX]) == "erfolg":
                                    for p in range(0, len(mit)+1):
                                        if mit[p]["id"] == mit_weit[j]["mit_id"]:
                                            result.append(mit[p])
                                            break
                                break
            break

        return self.view_o.createDetail_px(result)

    def POST(self, data):

        self.db_o.create_px(data)

        return

    def PUT(self, data):

        # self.db_o.create_px(data)
        self.db_o.update_px(data)

        return

    def DELETE(self, id):

        self.db_o.delete_px(id)
        self.status.delete_px(id)
        self.mit_weit.delete_px(id)
        return


class Weiterbildung_auswertung_cl(object):

    exposed = True  # gilt für alle Methoden

    def __init__(self):

        # spezielle Initialisierung können hier eingetragen werden
        self.db_o = Database_weit_cl()
        self.view_o = View_cl()
        self.status = Database_Status_cl()
        self.mit_weit = Database_mit_weit_cl()
        self.di_o = DataId_weit_cl()

    def GET(self):

        retVal_s = ''

        retVal_s = self.getList_p()

        return retVal_s

    def POST(self, data):

        self.db_o.create_px(data)

        return

    def PUT(self, data):

        self.db_o.update_px(data)

        return

    def DELETE(self, id):

        self.db_o.delete_px(id)
        self.status.delete_px(id)
        self.mit_weit.delete_px(id)
        return

    def getList_p(self):

        temp = []
        before = []

        temp = self.db_o.read_px()

        for i in range(0, int(self.di_o.read_px())):
            temp = self.db_o.read_px(str(i))

            if temp["id"] != None:

                if temp["col2"] < "2021-01-14" and temp["col3"] < "2021-01-14":
                    before.append(temp)

        return self.view_o.createList_px(before)

    def getDetail_p(self, id_spl):

        data_o = self.db_o.read_px(id_spl)
        return self.view_o.createDetail_px(data_o)


class Mitarbeiter_sort(object):

    exposed = True  # gilt für alle Methoden

    def __init__(self):

        # spezielle Initialisierung können hier eingetragen werden
        self.db_o = Database_weit_cl()
        self.view_o = View_cl()
        self.status = Database_Status_cl()
        self.mit_weit = Database_mit_weit_cl()
        self.di_o = DataId_weit_cl()
        self.mit = Database_Mitarbeiter_cl()

    def GET(self):

        retVal_s = ''

        retVal_s = self.getList_p()

        return retVal_s

    def POST(self, data):

        self.db_o.create_px(data)

        return

    def PUT(self, data):

        self.db_o.update_px(data)

        return

    def DELETE(self, id):

        self.db_o.delete_px(id)
        self.status.delete_px(id)
        self.mit_weit.delete_px(id)
        return

    def getList_p(self):

        mitarbeiter = self.mit.read_px()

        mitarbeiter.sort(key=lambda x: x["col1"])

        return self.view_o.createList_px(mitarbeiter)

    def getDetail_p(self, id_spl):

        data_o = self.db_o.read_px(id_spl)
        return self.view_o.createDetail_px(data_o)


class Weiterbildung_sort(object):

    exposed = True  # gilt für alle Methoden

    def __init__(self):

        # spezielle Initialisierung können hier eingetragen werden
        self.db_o = Database_weit_cl()
        self.view_o = View_cl()
        self.status = Database_Status_cl()
        self.mit_weit = Database_mit_weit_cl()
        self.di_o = DataId_weit_cl()
        self.mit = Database_Mitarbeiter_cl()

    def GET(self):

        retVal_s = ''

        retVal_s = self.getList_p()

        return retVal_s

    def POST(self, data):

        self.db_o.create_px(data)

        return

    def PUT(self, data):

        self.db_o.update_px(data)

        return

    def DELETE(self, id):

        self.db_o.delete_px(id)
        self.status.delete_px(id)
        self.mit_weit.delete_px(id)
        return

    def getList_p(self):

        mitarbeiter = self.db_o.read_px()

        mitarbeiter.sort(key=lambda x: x["col1"])

        return self.view_o.createList_px(mitarbeiter)

    def getDetail_p(self, id_spl):

        data_o = self.db_o.read_px(id_spl)
        return self.view_o.createDetail_px(data_o)


class Zertifikate_sort(object):

    exposed = True  # gilt für alle Methoden

    def __init__(self):

        # spezielle Initialisierung können hier eingetragen werden
        self.db_o = Database_weit_cl()
        self.view_o = View_cl()
        self.status = Database_Status_cl()
        self.mit_weit = Database_mit_weit_cl()
        self.di_o = DataId_weit_cl()
        self.mit = Database_Mitarbeiter_cl()

    def GET(self):

        retVal_s = ''

        retVal_s = self.getList_p()

        return retVal_s

    def POST(self, data):

        self.db_o.create_px(data)

        return

    def PUT(self, data):

        self.db_o.update_px(data)

        return

    def DELETE(self, id):

        self.db_o.delete_px(id)
        self.status.delete_px(id)
        self.mit_weit.delete_px(id)
        return

    def getList_p(self):

        mitarbeiter = self.db_o.read_px()

        # mitarbeiter=json.loads(mitarbeiter)
        mitarbeiter.sort(key=lambda x: x["col7"])

        return self.view_o.createList_px(mitarbeiter)

    def getDetail_p(self, id_spl):

        data_o = self.db_o.read_px(id_spl)
        return self.view_o.createDetail_px(data_o)


class Weiterbildung_aktiv_cl(object):

    exposed = True  # gilt für alle Methoden

    def __init__(self):

        # spezielle Initialisierung können hier eingetragen werden
        self.db_o = Database_weit_cl()
        self.view_o = View_cl()
        self.status = Database_Status_cl()
        self.mit_weit = Database_mit_weit_cl()
        self.di_o = DataId_weit_cl()

    def GET(self):

        retVal_s = ''

        retVal_s = self.getList_p()

        return retVal_s

    def POST(self, data):

        self.db_o.create_px(data)

        return

    def PUT(self, data):

        self.db_o.update_px(data)

        return

    def DELETE(self, id):

        self.db_o.delete_px(id)
        self.status.delete_px(id)
        self.mit_weit.delete_px(id)
        return

    def getList_p(self):

        temp = []
        before = []

        temp = self.db_o.read_px()

        for i in range(0, int(self.di_o.read_px())):
            temp = self.db_o.read_px(str(i))

            if temp["id"] != None:

                if temp["col2"] < "2021-01-14" and temp["col3"] > "2021-01-14":
                    before.append(temp)

        return self.view_o.createList_px(before)

    def getDetail_p(self, id_spl):

        data_o = self.db_o.read_px(id_spl)
        return self.view_o.createDetail_px(data_o)


class Weiterbildung_after_cl(object):

    exposed = True  # gilt für alle Methoden

    def __init__(self):

        # spezielle Initialisierung können hier eingetragen werden
        self.db_o = Database_weit_cl()
        self.view_o = View_cl()
        self.status = Database_Status_cl()
        self.mit_weit = Database_mit_weit_cl()
        self.di_o = DataId_weit_cl()

    def GET(self):

        retVal_s = ''

        retVal_s = self.getList_p()

        return retVal_s

    def POST(self, data):

        self.db_o.create_px(data)

        return

    def PUT(self, data):

        # self.db_o.create_px(data)
        self.db_o.update_px(data)

        return

    def DELETE(self, id):

        self.db_o.delete_px(id)
        self.status.delete_px(id)
        self.mit_weit.delete_px(id)
        return

    def getList_p(self):

        temp = []
        before = []

        temp = self.db_o.read_px()

        for i in range(0, int(self.di_o.read_px())):
            temp = self.db_o.read_px(str(i))

            if temp["id"] != None:

                if temp["col2"] > "2021-01-14" and temp["col3"] > "2021-01-14":
                    before.append(temp)

        return self.view_o.createList_px(before)

    def getDetail_p(self, id_spl):

        data_o = self.db_o.read_px(id_spl)
        return self.view_o.createDetail_px(data_o)


class Weiterbildung_cl(object):

    exposed = True  # gilt für alle Methoden

    def __init__(self):

        # spezielle Initialisierung können hier eingetragen werden
        self.db_o = Database_weit_cl()
        self.view_o = View_cl()
        self.status = Database_Status_cl()
        self.mit_weit = Database_mit_weit_cl()
        self.qual_weit = Database_Qual_in_weit_cl()

    def GET(self, id=None):

        retVal_s = ''
        if id == 'undefined':
            retVal_s = self.getList_p()

        elif id == None:
            # Anforderung der Liste
            retVal_s = self.getList_p()
        else:
            # Anforderung eines Details
            # Anforderung eines Details
            proba = self.db_o.read_px()

        # ret=self.db_o1.read_px(retVal_s[0])
            i = 0
            for i in range(0, len(proba)):
                if proba[i]["id"] == id:

                    break
            retVal_s = self.getDetail_p(i)

        return retVal_s

    def POST(self, data):

        self.db_o.create_px(data)

        return

    def PUT(self, data):

        # self.db_o.create_px(data)
        self.db_o.update_px(data)

        return

    def DELETE(self, id):

        self.db_o.delete_px(id)
        self.qual_weit.delete_px(id)
        return

    def getList_p(self):

        data_a = self.db_o.read_px()
        # default-Werte entfernen
        #ndata_a = data_a[1:]
        return self.view_o.createList_px(data_a)

    def getDetail_p(self, id_spl):

        data_o = self.db_o.read_px(id_spl)
        return self.view_o.createDetail_px(data_o)


class Mitarbeiter_cl(object):

    exposed = True  # gilt für alle Methoden

    def __init__(self):

        # spezielle Initialisierung können hier eingetragen werden
        self.db_o = Database_Mitarbeiter_cl()
        self.view_o = View_cl()
        self.status = Database_Status_cl()
        self.mit_weit = Database_mit_weit_cl()

    def GET(self, id=None):

        retVal_s = ''

        if id == 'undefined':
            retVal_s = self.getList_p()

        elif id == None:
            # Anforderung der Liste
            retVal_s = self.getList_p()
        else:
            # Anforderung eines Details
            proba = self.db_o.read_px()

        # ret=self.db_o1.read_px(retVal_s[0])
            i = 0
            for i in range(0, len(proba)):
                if proba[i]["id"] == id:

                    break

            retVal_s = self.getDetail_p(i)

        return retVal_s

    def POST(self, data):

        self.db_o.create_px(data)

        return

    def PUT(self, data):

        self.db_o.update_px(data)

        return

    def DELETE(self, id):

        self.db_o.delete_px(id)
        self.status.delete_px(id)
        self.mit_weit.delete_px(id)
        return

    def getList_p(self):

        data_a = self.db_o.read_px()
        # default-Werte entfernen
        #ndata_a = data_a[1:]
        return self.view_o.createList_px(data_a)

    def getDetail_p(self, id_spl):

        data_o = self.db_o.read_px(id_spl)
        return self.view_o.createDetail_px(data_o)


class Status_cl(object):

    exposed = True  # gilt für alle Methoden

    def __init__(self):

        # spezielle Initialisierung können hier eingetragen werden
        self.db_o = Database_Status_cl()
        self.view_o = View_cl()
        self.di_o = dataid.StatusId_cl()
        self.weit = DataId_weit_cl()
        self.mit_weit = Database_mit_weit_cl()
        self.w = Database_weit_cl()

    def GET(self, id=None):

        mitarbeiter = self.getDetail_p(id)

        return mitarbeiter

    def POST(self, data):

        self.db_o.create_px(data)

        return

    def getList_p(self):

        data_a = self.db_o.read_px()
        # default-Werte entfernen
        #ndata_a = data_a[1:]
        return self.view_o.createList_px(data_a)

    def getDetail_p(self, id):

        proba = self.db_o.read_px()
        proba_1 = self.mit_weit.read_px()
        mitarbeiter_status = []
        mitarbeiter_weit = []
        status_ready = []
        Zertifikate = []
        gesamt = []
        # ret=self.db_o1.read_px(retVal_s[0])

        for i in range(0, len(proba)+1):
            if proba[i]["mit_id"] == id:
                mitarbeiter_status = proba[i]
                mitarbeiter_weit = proba_1[i]
                break

        for k in range(0, int(self.weit.read_px())+1):
            if str(k) in mitarbeiter_weit["weiterbildung"]:
                indeX = mitarbeiter_weit["weiterbildung"].index(str(k))

                status_ready.append(mitarbeiter_status["status"][indeX])
                if mitarbeiter_status["status"][indeX] == "erfolg":
                    temp = self.w.read_px()

                    for i in range(0, len(self.w.read_px())):

                        if int(temp[i]["id"]) == k:
                            temp = self.w.read_px(i)
                            break
                    # temp=json.loads(temp)
                    temp = temp["col7"]

                    Zertifikate.append(temp)
                else:
                    Zertifikate.append("keine")

        gesamt.append(status_ready)
        gesamt.append(Zertifikate)

        return self.view_o.createDetail_px(gesamt)


class Mitarbeiter_Weit_cl(object):

    exposed = True  # gilt für alle Methoden

    def __init__(self):

        # spezielle Initialisierung können hier eingetragen werden
        self.db_o = Database_mit_weit_cl()
        self.db_o1 = Database_weit_cl()
        self.view_o = View_cl()
        self.di_o1 = DataId_weit_cl()
        self.weit_mit = Database_weit_mit_cl()

    def GET(self, id=None):

        retVal_s = ''
        p = []
        proba = self.db_o.read_px()
        mitarbeiter = []
        # ret=self.db_o1.read_px(retVal_s[0])
        maxid = int(self.di_o1.readMaxId_p())
        for i in range(0, len(proba)):
            if proba[i]["mit_id"] == id:
                mitarbeiter = proba[i]
                break

        retVal_s = mitarbeiter["weiterbildung"]

        for i in range(0, maxid+1):
            if str(i) in retVal_s:
                proba_weit = self.db_o1.read_px()

                for k in range(0, len(proba_weit)):

                    if str(proba_weit[k]["id"]) == str(i):
                        p.append(proba_weit[k])
                        break

        return self.view_o.createList_px(p)

    def POST(self, data):

        self.db_o.create_px(data)

        return

    def getList_p(self):

        data_a = self.db_o.read_px()
        # default-Werte entfernen
        #ndata_a = data_a[1:]
        return self.view_o.createList_px(data_a)

    def getDetail_p(self, id_spl):

        data_o = self.db_o.read_px(id_spl)
        return self.view_o.createDetail_px(data_o)

    def getDetail_p1(self, id_spl):

        data_o = self.db_o1.read_px(id_spl)
        return self.view_o.createDetail_px(data_o)


class Qual_cl(object):

    exposed = True  # gilt für alle Methoden

    def __init__(self):

        # spezielle Initialisierung können hier eingetragen werden
        self.db_o = Database_Qual_cl()
        self.db_o1 = Database_weit_cl()
        self.view_o = View_cl()
        self.di_o1 = Dataid_Qual_cl()
        self.qual_in_weit = Qual_in_weit_cl()

    def GET(self, id=None):

        proba = self.db_o1.read_px()

        # ret=self.db_o1.read_px(retVal_s[0])

        for i in range(0, len(proba)+1):
            if str(proba[i]["id"]) == str(id):

                proba = self.getDetail_p1(i)
                break

        return proba

    def POST(self, data):

        self.db_o.create_px(data)
        self.qual_in_weit.POST(data)

        return

    def getList_p(self):

        data_a = self.db_o.read_px()
        # default-Werte entfernen
        #ndata_a = data_a[1:]
        return self.view_o.createList_px(data_a)

    def getDetail_p(self, id_spl):

        data_o = self.db_o.read_px(id_spl)
        return self.view_o.createDetail_px(data_o)

    def getDetail_p1(self, id_spl):

        data_o = self.db_o1.read_px(id_spl)
        return self.view_o.createDetail_px(data_o)


class Qual_in_weit_cl(object):

    exposed = True  # gilt für alle Methoden

    def __init__(self):

        # spezielle Initialisierung können hier eingetragen werden
        self.db_o = Database_Qual_in_weit_cl()
        self.db_o1 = Database_weit_cl()
        self.view_o = View_cl()
        self.di_o1 = Dataid_Qual_cl()
        self.qual = Database_Qual_cl()

    def GET(self, id=None):

        data = []
        if id != None:
            data = self.getDetail_p(id)
        else:
            data = self.getList_p()

        return data

    def POST(self, data):

        status = False
        p = self.db_o.read_px()
        data = json.loads(data)
        i = 0
        for i in range(0, len(p)):

            if p[i]["weiterbildung"] == data[0]:
                status = True
                break
        counter = i
        if status == True:
            self.db_o.append_px(p[counter])
        else:
            self.db_o.create_px(data)

        return

    def getList_p(self):

        data_a = self.db_o.read_px()
        # default-Werte entfernen
        #ndata_a = data_a[1:]
        return self.view_o.createList_px(data_a)

    def getDetail_p(self, id_spl):

        p = self.db_o.read_px()

        i = 0
        for i in range(0, len(p)):

            if str(p[i]["weiterbildung"]) == str(id_spl):
                p = p[i]
                break

        data_o = []
        data = []

        for i in range(0, len(self.qual.read_px())+1):
            if str(i) in p["qual"]:
                temp = self.qual.read_px()
                for k in range(0, len(temp)+1):
                    if str(temp[k]["id"]) == str(i):
                        data.append(temp[k])
                        break

        data_o = data

        return self.view_o.createDetail_px(data_o)

    def getDetail_p1(self, id_spl):

        data_o = self.db_o1.read_px(id_spl)
        return self.view_o.createDetail_px(data_o)


class Anmelden_cl(object):

    exposed = True  # gilt für alle Methoden

    def __init__(self):

        # spezielle Initialisierung können hier eingetragen werden
        self.db_o = Database_weit_cl()
        self.db_o1 = Database_mit_weit_cl()
        self.view_o = View_cl()
        self.weit_mit = Database_weit_mit_cl()

    def GET(self, id=None):

        fp_o = codecs.open('data/temp.json', 'r', 'utf-8')
        temp_Id = json.load(fp_o)

        if temp_Id == "-1":
            with codecs.open('data/temp.json', 'w', 'utf-8') as fp_o:
                json.dump(str(id), fp_o)
        retVal_s = self.getList_p()
        return retVal_s

    def POST(self, data):

        fp_o = codecs.open('data/temp.json', 'r', 'utf-8')
        temp_Id = json.load(fp_o)
        p = self.db_o1.read_px()
        pp = self.weit_mit.read_px()

        #result=filter(lambda x: x.mit_id==temp_Id, p)
        #fred= find(lambda person: person.name == temp_Id, p)
        status = False

        for i in range(0, len(p)):
            if p[i]["mit_id"] == temp_Id:
                status = True
                break

        if status == True:
            # self.weit_mit.append_px(temp_Id,data)
            self.db_o1.append_px(temp_Id, data)

        else:
            # self.weit_mit.create_px(data)
            self.db_o1.create_px(temp_Id, data)
        temp = json.loads(data)

        for i in range(0, len(p)):
            if pp[i]["weiterbildung"] == temp["id"]:
                status = True
                break

        if status == True:
            self.weit_mit.append_px(temp_Id, data)
            # self.db_o1.append_px(temp_Id,data)

        else:
            self.weit_mit.create_px(data)
            # self.db_o1.create_px(temp_Id,data)

        return

    def getList_p(self):

        data_a = self.db_o.read_px()
        # default-Werte entfernen
        #ndata_a = data_a[1:]
        return self.view_o.createList_px(data_a)

    def getDetail_p(self, id_spl):

        data_o = self.db_o.read_px(id_spl)
        return self.view_o.createDetail_px(data_o)

# EOF
