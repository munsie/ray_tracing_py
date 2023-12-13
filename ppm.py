import ansi
import progress

from vec3 import Color

class ppm:
    _PROGRESS_BAR_WIDTH = 80

    def __init__(self, filename: str, width: int, height: int, progress: bool = False) -> None:
        self._width = width
        self._height = height
        
        self._current_width = 0
        self._current_height = 0

        self._progress = progress

        self._file = open(filename, 'w')
        self._file.write(f'P3\n{width} {height}\n255\n')

    def write(self, c: Color) -> None:
        if self._current_height == self._height:
            raise IndexError(f'PPM file overran image bounds - {self._width} x {self._height}')

        self._current_width += 1
        if self._current_width == self._width:
            self._current_width = 0
            self._current_height += 1
            
            if self._progress:
                if self._current_height == self._height:
                    progress.update_items(cur_item=self._current_height, num_items=self._height, suffix=f' {ansi.FG_GREEN}Done!{ansi.FG_DEFAULT}', bar_width=ppm._PROGRESS_BAR_WIDTH, bar_type=progress.BLACK_AND_WHITE)
                    print('')
                else:
                    progress.update_items(cur_item=self._current_height, num_items=self._height, bar_width=ppm._PROGRESS_BAR_WIDTH, bar_type=progress.RAINBOW)

        self._file.write(f'{int(c.x)} {int(c.y)} {int(c.z)}\n')
        
    def __del__(self) -> None:
        self._file.close()
        self._file = None
