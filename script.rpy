# ----------------------------------------------------
# CONFIGURACIÓN DE PERSONAJES Y LOGROS
# ----------------------------------------------------
define novio = Character("[nombre_player]", color="#d32f2f")
define yo = Character("Tú", color="#e91e63")

init python:
    def logro(titulo, desc):
        renpy.notify("LOGRO DESBLOQUEADO\n" + titulo + " - " + desc)

# ----------------------------------------------------
# INICIO DEL JUEGO
# ----------------------------------------------------
label start:
    play music "audio/piano_suave.mp3" fadein 1.0
    scene bg atardecer with dissolve

    # Entrada de nombre de usuario
    $ nombre_player = renpy.input("Ingresa tu usuario para iniciar la partida:", default="Moxx").strip()

    if nombre_player == "":
        $ nombre_player = "Moxx"

    $ logro("Jugador Registrado", "Bienvenido a la partida, " + nombre_player)

    show novio sorprendido at center with dissolve

    novio "¿Qué onda con este lugar?... El cielo se ve idéntico al de Your Name."

    novio "Espera, hay un mensaje flotando en la pantalla..."

    yo "¡Ey, [nombre_player]! Si quieres reclamar tu regalo de cumpleaños, vas a tener que ganártelo."

    yo "No va a estar tan fácil. Tienes puzles por delante, así que a ver qué tan listo andas hoy."

    show novio desafiante at center

    novio "Acepto el reto."

    jump puzle_uno

# ----------------------------------------------------
# PUZLE 1: LEAGUE OF LEGENDS
# ----------------------------------------------------
label puzle_uno:
    scene bg atardecer with dissolve
    show novio at center with dissolve

    yo "Para desbloquear la primera pista de tu regalo de cumpleaños, [nombre_player], tienes que demostrar que no eres un manco en LOL."

    novio "A ver, ponme a prueba."

    yo "Responde con la verdad absoluta: Si la partida se complica y todo va mal... ¿de quién es la culpa?"

    menu:
        "Del Jungla, obviamente":
            $ logro("Pro Player", "Demostraste tu sabiduría en LOL.")
            show novio feliz at center
            novio "Facilito. Esa regla se la sabe cualquiera."
            yo "Correcto. Veo que sí le sabes. Se desbloqueó la primera pista."
            jump puzle_dos

        "Mía, me equivoqué":
            show novio confundido at center
            yo "Incorrecto. Un verdadero jugador de LOL NUNCA acepta la culpa jajaja. Intenta otra vez."
            jump puzle_uno

        "Del Wifi":
            show novio riendo at center
            yo "Buen intento, pero la respuesta legendaria siempre es la del Jungla. ¡Prueba de nuevo!"
            jump puzle_uno

# ----------------------------------------------------
# PUZLE 2: ELECCIÓN VISUAL
# ----------------------------------------------------
label puzle_dos:
    scene bg atardecer_cometa with dissolve
    show novio concentrado at center with dissolve

    yo "Bien, pasaste la prueba gamer. Pero ahora se pone interesante, [nombre_player]."

    yo "Mira hacia el cielo... El cometa está pasando en pleno atardecer."
    yo "Hay tres destellos de luz flotando en el horizonte. Uno de ellos contiene la pista clave para abrir tu cofre de cumpleaños."

    novio "¿Cuál de los tres será? Déjame mirar bien..."

    hide novio with dissolve

    call screen eleccion_cometa

label resultado_cometa_correcto:
    show novio feliz at center with dissolve
    $ logro("Ojo de Halcón", "Encontraste el destello correcto a la primera.")
    yo "¡Exacto! Ese era el hilo rojo. Te estás acercando al regalo final..."
    jump puzle_tres

label resultado_cometa_incorrecto:
    show novio confundido at center with dissolve
    yo "Mmmm... no, ese destello era solo una estrella fugaz común. ¡Busca mejor, [nombre_player]!"
    jump puzle_dos

# ----------------------------------------------------
# PUZLE 3 Y CLÍMAX FINAL
# ----------------------------------------------------
label puzle_tres:
    play music "audio/piano_emotivo.mp3" fadein 2.0
    scene bg atardecer_top with dissolve

    show novio sorprendido at center with dissolve

    novio "¡Mira! El último destello hizo aparecer una caja en la cima..."

    yo "Llegaste al final del juego, [nombre_player]. Abre el cofre y reclama tu regalo de cumpleaños."

    scene bg nota_pantalla with dissolve

    $ logro("El Regalo de Cumpleaños", "Llegaste al final de la historia.")

    "{b}{size=+20}{color=#ff4081}¿Volvemos? :3{/color}{/size}{/b}"

    pause 2.0

    scene bg atardecer_top with dissolve
    show novio sonrojado at center with dissolve

    novio "..."

    yo "¡Feliz cumpleaños, [nombre_player]! El hilo rojo nunca se rompe del todo."

    yo "Ahora dime... ¿qué tienes para responder a eso?"

    $ respuesta_moxx = renpy.input("Escribe tu respuesta aquí:").strip()

    if respuesta_moxx == "":
        $ respuesta_moxx = "Me dejaste sin palabras..."

    python:
        with open(config.gamedir + "/respuesta_de_cumple.txt", "w") as f:
            f.write("Moxx respondió: " + respuesta_moxx)

    yo "Guardado. Ya leeré lo que pusiste."

    yo "¡Gracias por jugar!"

    return
