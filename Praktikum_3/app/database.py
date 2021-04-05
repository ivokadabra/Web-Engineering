# coding: utf-8

# Demonstrator!

from . import dataid
from .dataid import StatusId_cl
import os
import os.path
import codecs
import json


class Database_Mitarbeiter_cl(object):

    def __init__(self):
        self.data_o = None
        self.maxId_o = dataid.DataId_cl()

    def read_px(self, id_spl=None):

        data_o = None
        self.readData_p()
        if id_spl == None:
            data_o = self.data_o
        else:
            id_i = int(id_spl)
            if id_i > 0 and id_i < len(self.data_o):
                data_o = self.data_o[id_i]
            else:
                data_o = self.data_o[0]
        return data_o

    def delete_px(self, id_spl):
        proba = self.read_px()

        # ret=self.db_o1.read_px(retVal_s[0])

        for i in range(0, len(proba)):
            if len(proba) != 0:

                if proba[i]["id"] == id_spl:

                    if self.data_o.pop(i) != None:
                        self.saveData_p()
                        break

        return

    def create_px(self, data_opl):
        id_s = self.maxId_o.create_px()
        temp = json.loads(data_opl)

        objekt = {
            'id': id_s,
            'col1': temp[0],
            'col2': temp[1],
            'col3': temp[2],
            'col4': temp[3],

        }

        data_o = self.read_px()
        data_o.append(objekt)

        self.saveData_p()
        return str(id_s)

    def update_px(self, data_opl):
        id_s = self.maxId_o.create_px()
        temp = json.loads(data_opl)

        objekt = {
            'id': temp[0],
            'col1': temp[1],
            'col2': temp[2],
            'col3': temp[3],
            'col4': temp[4],

        }

        data_o = self.read_px()
        i = 0

        for i in range(0, int(id_s)):

            if data_o[i]["id"] == temp[0]:

                break
        k = i

        proba = data_o
        data_o = []
        for i in range(0, len(proba)):
            if i == k:
                data_o.append(objekt)
            else:
                data_o.append(proba[i])

        self.data_o = data_o

        self.saveData_p()
        return str(id_s)

    def readData_p(self):

        try:
            fp_o = codecs.open('data/webteams.json', 'r', 'utf-8')
        except:
            self.data_o = {}
            self.saveData_p()
        else:
            with fp_o:
                self.data_o = json.load(fp_o)
        return

    def saveData_p(self):

        with codecs.open('data/webteams.json', 'w', 'utf-8') as fp_o:
            json.dump(self.data_o, fp_o, indent=3)


class Database_Status_cl(object):

    def __init__(self):
        self.data_o = None
        self.maxId_o = dataid.StatusId_cl()
        self.mit_weit = dataid.DataId_mit_weit_cl()

    def read_px(self, id_spl=None):

        data_o = None
        self.readData_p()
        if id_spl == None:
            data_o = self.data_o
        else:
            id_i = int(id_spl)
            if id_i > 0 and id_i < len(self.data_o):
                data_o = self.data_o[id_i]
            else:
                data_o = self.data_o[0]
        return data_o

    def create_px(self, data_opl, temp):
        objekt = {
            'mit_id': temp,
            'status': [data_opl]

        }

        data_o = self.read_px()
        data_o.append(objekt)

        self.saveData_p()
        return

    def delete_px(self, id_spl):

        proba = self.read_px()

        for i in range(0, len(proba)):
            if len(proba) != 0:
                if proba[i]["mit_id"] == id_spl:
                    if self.data_o.pop(i) != None:
                        self.saveData_p()
                        break

        return

    def readData_p(self):

        try:
            fp_o = codecs.open('data/status.json', 'r', 'utf-8')
        except:
            self.data_o = {}
            self.saveData_p()
        else:
            with fp_o:
                self.data_o = json.load(fp_o)
        return

    def append_px(self, id_spl, data_opl):

        data_o = self.read_px()
        counter = self.mit_weit.read_px()
        for i in range(0, int(counter)):
            if data_o[i]["mit_id"] == id_spl:
                data_o = data_o[i]
                break

        data_o["status"].append(data_opl)

        fp_o = codecs.open('data/temp.json', 'w', 'utf-8')
        json.dump("-1", fp_o)
        self.saveData_p()
        return

    def saveData_p(self):

        with codecs.open('data/status.json', 'w', 'utf-8') as fp_o:
            json.dump(self.data_o, fp_o, indent=3)


class Database_Qual_cl(object):

    def __init__(self):
        self.data_o = None
        self.maxId_o = dataid.Dataid_Qual_cl()
        self.status = dataid.StatusId_cl()

    def read_px(self, id_spl=None):
        self.readData_p()
        data_o = None
        if id_spl == None:
            data_o = self.data_o
        else:
            id_i = int(id_spl)
            if id_i > 0 and id_i < len(self.data_o):
                data_o = self.data_o[id_i]
            else:
                data_o = self.data_o[0]
        return data_o

    def append_px(self, id_spl, data_opl):

        data_o = self.read_px()

        for i in range(0, len(data_opl)):
            if data_o[i]["mit_id"] == id_spl:
                data_o = data_o[i]
                break
        temp = json.loads(data_opl)

        data_o["weiterbildung"].append(temp["id"])
        self.status.append_px(id_spl, "angemeldet")

        fp_o = codecs.open('data/temp.json', 'w', 'utf-8')
        json.dump("-1", fp_o)
        self.saveData_p()
        return

    def delete_px(self, id_spl):

        proba = self.read_px()

        for i in range(0, len(proba)):
            if len(proba) != 0:
                if proba[i]["mit_id"] == id_spl:
                    if self.data_o.pop(i) != None:
                        self.saveData_p()
                        break

        return

    def create_px(self, data_opl):
        self.maxId_o.create_px()
        data_opl[1:]
        temp = json.loads(data_opl)

        mit_Id = self.maxId_o.read_px()

        objekt = {
            'id': mit_Id,
            'col1': temp[1],
            'col2': temp[2],
            #'col3': temp[3],
        }
        data_o = self.read_px()
        data_o.append(objekt)

        self.saveData_p()
        return

    def readData_p(self):

        try:
            fp_o = codecs.open('data/qual.json', 'r', 'utf-8')
        except:
            self.data_o = {}
            self.saveData_p()
        else:
            with fp_o:
                self.data_o = json.load(fp_o)
        return

    def saveData_p(self):

        with codecs.open('data/qual.json', 'w', 'utf-8') as fp_o:
            json.dump(self.data_o, fp_o, indent=3)


class Database_Qual_in_weit_cl(object):

    def __init__(self):
        self.data_o = None
        self.maxId_o = dataid.Dataid_Qual_cl()
        self.status = dataid.StatusId_cl()

    def read_px(self, id_spl=None):

        self.readData_p()
        data_o = None
        if id_spl == None:
            data_o = self.data_o
        else:
            id_i = int(id_spl)
            if id_i > 0 and id_i < len(self.data_o):
                data_o = self.data_o[id_i]
            else:
                data_o = self.data_o[0]
        return data_o

    def append_px(self, data_opl):

        index = self.maxId_o.read_px()

        data_opl["qual"].append(str(int(index)+1))

        self.saveData_p()
        return

    def delete_px(self, id_spl):

        proba = self.read_px()

        for i in range(0, len(self.read_px())):
            if len(proba) != 0:
                if proba[i]["weiterbildung"] == id_spl:
                    if self.data_o.pop(i) != None:
                        self.saveData_p()
                        break

        return

    def create_px(self, data_opl):

        self.maxId_o.create_px()

        mit_Id = self.maxId_o.read_px()

        objekt = {
            'weiterbildung': data_opl[0],
            'qual': [mit_Id],
        }
        data_o = self.read_px()
        data_o.append(objekt)

        self.saveData_p()
        return

    def readData_p(self):

        try:
            fp_o = codecs.open('data/qual_in_weit.json', 'r', 'utf-8')
        except:
            self.data_o = {}
            self.saveData_p()
        else:
            with fp_o:
                self.data_o = json.load(fp_o)
        return

    def saveData_p(self):

        with codecs.open('data/qual_in_weit.json', 'w', 'utf-8') as fp_o:
            json.dump(self.data_o, fp_o, indent=3)


class Database_mit_weit_cl(object):

    def __init__(self):
        self.data_o = None
        self.maxId_o = dataid.DataId_mit_weit_cl()
        self.status = Database_Status_cl()

    def read_px(self, id_spl=None):

        self.readData_p()
        data_o = None
        if id_spl == None:
            data_o = self.data_o
        else:
            id_i = int(id_spl)
            if id_i > 0 and id_i < len(self.data_o):
                data_o = self.data_o[id_i]
            else:
                data_o = self.data_o[0]
        return data_o

    def append_px(self, id_spl, data_opl):

        data_o = self.read_px()

        for i in range(0, len(data_opl)):
            if data_o[i]["mit_id"] == id_spl:
                data_o = data_o[i]
                break
        temp = json.loads(data_opl)

        data_o["weiterbildung"].append(temp["id"])
        self.status.append_px(id_spl, "angemeldet")

        fp_o = codecs.open('data/temp.json', 'w', 'utf-8')
        json.dump("-1", fp_o)
        self.saveData_p()
        return

    def delete_px(self, id_spl):

        proba = self.read_px()

        for i in range(0, len(self.read_px())):
            if len(proba) != 0:
                if proba[i]["mit_id"] == id_spl:
                    if self.data_o.pop(i) != None:
                        self.saveData_p()
                        break
        return

    def create_px(self, temp_id, data_opl):

        data_opl[1:]
        temp = json.loads(data_opl)

        fp_o = codecs.open('data/temp.json', 'r', 'utf-8')

        objekt = {
            'mit_id': temp_id,
            'weiterbildung': [temp["id"]],
        }

        self.status.create_px("angemeldet", temp_id)

        fp_o = codecs.open('data/temp.json', 'w', 'utf-8')
        json.dump("-1", fp_o)

        data_o = self.read_px()
        data_o.append(objekt)

        self.saveData_p()
        return

    def readData_p(self):

        try:
            fp_o = codecs.open('data/mit_weit.json', 'r', 'utf-8')
        except:
            self.data_o = {}
            self.saveData_p()
        else:
            with fp_o:
                self.data_o = json.load(fp_o)
        return

    def saveData_p(self):

        with codecs.open('data/mit_weit.json', 'w', 'utf-8') as fp_o:
            json.dump(self.data_o, fp_o, indent=3)


class Database_weit_mit_cl(object):

    def __init__(self):
        self.data_o = None
        self.maxId_o = dataid.DataId_mit_weit_cl()
        self.status = dataid.StatusId_cl()

    def read_px(self, id_spl=None):

        self.readData_p()
        data_o = None
        if id_spl == None:
            data_o = self.data_o
        else:
            id_i = int(id_spl)
            if id_i > 0 and id_i < len(self.data_o):
                data_o = self.data_o[id_i]
            else:
                data_o = self.data_o[0]
        return data_o

    def append_px(self, id_spl, data_opl):

        data_o = self.read_px()

        temp = json.loads(data_opl)

        for i in range(0, len(data_opl)+1):
            if data_o[i] != None:
                if int(data_o[i]["weiterbildung"]) == int(temp["id"]):
                    data_o = data_o[i]
                    break

        temp = json.loads(data_opl)

        data_o["mit"].append(id_spl)

        self.saveData_p()
        return

    def delete_px(self, id_spl):

        proba = self.read_px()
        maxid = int(self.maxId_o.read_px())
        i = 0

        for i in range(0, maxid):
            if len(proba) != 0:
                if proba[i]["mit_id"] == id_spl:

                    break

        if self.data_o.pop(i) != None:
            self.saveData_p()

        return

    def create_px(self, data_opl):

        data_opl[1:]
        temp = json.loads(data_opl)

        fp_o = codecs.open('data/temp.json', 'r', 'utf-8')
        mit_Id = json.load(fp_o)

        objekt = {
            'weiterbildung': temp["id"],
            'mit': [mit_Id],
        }

        data_o = self.read_px()
        data_o.append(objekt)

        self.saveData_p()
        return

    def readData_p(self):

        try:
            fp_o = codecs.open('data/weit_mit.json', 'r', 'utf-8')
        except:
            self.data_o = {}
            self.saveData_p()
        else:
            with fp_o:
                self.data_o = json.load(fp_o)
        return

    def saveData_p(self):

        with codecs.open('data/weit_mit.json', 'w', 'utf-8') as fp_o:
            json.dump(self.data_o, fp_o, indent=3)


class Database_weit_cl(object):

    def __init__(self):
        self.data_o = None
        self.maxId_o = dataid.DataId_weit_cl()

    def read_px(self, id_spl=None):

        self.readData_p()
        data_o = None
        if id_spl == None:
            data_o = self.data_o
        else:
            id_i = int(id_spl)
            if id_i > 0 and id_i < len(self.data_o):
                data_o = self.data_o[id_i]
            else:
                data_o = self.data_o[0]
        return data_o

    def create_px(self, data_opl):

        id_s = self.maxId_o.create_px()
        temp = json.loads(data_opl)

        objekt = {
            'id': id_s,
            'col1': temp[0],
            'col2': temp[1],
            'col3': temp[2],
            'col4': temp[3],
            'col5': temp[4],
            'col6': temp[5],
            'col7': temp[6],
            'col8': temp[7],

        }

        data_o = self.read_px()
        data_o.append(objekt)

        self.saveData_p()
        return str(id_s)

    def update_px(self, data_opl):

        id_s = self.maxId_o.create_px()
        temp = json.loads(data_opl)

        objekt = {
            'id': temp[0],
            'col1': temp[1],
            'col2': temp[2],
            'col3': temp[3],
            'col4': temp[4],
            'col5': temp[5],
            'col6': temp[6],
            'col7': temp[7],
            'col8': temp[8],

        }

        data_o = self.read_px()

        i = 0
        for i in range(0, int(id_s)):

            if data_o[i]["id"] == temp[0]:

                break
        k = i

        proba = data_o
        data_o = []
        for i in range(0, len(proba)):
            if i == k:
                data_o.append(objekt)
            else:
                data_o.append(proba[i])

        self.data_o = data_o

        self.saveData_p()
        return str(id_s)

    def delete_px(self, id_spl):

        proba = self.read_px()
        i = 0

        for i in range(0, len(proba)):
            if len(proba) != 0:

                if proba[i]["id"] == id_spl:

                    break

        if self.data_o.pop(i) != None:
            self.saveData_p()

        return

    def readData_p(self):

        try:
            fp_o = codecs.open('data/weiterbildung.json', 'r', 'utf-8')
        except:
            self.data_o = {}
            self.saveData_p()
        else:
            with fp_o:
                self.data_o = json.load(fp_o)
        return

    def saveData_p(self):

        with codecs.open('data/weiterbildung.json', 'w', 'utf-8') as fp_o:
            json.dump(self.data_o, fp_o, indent=3)


# EOF
