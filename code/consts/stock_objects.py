from consts.brush_style import BrushStyle
from objects.brush import Brush
from objects.color_ref import ColorRef

white_brush = Brush(BrushStyle.BS_SOLID, ColorRef(0xFF, 0xFF, 0xFF), None)
light_gray_brush = Brush(BrushStyle.BS_SOLID, ColorRef(0xC0, 0xC0, 0xC0), None)
gray_brush = Brush(BrushStyle.BS_SOLID, ColorRef(0x80, 0x80, 0x80), None)
dark_gray_brush = Brush(BrushStyle.BS_SOLID, ColorRef(0x40, 0x40, 0x40), None)
black_brush = Brush(BrushStyle.BS_SOLID, ColorRef(0x00, 0x00, 0x00), None)
null_brush = Brush(BrushStyle.BS_NULL, None, None)

StockObjects = {
    0x80000000: (white_brush, "white_brush"),
    0x80000001: (light_gray_brush, "light_gray_brush"),
    0x80000002: (gray_brush, "gray_brush"),
    0x80000003: (dark_gray_brush, "dark_gray_brush"),
    0x80000004: (black_brush, "black_brush"),
    0x80000005: (null_brush, "null_brus")
}
