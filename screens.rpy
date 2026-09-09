# PANTALLA INTERACTIVA DEL PUZLE 2 (DESTELLOS)
screen eleccion_cometa():
    imagebutton:
        idle "images/destello_azul.png"
        hover "images/destello_azul.png"
        xpos 0.2 ypos 0.3
        action Jump("resultado_cometa_incorrecto")

    imagebutton:
        idle "images/destello_rojo.png"
        hover "images/destello_rojo.png"
        xpos 0.5 ypos 0.2
        action Jump("resultado_cometa_correcto")

    imagebutton:
        idle "images/destello_dorado.png"
        hover "images/destello_dorado.png"
        xpos 0.8 ypos 0.4
        action Jump("resultado_cometa_incorrecto")
