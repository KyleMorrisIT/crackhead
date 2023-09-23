# CRACKHEAD
![MARKDOWN IMAGE](https://repository-images.githubusercontent.com/695599971/5facdf3f-bcd9-442c-83c8-1f9dd128943b) 
> the default cracker

Crackhead is a Python script that simplifies the process of cracking default router passwords using Hashcat. It provides a menu-driven interface to select the target router and execute the appropriate Hashcat command. It works in tandem with the glob python module to grab .hc22000 files in the directory and execute a hashcat command appropriate to the keyspace that the particular default utilizes. This is based on the keyspace research conducted by Seytonic in 2016: https://github.com/3mrgnc3/RouterKeySpaceWordlists. Many of these naming conventions are still in use today, and this project was created to demonstrate the insecurity of such devices and provide some automation for fellow pentesters and ethical hackers.

**Disclaimer: This tool is for research and educational purposes only. The author of this software is not responsible for any misuse or malicious use of this tool. Please use it responsibly and only on networks and systems that you are authorized to access. Unauthorized access to computer systems and networks is illegal.**

> Requirements
`pip install glob`
`pip install colorama`
- Python 3.x
- Hashcat installed and configured
- .hc22000 files (Hashcat hashes) in the current directory

> Usage

1. Clone or download this repository to your local machine.
2. Ensure you have Hashcat installed and configured properly.
3. Place the .hc22000 files (Hashcat hashes) in the same directory as the script, or execute from /usr/bin
4. Optionally, make sure you have the required wordlists for specific router models (NETGEARXX is included) by default this file is meant to be moved to usr/share/dict directory but can be modified to the directory of your choice.
5. Run the script using Python:

python crackhead.py
