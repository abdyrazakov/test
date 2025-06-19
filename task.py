
class Notifier:
    def notify(self, name, message):
        raise NotImplementedError("Notifier subclasses must implement the notify method")

class EmailNotifier(Notifier):
    def __init__(self, email):
       
        self.email = email
    def notify(self,name,  message):
        print(f"Senfing email message to {self.name} email:{self.email} message:{self.message}")

class TelegramNotifier(Notifier):
    def __init__(self,adress):
        self.adress = adress
    def notify(self,name,  message):
        print(f"Senfing Telegram message to {self.name} email:{self.adress} message:{self.message}")



class User:
    def __init__(self, name, preferred_notifier):
        self.name = name
        self.preferred_notifier = preferred_notifier

    def send_notifications(users,message):
        for user in users:
            user.preferred_notifier.notify(user.name, message)

users = [
    User("Alice", EmailNotifier("alice@mail.com")),
    User("Bob", TelegramNotifier("@bob123"))
]

result = User.send_notifications(users, "Добро пожаловать!")