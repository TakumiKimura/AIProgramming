class CommunicationBot:
    name = ""
    messageList = {"おはよう":"おはようございます！",
            "こんにちは": "こんにちは！",
            "こんばんは":"眠いです!"}

    def __init__(self, name = ""):
        self.name = name

    def mainLoop(self):
        for i in range(5):
            message = str( input("メッセージを入力してください："))
            ret_message = self.sendMessage(message)
            print(ret_message)
            if(ret_message == "さようなら。また、会いましょう。"):
                break
        else:
            print("今日はもう眠いです。");

    def sendMessage(self, message):
        ret_var = self.nameMessageCommand(message)
        if(ret_var != "not defined"):
            return ret_var
        elif(message in self.messageList):
            return self.messageList[message]
        else:
            ret_var = self.otherMessageCommand(message)
            return ret_var

    def nameMessageCommand(self, message):
        message_len = len(message)
        if(message == "あなたの名前はなんですか？"):
            if(self.name == ""):
                return "(名前は)ないです"
            else:
                return "私の名前は、「" + self.name + "」です。"
        elif(message[:7] == "あなたの名前は" and message[message_len-2:message_len] == "です"):
            self.name = message[7:message_len-2]
            return "私の名前は、「"+ self.name + "」ですね。覚えました"
        else:
            return "not defined"

    def otherMessageCommand(self, message):
        if(message == "exit" or message == "さようなら"):
            return "さようなら。また、会いましょう。"
        else:
            return "そのメッセージに対する返答を、私は知りません。"

    def addMessageCommand(self, key, value):
        self.messageList[key] = value
        
            
if __name__ == "__main__":
    import sys
    bot = CommunicationBot(sys.argv[1])
    bot.mainLoop()
