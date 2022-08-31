from environs import Env

# using 'enviros' module, to get data from the .env file
env = Env()
env.read_env()

BOT_TOKEN = env.str("BOT_TOKEN")  # taking BOT_TOKEN as a string
ADMINS = env.list("ADMINS")  # creating the list of admins
IP = env.str("ip")  # ip address of the host
