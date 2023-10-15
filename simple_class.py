class InfoLog():
    def __init__(self, message):
        self.message = message
    
    def log(self):
        print(f"INFO | {self.message}")

# Create an instance of the InfoLog class
# ant initialize it with a sample message
info_log = InfoLog("InfoLog sample message")

# Call the IfoLog log() method
info_log.log()