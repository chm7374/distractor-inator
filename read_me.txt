chm7374@rit.edu
DISTRACT-INATOR Tool - READ ME

The DISTRACT-INATOR is a red team tool that attempts to distract and flood the packet capture
software of a network with random gibberish to make finding any actual meaningful traffic with
them essentially pointless.

For maximum effect, it is recommended to have multiple instances of the tool running. Even
if one manages to get shut down, there will be many more in its place.

Attack option 1: Run this program in the background on a machine directly linked to the network.
Attack option 2: Run this program on a root-privileged machine that is able to reach the target.

This program can and should be run simultaneously with other copies of itself. Ending the program
results in some error messages being outputted, but that is nothing to worry about.

Specifications:
- MUST BE RUN ON LINUX MACHINE!
- MAKE SURE YOUR INPUTS ARE CORRECT!
- MAKE SURE python3, pip package, and requests packages ARE INSTALLED!