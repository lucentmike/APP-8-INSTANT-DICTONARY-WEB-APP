import justpy as jp
from webapp.about import About
from webapp.home import Home 
from webapp.dictonary import Dictonary
from webapp import page
import inspect


imports = list(globals().values())

for obj in imports:
    if inspect.isclass(obj):
        if issubclass(obj, page.Page) and obj is not page.Page:
            jp.Route(obj.path, obj.serve)

    jp.Route(About.path, About.serve)
    jp.Route(Home.path, Home.serve)
    jp.Route(Dictonary.path, Dictonary.serve)

jp.justpy(port=8001)