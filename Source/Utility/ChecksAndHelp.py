import glob

def is_command_rerun_requested(command, message):
    if command in message:
        return True
    return False