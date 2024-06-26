import os

def setup_script(username):
    os.system('sudo /home/nest-internal/nest-bot/bot/os/scripts/setup.sh ' + username)

def generate_config(username):
    current_dir = os.path.dirname(os.path.abspath(__file__))
    config_dir = os.path.join(current_dir, "template", "etcFile.txt")
    with open(config_dir, "r") as file:
        config = file.read()
        config = config.replace("<username>", username)
        append_to_caddyfile(config)

def home_script(username):
    os.system('sudo /home/nest-internal/nest-bot/bot/os/scripts/create_home.sh ' + username)

def append_to_caddyfile(config):
    with open("/etc/caddy/Caddyfile", "a") as caddyfile:
        caddyfile.write(config)