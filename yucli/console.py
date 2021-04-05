from yucli import _header
from yucli import _structure
from kivy.core.window import Window
from time import strftime, gmtime
from kivy.config import Config
from kivy.lang import Builder
from kivy.app import App
import os

# Loads design profile
root = Builder.load_file(os.path.dirname(os.path.realpath(__file__)) + '/structure.kv')


class Console(App):
    """Console Class

    Main class that houses all functions and features for the customizable console
    """

    def __init__(self, width, height, title="Console", resizable=False,
                 greeting_text="YUCLI [v1.1.0.0]", icon_path=None,
                 font_path=None, **kwargs):
        """Constructor for console class

        Constructs an instance of the Console class

        :param width: [INTEGER] Resizes console to specified width
        :param height: [INTEGER] Resizes console to specified height
        :param title: [STRING] Title of the console window
        :param resizable: [BOOLEAN] Whether or not the console should be resizable
        :param greeting_text: [STRING] Beginning text to display upon console window creation
        :param icon_path: [STRING] Path to icon for console window
        :param font_path: [STRING] Path to .ttf file for console
        """
        # Intakes values from parameters to instance variables
        self.width = width
        self.height = height
        self.title = title
        self.resizable = resizable
        self.greeting_text = greeting_text
        self.icon_path = icon_path
        self.font_path = font_path

        # Calls app constructor
        super().__init__(**kwargs)

        # Creates a widgets class to initiate widgets
        self.structure = _structure.Structure(self.width, self.height, self.font_path)

        # Displays greeting text upon window creation if applicable
        if self.greeting_text is not None:
            self.structure.ids.prompt.text += self.greeting_text + "\n\n"

    def build(self):
        """Window Constructor Method

        Constructors window with specified properties
        :return Structure: [Structure] Class that houses widgets for console window
        """
        # Constructs console window
        Window.size = (self.width, self.height)
        Config.set('graphics', 'resizable', self.resizable)
        Config.write()

        # Disables ESC exit and multitouch behavior
        Config.set('kivy', 'exit_on_escape', '0')
        Config.set('input', 'mouse', 'mouse,multitouch_on_demand')

        # Applies custom icon if applicable
        if self.icon_path is None:
            self.icon = os.path.dirname(os.path.realpath(__file__)) + '/asset/icon.png'
        else:
            self.icon = self.icon_path

        # Returns structure class
        return self.structure

    def print_new_line(self, text, header="INFO"):
        """Insert Text Method

        Inserts text into console

        :param text: [STRING] Text to insert into console
        :param header: [STRING] Type of header to append to new line
        """
        # Prints a new line with specified text
        self.structure.ids.prompt.text += _header.header(header, strftime("%H:%M", gmtime())) + text + "\n"

    def clear_console(self):
        """Console Clear Method [PRIVATE]

        Clears all content on the console
        :return args: [LIST] Returns args
        """
        # Clears console
        self.structure.ids.prompt.text = ""

    def register_command(self, command, function):
        """Command Register Method

        Registers command for the console

        :param command: [STRING] command to register
        :param function: [OBJECT] function to call upon entering of command
        """
        # Registers command and function to Structure instance
        self.structure.commands[command] = function