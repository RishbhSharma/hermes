from random import randint
from time import time,sleep
from network_base import Network

delay_ms = 100
sys_debug = True

def wait(): sleep(delay_ms/1000.0)
def wait_r(): sleep(delay_ms/1000.0*randint(1,10))

if __name__ == "__main__":

    n = Network([6,7,5,3,9])
    n.check()
