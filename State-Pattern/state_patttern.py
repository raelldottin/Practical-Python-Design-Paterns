import curses
import time


class State(object):
    def __init__(self, state_machine):
        self.state_machine = state_machine

    def switch(self, in_key):
        if in_key in self.state_machine.mapping:
            self.state_machine.state = self.state_machine.mapping[in_key]
        else:
            self.state_machine.state = self.state_machine.mapping["default"]


class Standing(State):
    def __str__(self):
        return "Standing"


class RunningLeft(State):
    def __str__(self):
        return "Running Left"


class RunningRight(State):
    def __str__(self):
        return "Running Right"


class Jumping(State):
    def __str__(self):
        return "Jumping"


class Crouching(State):
    def __str__(self):
        return "Crouching"


class StateMachine(object):
    def __init__(self):
        self.standing = Standing(self)
        self.running_left = RunningLeft(self)
        self.running_right = RunningRight(self)
        self.jumping = Jumping(self)
        self.crouching = Crouching(self)

        self.mapping = {
            "a": self.running_left,
            "d": self.running_right,
            "s": self.crouching,
            "w": self.jumping,
            "default": self.standing,
        }

        self.state = self.standing

    def action(self, in_key):
        self.state.switch(in_key)

    def __str__(self):
        return str(self.state)


def main():
    player1 = StateMachine()
    win = curses.initscr()
    curses.noecho()

    win.addstr(0, 0, "press the keys w a s d to initiate actions")
    win.addstr(1, 0, "press x to exit")
    win.addstr(2, 0, "> ")
    win.move(2, 2)

    while True:
        ch = win.getch()
        if ch is not None:
            win.move(2, 0)
            win.deleteln()
            win.addstr(2, 0, "> ")
            if ch == 120:
                break
            player1.action(chr(ch))
            print(player1.state)
        time.sleep(0.05)


if __name__ == "__main__":
    main()
