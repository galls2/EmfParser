log_level = "info"


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
