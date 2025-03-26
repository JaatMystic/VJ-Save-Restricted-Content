import os

# Bot token @Botfather
BOT_TOKEN = os.environ.get("BOT_TOKEN", "7666785799:AAE2ma50aAaYZJaqy2G5gYvBb0LfjzdocNU")

# Your API ID from my.telegram.org
API_ID = int(os.environ.get("API_ID", "28624690"))

# Your API Hash from my.telegram.org
API_HASH = os.environ.get("API_HASH", "67e6593b5a9b5ab20b11ccef6700af5b")

# Your Owner / Admin Id For Broadcast 
ADMINS = int(os.environ.get("ADMINS", "7656415064"))

# Your Mongodb Database Url
# Warning - Give Db uri in deploy server environment variable, don't give in repo.
DB_URI = os.environ.get("DB_URI", "mongodb+srv://InSaneOp:82QMu3KRRZNfinJr@cluster0.8zbpi.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0") # Warning - Give Db uri in deploy server environment variable, don't give in repo.
DB_NAME = os.environ.get("DB_NAME", "InSaneOp")

# If You Want Error Message In Your Personal Message Then Turn It True Else If You Don't Want Then Flase
ERROR_MESSAGE = bool(os.environ.get('ERROR_MESSAGE', False))
