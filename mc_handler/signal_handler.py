import os
import signal
import sys
import random
import subprocess

class signal_handler:
    """Abstract out the signal handling part."""
    def __init__(self):
        self.pids = []
        self.val =  []
        self.alarm_callback = None # User specific alarm action.
        self.signal_callback = None # User specific signal action.


    def alarm_handler(self, signum, stack):
        print("Alarm recieved.")
        if self.alarm_callback:
            self.alarm_callback(signum)


    def sig_handler(self, sig):
        print("Signal : {} Recieved.\n", sig)
        if self.signal_callback:
            self.signal_callback(sig)


    def list_signal_handlers(self):
        """List the currently registered signal handlers."""
        signal_name_dict = {}
        for n in dir(signal):
            if n.startwith('SIG')and not n.startwith('SIG_'):
                signal_name_dict[getattr(signal, n)] = n

        for s, name in sorted(signal_name_dict.items()):
            handler = signal.getsignal(s)

            if handler is signal.SIG_DFL:
                handler = 'SIG_DFL'
            elif handler is signal.IGN:
                handler = 'SIG_IGN'
            print("{:<10d} -- {:<10d}".format(s, handler))


    def raise_signal_to_pid(self, pid, sig):
        """Raise a USR signal to given pid."""
        if sig is signal.SIGUSR1 or signal.SIGUSR2:
            os.kill(pid, getattr(signal, sig))
        else:
            print("Only user signals SIGUSR1 and SIGUSR2 are supported.\n")


    def common_handler(self, args):

        if len(args) < 2:
            print("Signal Handler: No valid argument provided.\n")
            sys.exit()

        arg = args[0]
        if arg == 'register':
            # Register a handler  for user signals.
            signal.signal(signal.SIGUSR1, sig_handler)
            signal.signal(signal.SIGUSR2, sig_handler)
        elif arg == 'list':
            # List all the current registered handlers for signal.
            list_signal_handlers()
        elif arg == 'raise':
            # Raise a signal of user provided value.
            pid = int(args[1])
            raise_signal_to_pid(pid)
        elif arg == 'alarm':
            # Arm an alarm.
            signal.signal(signal.SIGALRM, alarm_handler)
            try:
                alarm_time = int(args[1])
            except AttributeError:
                print("Provide alarm value as input.\n")
                sys.exit()
            signal.alarm(alarm_time)
        else:
            print("Undefined parameter recieved.")
    
    def register_signal_callback(self, callback = None):
        """Register user specific callback"""
        if callback:
            self.signal_callback = callback
        else:
            print("Warning: Callback set to None.")

    def register_alarm_callback(self, callback = None):
        if callback:
            self.alarm_callback = callback
        else:
            print("Warning: Callback set to None.")

#***Test stub.******
#def main():
#    signal_handler handler
#    handler.common_handler("list")

#if __name__ =='__main__':
#    main()
#*******************
