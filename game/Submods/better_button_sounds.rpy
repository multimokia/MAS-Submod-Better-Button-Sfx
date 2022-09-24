init -990 python in mas_submod_utils:
    Submod(
        author="multimokia",
        name="Better Button Sounds",
        description="A submod which modifies the stock DDLC sfx and replaces it with something more {i}listenable{/i}.",
        version="1.0.0",
        version_updates={}
    )

init 1 python:
    gui.hover_sound = "mod_assets/sounds/piano_buttons/button_hover.ogg"
    gui.activate_sound = "mod_assets/sounds/piano_buttons/button_press.ogg"
