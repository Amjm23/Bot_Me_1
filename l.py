import subprocess
import psutil
from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext

TOKEN = '8058933713:AAGesdo-vkB9I6lFO-naz3ncZ8_EIVCDmOM'

AUTHORIZED_USERS = [1544133696]

def start(update: Update, context: CallbackContext):
    if update.effective_user.id not in AUTHORIZED_USERS:
        update.message.reply_text("You do not have access to this bot.")
        return
    update.message.reply_text("Administrative panel is active.")

def sent_command(update: Update, context: CallbackContext):
    if update.effective_user.id not in AUTHORIZED_USERS:
        update.message.reply_text("You do not have access to this bot.")
        return
    if context.args:
        command = ' '.join(context.args)
        try:
            output = subprocess.check_output(command, shell=True, stderr=subprocess.STDOUT, universal_newlines=True)
            
            if len(output) > 4000:
                output = output[:4000] + "\n... Output truncated ..."
            update.message.reply_text(f"**Command Output:**\n```\n{output}\n```", parse_mode='Markdown')
        except subprocess.CalledProcessError as e:
            update.message.reply_text(f"**Error executing command:**\n```\n{e.output}\n```", parse_mode='Markdown')
    else:
        update.message.reply_text("Please provide a command to execute. Example: /sent ls")

def online_command(update: Update, context: CallbackContext):
    if update.effective_user.id not in AUTHORIZED_USERS:
        update.message.reply_text("You do not have access to this bot.")
        return

    servers = [
        {'os': 'Linux', 'memory': f"{psutil.virtual_memory().total // (1024**3)} GB", 'cpu': f"{psutil.cpu_count()} Cores"},
        {'os': 'Windows', 'memory': f"{psutil.virtual_memory().total // (1024**3)} GB", 'cpu': f"{psutil.cpu_count()} Cores"},
    ]

    response = f"**Total Servers:** {len(servers)}\n\n"
    for idx, server in enumerate(servers, 1):
        response += f"**Server {idx}:**\n- OS: {server['os']}\n- Memory: {server['memory']}\n- CPU: {server['cpu']}\n\n"

    update.message.reply_text(response, parse_mode='Markdown')

def main():
    updater = Updater(TOKEN, use_context=True)
    dp = updater.dispatcher

    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("sent", sent_command))
    dp.add_handler(CommandHandler("online", online_command))

    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()

