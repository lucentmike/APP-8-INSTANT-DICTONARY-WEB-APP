import justpy as jp
import definition_file
from webapp import layout, page

class Dictonary(page.Page):
    path = "/dictonary"

    @classmethod
    def serve(cls, req):
        wp = jp.QuasarPage(tailwind=True)

        lay = layout.DefaultLayout(a=wp)

        container = jp.QPageContainer(a=lay)

        div = jp.Div(a=container, classes="bg-gray-200 h-screen")
        jp.Div(a=div, text = "Instant English Dictonary", classes="text-4xl m-2")
        jp.Div(a=div, text="Get the definition of any English word instantly as you type.", classes="text-lg")

        input_div = jp.Div(a=div, classes= "grid grid-cals-2")

        output_div = jp.Div(a=div, classes="m-2 p-2 text-lg border-2 h-40")

        input_box = jp.Input(a=input_div, placeholder="Type in a word here...", outputdiv = output_div, classes="m-2 bg-gray-200 border-2 border-gray-200 rounded w-64 focus:bg-white focus:outline-none focus:border-purple-500 py-2 px-4 ")

        input_box.on('input', cls.get_definition)

        return wp
 
   
    @staticmethod
    def get_definition(widget, msg):
        defined = definition_file.Definition(widget.value).get()
        widget.outputdiv.text = " ".join(defined)
