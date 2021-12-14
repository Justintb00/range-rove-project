import pymysql

class database:
    def __init__(self):
        self.host = '127.0.0.1'
        self.port = 33060
        self.database = 'picar_database'
        self.user = 'root'
        self.password = 'admin1234'
        self.connection = None
        self.cursor = None
    
    def connect(self):
        try:
            self.connection = pymysql.connect(
                host=self.host,
                port=self.port,
                database=self.database,
                user=self.user,
                password=self.password
                )
            self.cursor = self.connection.cursor
        except:
            print(f"Connection could not be established to {self.host}:{self.port}")
    
    def disconnect(self):
        if self.connection:
            self.connection.close()
            self.connection = None
            self.cursor = None
            print("Succesfully Disconnected")
    