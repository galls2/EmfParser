log_level = "debug"


# debug < info < warning < error

def _print(*args, newline):
    if newline:
        print(*args)
    if not newline:
        print(*args, end=" ")


def debug_print(*args, newline=True):
    if log_level in ["debug"]:
        _print(*args, newline=newline)


def error_print(*args, newline=True):
    if log_level in ["debug", "info", "warning", "error"]:
        _print(*args, newline=newline)


def warning_print(*args, newline=True):
    if log_level in ["debug", "info", "warning"]:
        _print(*args, newline=newline)


def info_print(*args, newline=True):
    if log_level in ["info", "debug"]:
        _print(*args, newline=newline)


def enum_index_to_enum_val(enum_index, enum_class):
    try:
        enum_obj = enum_class(enum_index)
        return enum_obj
    except ValueError:
        info_print(f">>>>> Error in conversion {hex(enum_index)}({enum_index}) to enum object of type {enum_class.__name__}")
        return None
