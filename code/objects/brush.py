from objects.emf_object import EmfObj


class Brush(EmfObj):
    def __init__(self, brush_style, brush_color, brush_hatch):
        super().__init__()
        self._brush_style = brush_style
        self._brush_color = brush_color
        self._brush_hatch = brush_hatch

        ## TODO validate legal values
