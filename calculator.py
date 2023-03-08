from pywin import PyWin
import logging

logger = logging.getLogger(__name__)

class Calculator():
    def __init__(self):
        self.win = PyWin.open_calculator()

        # get key and its name by using Windows Inspect
        self.key_name = {
            "0": "0",
            "1": "1",
            "2": "2",
            "3": "3",
            "4": "4",
            "5": "5",
            "6": "6",
            "7": "7",
            "8": "8",
            "9": "9",
            "+": "Add",
            "-": "Subtract",
            "*": "Multiply",
            "/": "Divide",
            "=": "Equals"
        }

    def click_button(self, key):
        logger.info('click_button[' + key + ']')
        if not key in self.key_name:
            logger.warning('unknown key: "%s"', key)
            return
        button = PyWin.find_button(self.win, self.key_name[key])
        if button != None:
            PyWin.click(button)

    def get_result(self):
        return PyWin.get_result(self.win)
