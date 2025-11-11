import board

from kmk.kmk_keyboard import KMKKeyboard
from kmk.scanners.keypad import KeysScanner
from kmk.keys import KC
from kmk.modules.macros import Press, Release, Tap, Macros

# Main keyboard object
keyboard = KMKKeyboard()

# Macro extension
macros = Macros()
keyboard.modules.append(macros)

# Definitions
PINS = [board.D3, board.D4, board.D2, board.D1]

# Matrix of Keys
keyboard.matrix = KeysScanner(
    pins=PINS,
    value_when_pressed=False,
)

# Keycodes: https://github.com/KMKfw/kmk_firmware/blob/main/docs/en/keycodes.md
# Macros: https://github.com/KMKfw/kmk_firmware/blob/main/docs/en/macros.md
keyboard.keymap = [
    [KC.A, KC.DELETE, KC.MACRO("Hello world!"), KC.Macro(Press(KC.LCMD), Tap(KC.S), Release(KC.LCMD)),]
]

if __name__ == '__main__':
    keyboard.go()
