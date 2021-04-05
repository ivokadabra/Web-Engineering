# coding:utf-8

# Demonstrator es/te/tm

import sys
import os.path
import cherrypy

from app import application, template



def main():
    # ----------------------------------------------------------

    # aktuelles Verzeichnis ermitteln, damit es in der Konfigurationsdatei als
    # Bezugspunkt verwendet werden kann
    try:                                    # aktuelles Verzeichnis als absoluter Pfad
        currentDir_s = os.path.dirname(os.path.abspath(__file__))
    except:
        currentDir_s = os.path.dirname(os.path.abspath(sys.executable))
    cherrypy.Application.currentDir_s = currentDir_s

    configFileName_s = os.path.join(
        currentDir_s, 'server.conf')  # im aktuellen Verzeichnis
    if os.path.exists(configFileName_s) == False:
        # Datei gibt es nicht
        configFileName_s = None

    # autoreload-Monitor hier abschalten
    cherrypy.engine.autoreload.unsubscribe()

    # 1. Eintrag: Standardverhalten, Berücksichtigung der Konfigurationsangaben im configFile
    cherrypy.tree.mount(
        None, '/', configFileName_s
    )

    # 2. Eintrag: Method-Dispatcher für die "Applikation" "app" vereinbaren
    cherrypy.tree.mount(
        application.COUNT_Total(),
        '/ctotal',
        {'/': {'request.dispatch': cherrypy.dispatch.MethodDispatcher()}}
    )


    cherrypy.tree.mount(
        application.Mitarbeiter_cl(),
        '/mitarbeiter',
        {'/': {'request.dispatch': cherrypy.dispatch.MethodDispatcher()}}
    )

    cherrypy.tree.mount(
        application.Mitarbeiter_Weit_cl(),
        '/weit_mit',
        {'/': {'request.dispatch': cherrypy.dispatch.MethodDispatcher()}}
    )

    cherrypy.tree.mount(
        application.Anmelden_cl(),
        '/anmelden',
        {'/': {'request.dispatch': cherrypy.dispatch.MethodDispatcher()}}
    )

    cherrypy.tree.mount(
        application.Weiterbildung_cl(),
        '/weiterbildung',
        {'/': {'request.dispatch': cherrypy.dispatch.MethodDispatcher()}}
    )


    cherrypy.tree.mount(
        application.Status_cl(),
        '/status',
        {'/': {'request.dispatch': cherrypy.dispatch.MethodDispatcher()}}
    )

    
    cherrypy.tree.mount(
        application.Qual_cl(),
        '/qual',
        {'/': {'request.dispatch': cherrypy.dispatch.MethodDispatcher()}}
    )
    
    cherrypy.tree.mount(
        application.Qual_in_weit_cl(),
        '/qual_in_weit',
        {'/': {'request.dispatch': cherrypy.dispatch.MethodDispatcher()}}
    )
    cherrypy.tree.mount(
        application.Weiterbildung_auswertung_cl(),
        '/weiter_before',
        {'/': {'request.dispatch': cherrypy.dispatch.MethodDispatcher()}}
    )

    cherrypy.tree.mount(
        application.Weiterbildung_aktiv_cl(),
        '/weiter_aktiv',
        {'/': {'request.dispatch': cherrypy.dispatch.MethodDispatcher()}}
    )

    cherrypy.tree.mount(
        application.Weiterbildung_after_cl(),
        '/weiter_after',
        {'/': {'request.dispatch': cherrypy.dispatch.MethodDispatcher()}}
    )

    cherrypy.tree.mount(
        application.Erfolg(),
        '/erfolg',
        {'/': {'request.dispatch': cherrypy.dispatch.MethodDispatcher()}}
    )
    cherrypy.tree.mount(
        application.Mitarbeiter_sort(),
        '/mitarbeiter_sort',
        {'/': {'request.dispatch': cherrypy.dispatch.MethodDispatcher()}}
    )
    cherrypy.tree.mount(
        application.Hronologisch_weit(),
        '/hronologisch',
        {'/': {'request.dispatch': cherrypy.dispatch.MethodDispatcher()}}
    )
    cherrypy.tree.mount(
        application.Weiterbildung_sort(),
        '/weit_sort',
        {'/': {'request.dispatch': cherrypy.dispatch.MethodDispatcher()}}
    )
    cherrypy.tree.mount(
        application.Erfolg_teihnemher(),
        '/erfolg_teil',
        {'/': {'request.dispatch': cherrypy.dispatch.MethodDispatcher()}}
    )

    cherrypy.tree.mount(
        application.WEIT_IN_STATUS(),
        '/weit_status',
        {'/': {'request.dispatch': cherrypy.dispatch.MethodDispatcher()}}
    )

    cherrypy.tree.mount(
        application.Zertifikate_sort(),
        '/zertifikate_sort',
        {'/': {'request.dispatch': cherrypy.dispatch.MethodDispatcher()}}
    )

    # 2. Eintrag: Method-Dispatcher für die "Applikation" "templates" vereinbaren
    cherrypy.tree.mount(
        template.Template_cl(),
        '/templates',
        {'/': {'request.dispatch': cherrypy.dispatch.MethodDispatcher()}}
    )

    cherrypy.engine.start()
    cherrypy.engine.block()


# ----------------------------------------------------------
if __name__ == '__main__':
    # ----------------------------------------------------------
    main()
