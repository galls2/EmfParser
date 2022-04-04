log_level = "debug"


def _print(*args, newline):
    if newline:
        print(*args)
    if not newline:
        print(*args, end=" ")


def debug_print(*args, newline=True):
    if log_level == "debug":
        _print(*args, newline=newline)


def info_print(*args, newline=True):
    if log_level in ["info", "debug"]:
        _print(*args, newline=newline)


def parse_color_ref(raw_bytes):
    assert len(raw_bytes) == 4

    if raw_bytes[-1] != 0:
        info_print("Invalid ColorRef Object")
    r, g, b = raw_bytes[0:3]
    return (r,g,b)
