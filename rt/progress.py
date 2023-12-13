import ansi
import time
import util

BLACK_AND_WHITE = 0
RAINBOW = 1
ANIMATED_RAINBOW = 2

def _calc_rainbow_color(f: float, animate = False):
    angle = f * 360.0
    if animate:
        angle = (angle - ((time.time() % 6.0) * 60.0)) % 360.0
    if angle < 60.0:
        return ansi.bg_color(1.0, (angle * 4.25) / 255.0, 0.0)
    elif angle < 120.0:
        return ansi.bg_color(((120.0 - angle) * 4.25) / 255.0, 1.0, 0.0)
    elif angle < 180.0:
        return ansi.bg_color(0.0, 1.0, ((angle - 120.0) * 4.25) / 255.0)
    elif angle < 240.0:
        return ansi.bg_color(0.0, ((240.0 - angle) * 4.25) / 255.0, 1.0)
    elif angle < 300.0:
        return ansi.bg_color(((angle - 240.0) * 4.25) / 255.0, 0.0, 1.0)
    else:
        return ansi.bg_color(1.0, 0.0, ((360.0 - angle) * 4.25) / 255.0)

def update_percent(progress: float, bar_width = 10, prefix = '', suffix = '', bar_type = BLACK_AND_WHITE):
    '''
    Renders a progress bar based on percentage.

    Args:
        progress: a value between 0.0 and 1.0 representing how much has been done
        bar_width: width of the bar in characters
        prefix: an optional message to show before the progress bar
        suffix: an optional message to show after the progress bar
        bar_type: type of bar to render
    '''
    progress = util.clamp(progress)
    block = int(round(bar_width * progress))
    
    bar = ''
    if bar_type == BLACK_AND_WHITE:
        # render the bar in black and white
        bar = f'{ansi.BG_WHITE}{" " * block}'
    elif bar_type == RAINBOW or bar_type == ANIMATED_RAINBOW:
        # render the bar in a rainbow
        animate = bar_type == ANIMATED_RAINBOW
        for i in range(0, block):
            bar += f'{_calc_rainbow_color(float(i) / float(bar_width), animate = animate)} '
    # add in the blank part of the bar
    bar += ansi.BG_DEFAULT
    bar += " " * (bar_width - block)

    print(f'\r{ansi.CLEAR_LINE}{prefix}[{bar}] {progress * 100.0:5.1f}%{suffix}', end='')

def update_items(cur_item: int, num_items: int, bar_width = 10, prefix = '', suffix = '', bar_type = BLACK_AND_WHITE):
    '''
    Renders a progress bar based on number of items completed.

    Args:
        cur_item: current item
        num_items: total number of items
        bar_width: width of the bar in characters
        prefix: an optional message to show before the progress bar
        suffix: an optional message to show after the progress bar
        bar_type: type of bar to render
    '''
    width = len(str(num_items))
    suffix = f' [ {ansi.BOLD_ON}{cur_item:{width}}{ansi.BOLD_OFF} / {ansi.BOLD_ON}{num_items}{ansi.BOLD_OFF} ]{suffix}'
    update_percent(float(cur_item) / float(num_items), bar_width, prefix, suffix, bar_type)
