import platform
import subprocess


def ping(host):
    """
    Returns True if host (str) responds to a app request.
    Remember that a host may not respond to a app (ICMP) request even if the host name is valid.
    """

    # Option for the number of packets as a function of
    param = '-n' if platform.system().lower()=='windows' else '-c'

    # Building the command. Ex: "app -c 1 google.com"
    command = ['ping', param, '1', host]

    return subprocess.call(command) == 0


