# coding=utf-8


class DjangoApplication(object):
    HOST = "0.0.0.0"
    PORT = 8001

    # noinspection PyMethodMayBeStatic
    def mount_static(self, url, root):
        config = {
            'tools.staticdir.on': True,
            'tools.staticdir.dir': root,
            'tools.expires.on': True,
            'tools.expires.secs': 86400
        }

        import cherrypy
        cherrypy.tree.mount(None, url, {'/': config})

    def run(self):
        from cherrypy.process.plugins import Daemonizer
        from cherrypy.process.plugins import PIDFile
        
        import cherrypy
        import os
        
        os.environ["DJANGO_SETTINGS_MODULE"] = "ImageResize.settings"
        
        from django.core.handlers.wsgi import WSGIHandler
        from django.core.management import call_command
        import django

        django.setup(set_prefix=False)
        call_command("migrate", interactive=False)
        call_command("collectstatic", interactive=False)

        engine = cherrypy.engine
        autoreload = engine.autoreload
        
        autoreload.stop()
        autoreload.unsubscribe()
        cherrypy.config.update({
            'server.socket_host': self.HOST,
            'server.socket_port': self.PORT,
            'engine.autoreload_on': False,
            'log.screen': True
        })

        from django.conf import settings
        self.mount_static(settings.STATIC_URL, settings.STATIC_ROOT)

        cherrypy.log("Loading and serving Django application")
        cherrypy.tree.graft(WSGIHandler())
        
        Daemonizer(engine).subscribe()
        PIDFile(cherrypy.engine, 'app.pid').subscribe()
        engine.start()


if __name__ == "__main__":
    print "Your app is running at http://localhost:8001"
    
    DjangoApplication().run()
