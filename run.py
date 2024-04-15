from app import app
from config import Server

if __name__ == "__main__":
    app.run(host=Server.SERVER_DOMAIN, port=Server.SERVER_PORT, debug=True)
