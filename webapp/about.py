import justpy as jp
from webapp import layout

class About:
    path = "/about"

    def serve(self):
        wp = jp.QuasarPage(tailwind=True)

        lay = layout.DefaultLayout(a=wp)

        container = jp.QPageContainer(a=lay)

        div = jp.Div(a=container, classes="bg-gray-200 h-screen")
        jp.Div(a=div, text = "This is the about page!", classes="text-4xl m-2")
        jp.Div(a=div, text="""
        When I was a young boy
        When I was a young boy
        My father took me into the city
        To see a marching band
        He said, "Son, when you grow up
        Would you be the savior of the broken
        The beaten and the damned?"
        He said, "Will you defeat them?
        Your demons, and all the non-believers
        The plans that they have made?"
        "Because one day, I'll leave you a phantom
        To lead you in the summer
        To join the black parade"
        When I was a young boy
        My father took me into the city
        To see a marching band
        He said, "Son, when you grow up
        Would you be the savior of the broken
        The beaten and the damned?"
        Sometimes I get the feelin'
        She's watchin' over me
        And other times I feel like I should go
        And through it all, the rise and fall
        The bodies in the streets
        And when you're gone, we want you all to know
        We'll carry on, we'll carry on
        And though you're dead and gone, believe me
        Your memory will carry on
        We'll carry on
        And in my heart, I can't contain it
        The anthem won't explain it
        A world that sends you reelin'
        From decimated dreams
        Your misery and hate will kill us all
        So paint it black and take it back
        Let's shout it loud and clear
        Defiant to the end, we hear the call
        
        """, classes="text-lg")
        return wp
