from yucli import _header
from kivy.uix.widget import Widget
from time import strftime, gmtime
from kivy.clock import Clock
import os


class Structure(Widget):
    """Widget Layout Class

    Class that houses all of the widgets for the console window
    """
    # Class variables
    text_font = os.path.dirname(os.path.realpath(__file__)) + "/asset/CascadiaCode.ttf"

    def __init__(self, width, height, font_path=None, **kwargs):
        """Constructor for Structure class

        Constructs an instance of the structure class
        :param width: [INTEGER] Width specification of the console window
        :param height: [INTEGER] Height specification of the console window
        :param font_path: [STRING] Path to custom font if specified
        """
        # Intakes values from parameters to instance variables and initializes variables
        self.width = width
        self.height = height
        self.font_path = font_path
        self.commands = {}

        # Calculates widget dimension specifications
        Structure.text_input_top_height = (self.height - 32) / self.height

        # Changes text_font if font_path is specified
        if self.font_path is not None:
            Structure.text_font = self.font_path
        else:
            pass

        # Calls widget constructor
        super().__init__(**kwargs)

    def on_enter(self):
        """User Input Mirror Method

        Posts user input to console
        """
        # Posts user input to console and refocuses to user input section
        self.ids.prompt.text += _header.header("USER", strftime("%H:%M", gmtime())) + self.ids.user_input.text + "\n"
        self.schedule_refocus()

        # Calls whatever method is stored in
        if self.ids.user_input.text.split()[0] in self.commands:
            try:
                self.commands[self.ids.user_input.text.split()[0]](arguments=self.ids.user_input.text.split()[1:])
            except IndexError:
                pass

        # Clears user input
        self.ids.user_input.text = ""

    def on_touch_up(self, touch):
        """Widget Event Handler

        Handles on-keypress-up events

        :param touch: [UNKNOWN] Touch event
        """
        # Refocuses to user_input section
        self.schedule_refocus()

    def schedule_refocus(self):
        """User Input Refocus Method [PRIVATE]

        Refocuses user to user input after entering an input
        """
        # Schedules an instant refocus
        Clock.schedule_once(self.refocus, 0)

    def refocus(self, arg1):
        """User Input Initial Refocus Method [PRIVATE]

        Initializes refocus to user input after entering an input
        Needs _schedule_refocus() to refocus

        :param arg1: [UNKNOWN] I have no fucking idea what this is suppose to be, but StackOverflow said you need it
        """
        # Changes user_input attributes for refocus
        self.ids.user_input.focus = True

        # Give some usage to arg1
        return arg1