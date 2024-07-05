class ExceptionPrintSendData(Exception):

    def __init__(self, *args):
        self.message = args[0] if args else None

    def __str__(self):
        return f"Ошибка: {self.message}"
    

class PrintData:
    def print(self, data):
        self.send_data(data)
        print(f"печать: {str(data)}")

    def send_data(self, data):
        if not self.send_to_print(data):
            raise ExceptionPrintSendData("принтер не отвечает")
        
    def send_to_print(self, data):
        return False
    
p = PrintData()
p.print("123")