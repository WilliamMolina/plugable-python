from yapsy.IPlugin import IPlugin

class RabbitMQPlugin(IPlugin):
    def print_name(self):
        print("RabbitMQ Plugin")
        
    def retry(self, host, user, password, message):
        print(host, user, password, message)