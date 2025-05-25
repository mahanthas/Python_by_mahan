import logging
import subprocess
import os


logging.basicConfig(level=logging.DEBUG)

logging.info("Hello friends")

subprocess.run("ls -l")

os.system("echo hello")