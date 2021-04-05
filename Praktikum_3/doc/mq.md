**Keine Gruppe**
**Ivaylo Iliev**
**Gültigkeitsdatum: 14.01.2021**




#Aufgabe der Anwendung
###Die WEB-Anwendung dient zur Konfiguration,Speciherung und Übreschreiben der Daten von Mitarbeiter,Weiterbildung,Qualifikationen und Zertifikate.Im Bezug darauf haben die verschiedenen Komponente bestimmte Relation zueinander.Zum Beipiel einer Mitarbeiter kann sich für mehrere Weiterbildungen einschreiben, eine Weiterbildung kann zu mehr als einen Mitarbeiter zugehören, eine Weiterbildung kann nur eine Zertifikate haben,aber eine Weiterbildungg kann eine oder meherere Qualifikkationen besetzen.Diesbezüglisch darauf wird eine komplexe Vernentzung der Veschieden Komponenten aufgebaut, indem man beide Server-und Clientseitige Programierung anwendet.
#Übersicht der fachlichen Funktionen:
##Backend:
###Die Backend-Teil ist auf Python geschrieben und ist auf 5 Module veteilt.Im application.py wird die Logik des Programms aufgebaut.Für jeder Komponent oder bestimmte Relation wird ein separater Klass aufgebaut.Einige der Wichtigste Funktionen für jeder Klass sind:
###GET():dient zur Verwendung einer GET-Request man kann,indem man entweder mit einen ID bestimmte numerrierte Objekt(mit der Funktion getDetail) oder alle Objekte der zugehörige Komponent entnehmen kann(mit der Funktion getList).
###POST(): diese Methode dient zur Zufügung neuer Informationen in bestimmter Objekt oder Element,indem in der Trumpf der Mthode die create_px Funtkion aus Modul database.py aufgerufen wird.In der POST methode kann man auch die append_px Funtkion auf Modul database.py ausführen.Diese dient ,um bei einem schön existierende List neuen Element einzufpgen.
###PUT():diese Methode dient zur Aktualisierung  bestimmter Informationen in einem Objekt oder Element,indem in der Trumpf der Mthode die update_px Funtkion aus Modul database.py aufgerufen wird.
###DELETE():diese Methode dient zur Löschen bestimmter Informationen in einem Objekt oder Element,indem in der Trumpf der Methode die delete_px Funtkion aus Modul database.py aufgerufen wird.
##Frondend:
###Die Frondend-Teil ist im Javascript geschrieben, indem die Logik dieser Teil in der Modul mein.js geschrieben wird.Da gibt es 24 Klassen die für den verschieden Objekten oder Relationen zugeeignet sind.Es gibt ,aber Funktionen,die zu jeder Klass zugeignet sind:
###render_px(): dient um die Information der geeignete Seite zu entnehmen ,indem man einen GET-Reguest mit der Hilfe der in Modul req.js definierte Funktion GET_px() erschaffen kann.Die Information wird durch die Hilfe einer Labmda-Funktion geliefert und nachher wird diese mit JSON.parse and der Methode do_Render übergeben.
###do_Render(): Diese Funktion dient, um die geliferte Daten aus der GET-Request auf der HTML Dokument anzupassen.Diesbezüglich verwendet man die Methode execute_px , an dem Man die Template,der inde rKonstruktor definiert ist , und der Data übergibt.
###handleEvent_p():Diese Funtion dient zur Selektion, Drükung von Buttonen auf der bestimmte Seite.Mit der Objekt event_opl.target.id kann man die ID der verschiedenen Buttonen entnehmen und dann die geignete Funtion ausführen.

#Beschreibung der Komponenten des Servers
##1)application.py
###In dieser Modul wird die Lokig des Programms gestellt, wo es 20 Klassen gibt:
###- class COUNT_total:Da werden die Anzahl der Mitarbeiter und Weiterbuldungen gezeigt,indem Man die Länge der JSON-Dateien ,wo die Komponente gespeichert sind,entnimmt.
###-class Mitarbeiter: In dieser Klasse werden alle Aktivitäten wie Einfügen,Löschen,Aktualieseren,oder Entnehmen die im Bezug auf Mitarbeiter stehen.Die Methode ,die verwendet werden,sind GET,POST,PUT,DELETE. Die GET Funktion besteht aus ein paar if-else Bedingungen ,deren Ziel ist hearuszufinden ,ob in in ID and der Funktion übergeben wird.Wenn das der Fall ist dan wird eine Schliefe durchgeführt, um die Position der Mitarbeiter mit diese Id herauszufinden.Nachher wird die Funktion getDetail aufgerufen, wo man die gefundene Mitarbeiter als JSON and Frondend übergibt.Wenn aber keine ID vorhanden ist(d.h id==None),dann werden alle Mitarbeiter selektiert.Die nächste Methode ist POST,deren Ziel einen neuen Mitarbeiter hinzufügen ist,indem man die Funktion create_px aus Modul database.py aufruft.Auf eineähnliche Weise ist die PUT Funktion implemntiert,wo man anstatt create_px,update_px aufruft.Bei der DELETE Funktion aufruft löscht man nicht nur der Mitarbeiter ,sondern auch seine Relation zu den Weiterbildungen und seinem Status.
###-class Mitarebietr_Weit_cl: In dieser Klasse wird die Beziehung zwischen die Mitarbeiter und die Weiterbildung, an dennen sie siech eingeschrieben haben,erstellt.
###-class Anmelden: In dieser Klasse wird die Anmeldung der Mitarbeiter zur der verschieden Weiterbildungen erschafft.In der GET-Methode verwendet man einen JSON-Datei temp.json der die ID der Mitaebeiter speichert.Dann werden mit getList alle Weiterbildungen zugegeben.Die POST Methode dienst zur Anmeldung der Mitarbeiter zu einer Weiterbildung.Da werden vorwiegend zwei Funtkionen gebraucht:create_px und append_px aus dem database.py Modul.Zuerst wird mit Hilfe einer for-Schleife die Position der Mitarbeiter gesucht.Wenn die Mitarbeiter gefunden ist dann wird die append_px gewählt ,wo zu den schön existierende Mitarbeiter-Weiterbidlugn Bezihung einen neuen Element eingefügt wird.Wenn aber keinen Mitarbeiter gefunden wird,dann wird die Methode create_px verwdnet ,wo man in der mit_weit.json Datei einen neuen Objekt mit "mit_id" und einen List "weiterbildung" erstellt.Die ID aus dem temp.json Datei wird in mit_id gespeichert und die ID der Weiterbidlung wird in der List "weiterbildung" gespeichert.
###-class Weiterbildung: In dieser Klasse werden alle Aktivitäten wie Einfügen,Löschen,Aktualieseren,oder Entnehmen die im Bezug auf Weiterbildung stehen.
###-class Status:Die Klasse dient zum Entnehmen oder Einfügen von Status der Mitarbeiter zu bestimmte Weiterbildung.Um die Status zu entnehmen wird die Funktion getDetail in der GET-Methode verwendet.In diesr Methode wird zuerst eine for-Schleife gemacht,um die Position der Mitarbeiter in der JSON-Datei zu finden.In der Zweite for-Schleife wird die index der Weiterbildung in der mit_weit Objekt gesucht.Wenn das der Fall ist wird in einer Liste die Status hinzugefügt.Nachher gibt es aber eine dritte for_schleife die nach der Anzahl der efolgreich geschlossene Weiterbildungen sucht.Wenn das der Fall ist wird in die Name der Zertifikate genommen.Sonst wird "keine" hinzugefügt.
###-class Qual: In dieser Klasse werden alle Aktivitäten wie Einfügen,Löschen,Aktualieseren,oder Entnehmen die im Bezug auf Qualifikationen stehen.
###-class Qual_in_weit_cl: In diser Klasse werden die Qualifikationen die zu einer Weiterbildung hinzugefügt werden.Dafür benuzt man die POST-Methode,wo man eine FOR-Scheife hat, um herauszufinden, a welchen Position sich die Weiterbildung mit bestimmte Qualifikationen befindet. Wenn solche Objekt existiert wird die create_px Funktion uas Modul database.py verwendet.Sonst wird die Funtkion append_px genuzt.
###-class Weiterbildung_auswertung_cl:In dieser Klasse wirden die Alle Weiterbildungen genommen die schön abgeschlossen sind.Dafür wird in der Funktion getList_p mit Hilfe einer Schleife spezifisch diese Weiterbildungen gewählt.
###-class Weiterbildung_aktiv_cl::In dieser Klasse wirden die Alle Weiterbildungen genommen die im Moment noch laufend sind.Dafür wird in der Funktion getList_p mit Hilfe einer Schleife spezifisch diese Weiterbildungen gewählt.
###-class Weiterbildung_after_cl::In dieser Klasse wirden die Alle Weiterbildungen genommen ,die für die Zukunft geplannt sind.Dafür wird in der Funktion getList_p mit Hilfe einer Schleife spezifisch diese Weiterbildungen gewählt.
###-class Erfolg: In dieser Klasse wird den Status zur bestimmte Mitarbeiter auf erfolg , kein efolf ,stoniert oder angebrochen angesetzt.Dazu verwendet man eine FOR-Schleife um die Mitabeiterposition in der JSON-Datei zu finden.Nachher benutzt man die JSON-Datei erfolgid.json ,wo man die ID der Weiterbildung speichert. Dann wird die Position der Weiterbildung in der mit_weit Objekt gesucht.Im bezug auf welche Status eingefügt werden muss wird eine Folge von if-else Kombinationen geschrieben.Nachher wird die alte status mit pop genommen und die neue mit insert eingefügt.
###-class Mitarbeiter_sort(): Dient zur Sortierung der Mitarbeiter Alphabetisch
###-class Mitarbeiter_sort(): Dient zur Sortierung der Weiterbildungen Hronologisch
###-class Weiterbildung_sort(): Dient zur Sortierung der Weiterbildungen Alphabetisch
###-class Erfolg_teilnehmer():Dient zur Sortierung der Erfolgreiche Teilnehmer.Dazu wird in der GET-Methode eine Mischung von for-Schleifen und if-Bedingungen genuzt.Die erste for-Schleife nimmt Position der Weiterbidlung,die einen List mit der Mitarbeiter entnimmt.Dann werden mit eine andere Schleife welche mitarbeiter zu diesen Weiterbildung eingeschrieben sind.Dann wird in der nächste Schleife die Position dieser Mitarbeiter in der JSON-Datei gesucht.Dann wird die Postion der Status gesucht.Wenn der status erfolg ist wird die Mitarbeiter in einer result List eingefügt der als JSON and der GET-Request übergeben wird.
###-class WEIT_IN_STATUS(): Dient zur stonieren einer Weiterbildung zur bestimmter Mitarbeiter
###-class Zertifikate_sort(): Dient zur Sortierung der Zertifikaten Alphabetisch
###-class Template_cl():Dient zum Laden der Templates
##2)database.py
###In diesen Modul wird die Data vewandelt, indem es 8 Klassen gibt.Für jede Klasse gibt es gemeinsame Funktionen wie z.B:
###read_px(): mit dieser Funktion kann man die bestimmte JSON-Datei lesen
###create_px(): dient zurerstellung neuer Element oder Objekt.
###append_px(): dient zur Einfügungn einer neuen Element in einer schön existirende Liste oder Objekt.
###update_px():dient zur Aktualiesirung einer neuen Element von betimmte List oder Objekt.
###delete_px():dient zur Löschen  einer Objekt oder Element.
###saveData_p():dient zur Speicherung neuer Elemente oder Objekten.
###-Trotz die gemeinsame Funktion,jeder Klass bezitzt eigen Aufgaben:
###-class Database_weit_cl(): Dient zur Konfiguration von Daten der Weiterbildungen
###-class Database_weit_mit_cl(): Dient zur Konfiguration der Daten von Weiterbildungen und zu dennen eingeschriebenen Mitarbeiter
###-class Database_mit_weit_cl():Dient zur Konfiguration der Daten von Mitarbeiter und die Weiterbildungen ,an dennen man teilnihmmt.
###-class  Database_Qual_in_weit_cl():Dient zur Konfiguration der Daten von Weiterbildungen und zu dennen eingeschriebenen Qualifikationen.
###-class Database_Qual_cl(): Dient zur Konfiguration von Daten der Qualifikationen.
###-class Database_Status_cl(): Dient zur Konfiguration von Daten der Status von Mitarbeiter zur eingeschribenen Weitebildungen.
###-class Database_weit_cl(): Dient zur Konfiguration von Daten der Weiterbildungen
##3)dataid.py:
###In dieser Modul wird die MaxID der vreschiedene Komponenten konfiguriert.Es gibt 4 Klassen hier:
###-class DataId_cl():dient zur Verwaltung der MaxID der Mitarbeiter
###-class StatusId_cl():dient zur Verwaltung der MaxID der Status der Mitarbeiter für bestimmte Weiterbildungen.
###-class DataId_mit_weit_cl():dient zur Verwaltung der MaxID der Mitarbeiter und die Weiterbildungen ,an dennen der sich eingeschrieben hat
###-class DataId_cl():dient zur Verwaltung der MaxID der Weiterbildungen.
###-class Dataid_Qual_cl():dient zur Verwaltung der MaxID der Qualifikationen
###Für alle Klassen sind aber gemeinsame Funtkionen defieniert:
###-create_px():dient zur Erstellung der MaxID.
###read_px():dient zum Lesen der MaxId.
###saveMaxId_p():dient zur Speicherung der MaxId.
##4)template.py
###Dieser Modul dient zur Laden der Templates.Es gibt nur einer Klassemit der Name "Template_cl" und eine Funtkion "GET",wo mit Hilfe der cherrypy Funktionen die Templates geöffnet und gelesen werden.
##5)view.py:
###Diese Modus dient zum Schicken der Information im Form von JSON die Aus dem GET-Requests der Frontend.Es gibt eine Klasse mit der name "View_cl" und zwei Funktionen:
###createList_px():dient zum Senden von Ganze Informationen oder Objekte(also ohne ID spezifizierte Objekt)
###createDetail_px():dient zum Senden von Informatonen mit bestimmte ID,d.h bestimmte Objekt oder Element.
##6)JSONS
###-efolgid.json:dient zur Speicherung der Zahlt von Mitarbeiter bei Selektierung der erfolgreich abgeschlossen Mitarbeiter.
###-maxid.json: dient zur Speicherung der MaxId der Mitarbeiter
###-mit_weit.json: dient zur Speicherung der Mitaberiter und der Weiterbildungen, an dennen der sich eingeschrieben hat
###-mit_weit_id.json:dient zur Speicherung der MaxId der mit_weit Komponente
###qual_in_weit.json: dient zur Speicherung der Quelifikationen in bestimmte Weiterbldung
###qual.id.json: dient zur Speicherung der MaxID der Qualifikationen
###qual.json: dient zur Speicherung der Qualifikationen 
###status.json:dient zur Speihcerung der Status der Mitarbeiter fürbestimmte Weiterbildung
###statusid.json: dient zur Speicherung der MaxID der Satus Komponente
###temp.json: dient zur Speicherung von einer temporere ID von Mitarbeiter bei der einfügen in mit_weit
###webteam.json: dient zur Speicherung der Mitarbeiter
###weit_mit.json: dient zur Speicherung der Weiterbildungen in zu dennen zugeeignete Mitarbeiter
###weit.id.json: dient zur Speicherung der der MaxID der Weiterbildungen
###weiterbildung.json: dient zur Speicherung der Weiterbildungen

<img src="p3_bild_1.png" alt="Flowers in Chania" width="1000" height="500">
<img src="p3_bild_2.png" alt="Flowers in Chania" width="1000" height="500">
<img src="p3_bild_3.png" alt="Flowers in Chania" width="1000" height="500">
<img src="p3_bild_4.png" alt="Flowers in Chania" width="1000" height="500">
<img src="p3_bild_5.png" alt="Flowers in Chania" width="1000" height="500">


