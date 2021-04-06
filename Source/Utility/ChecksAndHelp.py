from Source.Utility import Globals
from Source.Utility.Messaging import send_cancelable_message

#verify if the message received in chat is from the person that called the command
def check(ctx,msg):
    return msg.author == ctx.author and msg.channel == ctx.channel

#verify if we call the same command as the one we are currently in
def is_command_rerun_requested(command, message):
    if command in message:
        return True
    return False

#verifies if a command rerun or cancel is requested
def should_exit_command(current_command,response):
    if is_command_rerun_requested(current_command,response):
        return True
    if Globals.is_cancel_requested:
        Globals.is_cancel_requested = False
        return True
    return False