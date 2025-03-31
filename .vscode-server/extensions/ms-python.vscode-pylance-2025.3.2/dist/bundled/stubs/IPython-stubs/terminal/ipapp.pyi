"""
This type stub file was generated by pyright.
"""

from traitlets.config.application import catch_config_error
from IPython.core.crashhandler import CrashHandler
from IPython.core.application import BaseIPythonApplication
from IPython.core.shellapp import InteractiveShellApp

"""
The :class:`~traitlets.config.application.Application` object for the command
line :command:`ipython` program.
"""
_examples = ...
class IPAppCrashHandler(CrashHandler):
    """sys.excepthook for IPython itself, leaves a detailed report on disk."""
    def __init__(self, app) -> None:
        ...
    
    def make_report(self, traceback):
        """Return a string containing a crash report."""
        ...
    


flags = ...
frontend_flags = ...
addflag = ...
classic_config = ...
aliases = ...
class LocateIPythonApp(BaseIPythonApplication):
    description = ...
    subcommands = ...
    def start(self): # -> None:
        ...
    


class TerminalIPythonApp(BaseIPythonApplication, InteractiveShellApp):
    name = ...
    description = ...
    crash_handler_class = IPAppCrashHandler
    examples = ...
    flags = ...
    aliases = ...
    classes = ...
    interactive_shell_class = ...
    subcommands = ...
    auto_create = ...
    quick = ...
    display_banner = ...
    force_interact = ...
    something_to_run = ...
    @catch_config_error
    def initialize(self, argv=...): # -> None:
        """Do actions after construct, but before starting the app."""
        ...
    
    def init_shell(self): # -> None:
        """initialize the InteractiveShell instance"""
        ...
    
    def init_banner(self): # -> None:
        """optionally display the banner"""
        ...
    
    def start(self): # -> None:
        ...
    


def load_default_config(ipython_dir=...): # -> Instance:
    """Load the default config file from the default ipython_dir.

    This is useful for embedded shells.
    """
    ...

launch_new_instance = ...
if __name__ == '__main__':
    ...
