import pywinauto
import logging

logger = logging.getLogger(__name__)


class PyWin:
    def open_calculator():
        try:
            # if Calculator is in open, use it
            app = pywinauto.Application(backend='uia').connect(title="Calculator")
        except pywinauto.findwindows.ElementNotFoundError as e:
            # otherwise, start Calculator window, start it
            app = pywinauto.Application(backend='uia').start("calc.exe")
        win = app.Calculator
        win.set_focus()     # raise the window on top
        return win

    def find_button(win, name):
        button = win.child_window(title=name, control_type="Button")
        if button.exists():
            return button
        logger.warning('did not find button "%s"', name)
        return None

    def get_result(win):
        text = win.child_window(title="Result", control_type="Text")
        return text.iface_value.CurrentValue

    # click left mouse button at the center of button
    def click(button):
        rect = button.rectangle()
        x = int((rect.left + rect.right) / 2)
        y = int((rect.top + rect.bottom) / 2)
        pywinauto.mouse.click(button="left", coords=(x, y))
