log_level = "info"


def info_print(*arg, newline=True):
    if log_level == "info" or log_level == "debug":
        if newline:
            print(*arg)
        if not newline:
            print(*arg, end=" ")
