import util

RESET              = "\033[0m"
BOLD_ON            = "\033[1m"
ITALICS_ON         = "\033[3m"
UNDERLINE_ON       = "\033[4m"
INVERSE_ON         = "\033[7m"
STRIKETHROUGH_ON   = "\033[9m"
BOLD_OFF           = "\033[22m"
ITALICS_OFF        = "\033[23m"
UNDERLINE_OFF      = "\033[24m"
INVERSE_OFF        = "\033[27m"
STRIKETHROUGH_OFF  = "\033[29m"
FG_BLACK           = "\033[30m"
FG_RED             = "\033[31m"
FG_GREEN           = "\033[32m"
FG_YELLOW          = "\033[33m"
FG_BLUE            = "\033[34m"
FG_MAGENTA         = "\033[35m"
FG_CYAN            = "\033[36m"
FG_WHITE           = "\033[37m"
FG_DEFAULT         = "\033[39m"
BG_BLACK           = "\033[40m"
BG_RED             = "\033[41m"
BG_GREEN           = "\033[42m"
BG_YELLOW          = "\033[43m"
BG_BLUE            = "\033[44m"
BG_MAGENTA         = "\033[45m"
BG_CYAN            = "\033[46m"
BG_WHITE           = "\033[47m"
BG_DEFAULT         = "\033[49m"
CURSOR_ON          = "\033[?25h"
CURSOR_OFF         = "\033[?25l"
CLEAR_LINE         = "\033[2K"
CLEAR_SCREEN       = "\033[2J"

def fg_color(r: float, g: float, b: float):
    return f'\033[38;2;{int(util.clamp(r) * 255.0)};{int(util.clamp(g) * 255.0)};{int(util.clamp(b) * 255.0)}m'

def bg_color(r: float, g: float, b: float):
    return f'\033[48;2;{int(util.clamp(r) * 255.0)};{int(util.clamp(g) * 255.0)};{int(util.clamp(b) * 255.0)}m'
