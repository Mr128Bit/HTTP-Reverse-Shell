# HTTP Reverse Shell

## Overview

The HTTP Reverse Shell is a tool designed for educational purposes to demonstrate how an attacker might use covert channels over HTTP for remote command execution. This tool should only be used in controlled environments and with proper authorization.

## Features

- Covert communication using HTTP.
- Based on a simple Flask web server.
- Reverse shell functionality for remote control.
- Stealthy traffic to evade simple network detection.

## Usage

1. **Server Side:**
   - Run the Flask server on the target machine:
     ```bash
     python server.py
     ```
   - Make sure the server is accessible from the internet or desired network.

2. **Client Side:**
   - Run the generated payload from the reverse shell
  
3. **Command Execution:**
   - Once the client is connected, the server can send commands to the client, and the client executes them.

## Disclaimer

This tool is created for educational and ethical purposes only. Unauthorized use of this tool may violate applicable laws. Use this tool responsibly and with proper authorization. The creator is not responsible for any misuse or damage caused by the tool.

## License

This project is licensed under the [MIT License](LICENSE).
