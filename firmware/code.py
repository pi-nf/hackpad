import board

from kmk.keys import KC
from kmk.kmk_keyboard import KMKKeyboard
from kmk.scanners import DiodeOrientation


keyboard = KMKKeyboard()

keyboard.col_pins = (board.D0, board.D1)
keyboard.row_pins = (board.D2, board.D3, board.D4)

keyboard.diode_orientation = DiodeOrientation.COL2ROW

keyboard.keymap = [
    [KC.LEFT, KC.DOWN, KC.RIGHT],
    [KC.SPACE, KC.C, KC.D, KC.S, KC.A],
    [KC.F, KC.K, KC.E, KC.Q, KC.B]
]


if __name__ == '__main__':
    keyboard.go()
