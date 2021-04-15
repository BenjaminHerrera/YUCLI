from yucli import _header
from yucli import _structure
from kivy.core.window import Window
from time import strftime, gmtime
from kivy.config import Config
from kivy.lang import Builder
from kivy.app import App
from kivy.clock import Clock
import os

# Loads design profile
root = Builder.load_file(os.path.dirname(os.path.realpath(__file__)) + '/structure.kv')


class Console(App):
    """Console Class

    Main class that houses all functions and features for the customizable console
    """

    def __init__(self, width, height, title="Console", resizable=False,
                 greeting_text="YUCLI [v1.3.0.0]", icon_path=None,
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
        self._width = width
        self._height = height
        self._title = title
        self._resizable = resizable
        self._greeting_text = greeting_text
        self._icon_path = icon_path
        self._font_path = font_path

        # Calls app constructor
        super().__init__(**kwargs)

        # Creates a widgets class to initiate widgets
        self._structure = _structure.Structure(self._width, self._height, self._font_path)

        # Set window title
        self.title = title

        # Displays greeting text upon window creation if applicable
        if self._greeting_text is not None:
            if self._greeting_text is "":
                pass
            else:
                self._structure.ids.prompt.text += self._greeting_text + "\n\n"

    def build(self):
        """Window Constructor Method

        Constructors window with specified properties

        :return Structure: [Structure] Class that houses widgets for console window
        """
        # Constructs console window
        Window.size = (self._width, self._height)
        Config.set('graphics', 'resizable', self._resizable)
        Config.write()

        # Disables ESC exit and multitouch behavior
        Config.set('kivy', 'exit_on_escape', '0')
        Config.set('input', 'mouse', 'mouse,multitouch_on_demand')

        # Applies custom icon if applicable
        if self._icon_path is None:
            self.icon = os.path.dirname(os.path.realpath(__file__)) + '/asset/icon.png'
        else:
            self.icon = self._icon_path

        # Returns structure class
        return self._structure

    def stop(self):
        """Window Grace Closer Method

        Gracefully closes window upon being called

        :return: True
        """
        # Closes current instance
        App.stop(self)

    def print_new_line(self, text, header="INFO"):
        """Insert Text Method

        Inserts text into console

        :param text: [STRING] Text to insert into console
        :param header: [STRING] Type of header to append to new line
        """
        # Prints a new line with specified text
        self._structure.ids.prompt.text += _header.header(header, strftime("%H:%M", gmtime())) + text + "\n"

    def print_replace_line(self, text, header="INFO"):
        """Line Replacer Method

        Replaces the line before with the specified text

        :param text: [STRING] Text to replace previous line in the console
        :param header: [STRING] Type of header to append to new line
        """
        # Get history of lines on the console into list format
        console_log = self._structure.ids.prompt.text.splitlines()

        # Removes previous line and adds in new line
        if "USER" in console_log[-1]:
            if console_log[0] == self._greeting_text.splitlines()[0]:
                if len(console_log) == len(self._greeting_text.splitlines()) + 2:
                    trimmed_console_log = "\n".join(console_log[:len(console_log)-1])
                    self._structure.ids.prompt.text = trimmed_console_log + "\n" + \
                                                      _header.header(header, strftime("%H:%M", gmtime())) + text + "\n"
                else:
                    trimmed_console_log = "\n".join(console_log[:len(console_log)-2])
                    self._structure.ids.prompt.text = trimmed_console_log + "\n" + \
                                                      _header.header(header, strftime("%H:%M", gmtime())) + text + "\n"
            else:
                if len(console_log) <= 2:
                    self._structure.ids.prompt.text = _header.header(header, strftime("%H:%M", gmtime())) + text + "\n"
                else:
                    trimmed_console_log = "\n".join(console_log[:len(console_log)-2])
                    self._structure.ids.prompt.text = trimmed_console_log + "\n" + \
                                                      _header.header(header, strftime("%H:%M", gmtime())) + text + "\n"
        else:
            if console_log[0] == self._greeting_text.splitlines()[0]:
                if len(console_log) == len(self._greeting_text.splitlines()) + 2:
                    trimmed_console_log = "\n".join(console_log[:len(console_log)-1])
                    self._structure.ids.prompt.text = trimmed_console_log + "\n" + \
                                                      _header.header(header, strftime("%H:%M", gmtime())) + text + "\n"
                else:
                    if len(console_log) > len(self._greeting_text.splitlines()):
                        trimmed_console_log = "\n".join(console_log[:len(console_log)-1])
                        self._structure.ids.prompt.text = trimmed_console_log + "\n" + \
                                                         _header.header(header, strftime("%H:%M", gmtime())) + text + "\n"
                    else:
                        trimmed_console_log = "\n".join(console_log[:len(console_log)])
                        self._structure.ids.prompt.text = trimmed_console_log + "\n" + \
                                                         _header.header(header, strftime("%H:%M", gmtime())) + text + "\n"
            else:
                if len(console_log) == 1:
                    self._structure.ids.prompt.text = _header.header(header, strftime("%H:%M", gmtime())) + text + "\n"
                else:
                    trimmed_console_log = "\n".join(console_log[:len(console_log)-1])
                    self._structure.ids.prompt.text = trimmed_console_log + "\n" + \
                                                      _header.header(header, strftime("%H:%M", gmtime())) + text + "\n"

    @staticmethod
    def schedule_task(function, time):
        """Scheduler Wrapper Method

        Applies a schedule task on a function that will be executed after a specific time

        :param function: [FUNCTION] Function to execute upon scheduled task
        :param time: [FLOAT] Time after to execute
        """
        # Schedules the execution of the given function once
        Clock.schedule_once(function, time)

    @staticmethod
    def schedule_recurring_task(function, interval):
        """Recurring Scheduler Wrapper Method

        Applies a recurring schedule task on a function that will be executed on a given interval

        :param function: [FUNCTION] Function to execute upon scheduled task
        :param interval: [FLOAT] How often to execute given function
        """
        # Schedules the recurring execution of the given function
        Clock.schedule_interval(function, interval)

    @staticmethod
    def unschedule_task(function):
        """Unscheduler Wrapper Method

        Unschedule a given task

        :param function: [FUNCTION] Function to unschedule
        """
        # Unschedule function
        Clock.unschedule(function)

    def disable_input(self):
        """Input Disabler Method

        Disables user input
        """
        # Disables user input
        self._structure.disable = True

    def enable_input(self):
        """Input Disabler Method

        Disables user input
        """
        # Enable user input
        self._structure.disable = False

    def clear_console(self):
        """Console Clear Method [PRIVATE]

        Clears all content on the console

        :return args: [LIST] Returns args
        """
        # Clears console
        self._structure.ids.prompt.text = ""

    def register_command(self, command, function):
        """Command Register Method

        Registers command for the console

        :param command: [STRING] command to register
        :param function: [OBJECT] function to call upon entering of command
        """
        # Registers command and function to Structure instance
        self._structure.commands[command] = function