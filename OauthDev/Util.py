from datetime import datetime

def getNow():
    return datetime.utcnow().strftime("%Y-%m-%d %H:%M:%S")      # <--- Visst ville vi använda utcnow() istället för now()?
