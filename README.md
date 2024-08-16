# Stealthy Multi-OS Key Logger

## Overview:
This key logger is designed to operate discreetly across different operating systems, including Windows, macOS, and Linux. It runs quietly in the background, capturing and sending keystrokes without drawing attention.

Key Features:

- Cross-Platform Support: Works seamlessly on Windows, macOS, and Linux, providing consistent performance regardless of the operating system.

- Invisible Operation: Runs without any visible notifications or alerts, making it hard to detect and ensuring it operates under the radar.

- Silent Mode: The software doesn’t display any messages or logs activity to the screen, maintaining complete stealth.

- Secure Transmission: Sends captured keystrokes to a remote server using secure methods, with options to encrypt the data for extra protection.

- Flexible Logging: You can set how often the data is sent, whether at regular intervals or based on specific events, giving you control over monitoring.

- Reliable: Handles errors gracefully, so it continues to work even if there are network issues or other problems.

- Data Handling: Captured keystrokes can be saved locally or sent to a server, with measures in place to protect this data from unauthorized access.

Applications:

- Security Monitoring: Keep track of activity on systems to detect unauthorized access.

- Parental Controls: Monitor usage on family computers to ensure safety.

- Corporate Oversight: Ensure compliance with company policies and safeguard sensitive information.

## How to Use

 - Download keylogger.py and server.py (obf.py provides the keylogger in obfuscated format and is optional to download)
   
 - Install External Modules:
   `pip3 install pynput requests`

 - Change the IP Address to the attacker machine on keylogger.py and server.py.

 - Run keylogger.py on the victim machine:
   `python3 keylogger`

 - Run server.py on the attacker Machine:
   `python3 server.py`
   
 - Kill the process if something goes wrong:
   `sudo pkill python3 keylogger.py` or `taskkill /IM python.exe keylogger.py` if on Windows.

Important Note: Make sure to use this tool responsibly and legally. Unauthorized key logging can violate privacy laws and regulations. Always get proper consent and follow relevant legal guidelines.
