Class
Ask: Who or what is performing the action?
Problem
Ask: What happens to the data when the Actor touches it?
Constraint
Ask: Where does the logic break or change?
Inverse
Ask: If I do this, how do I undo it?

Command: uv
Problem: it's an extremely fast python package and project manager
Constraint: Not included in python by default
    Argument: help
    Problem: diplays help menu
        Argument: <COMMAND>
        Problem: display help menu for user provided command

    Argument: init
    Problem: creates a new project
        Argument: --name
        Problem: create a project using the name of the current working directory
        Inverse: Delete all files created by this command to remove the project
            Argument: <NAME>
            Problem: creates a project with user provided name

    Argument: tool
    Problem: run and install commands provided by python packages
        Argument: install
        Problem: intall commands provided by a python package
        Inverse: uninstall
            Argument: <PACKAGE>
            Problem: the user provided package name to install commands from

        Argument: update-shell
        Problem: ensure that tool executable directory is on the PATH

    Argument: pip
    Problem: manage python packages with pip-compatible interface
        Argument: install
        Problem: install packages into en environment
        Inverse: uninstall

    Argument: venv
    Problem: create a virtual environment

    Argument: run
    Problem: run a command or script
    Constraint: all options to uv must be provided before the command and its options
        Argument: <COMMAND> 
        Problem: Ensures that the command runs in a Python environment
        Constraint: creates a project environment and updates it before invoking command or if virtual environment exists the command will run within it
            Argument: <OPTIONS>
            Problem: arguments are not interpreted as arguments to uv
        Argument: flet
        Problem: runs flet command
            Argument: build
            Problem: build a flutter app
            Contrainst: must specify the target platform: macos | linux | windows | web | apk | aab | ipa | ios-simulator

            Argument: run
            Problem: runs the flet app
