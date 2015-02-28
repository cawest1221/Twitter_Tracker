import cherrypy
from random import random
import os


class Server(object):

    @cherrypy.expose
    def index(self):
        return """
<html>
<head>
    <meta name="viewport" content="initial-scale=1.0, user-scalable=no" />
    <meta http-equiv="content-type" content="text/html; charset=UTF-8"/>
    <title>Twitter Tracker</title>
    <link href="/static/css/style.css" rel="stylesheet" />
    <script type="text/javascript" src="/static/js/jsrefresh.js#js,notify"></script>
    <script type="text/javascript" src="/static/js/map.js?%(RAND)s"></script>
    <script type="text/javascript">
        function loadScript() {
          var script = document.createElement('script');
          script.type = 'text/javascript';
          script.src = 'https://maps.googleapis.com/maps/api/js?v=3.exp&sensor=false&' +
              'callback=initialize';
          document.body.appendChild(script);
        }
        window.onload = loadScript;
    </script>
</head>
    <body>
    	<div id="map_canvas"></div>
    </body>
</html>
    """ % {'RAND' : random()}

if __name__ == '__main__':
    conf = {
        '/': {
            'tools.sessions.on': True,
            'tools.staticdir.root': os.path.abspath(os.getcwd())
        },
        '/static': {
            'tools.staticdir.on': True,
            'tools.staticdir.dir': './public'
        }
    }
    cherrypy.quickstart(Server(), '/', conf)
