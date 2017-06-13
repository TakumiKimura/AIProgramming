class CommunicationBot:
    name = ""
    messageList = {"おはよう":"おはようございます！", "こんにちは": "こんにちは！", "こんばんは":"眠いです!",}

    def NameMessageCommand(message):
        message_len = len(message)
        if(messgae == "あなたの名前はなんですか？"):
            if(name == ""):
                return "(名前は)ないです"
            else:
                return "私の名前は、「" + name + "」です。"
        elif(message[:7] == "あなたの名前は" and message[message_len-2:message_len] == "です"):
            return "私の名前は、「"+ name + "」ですね。覚えました"
        else:
            return False

    def OtherMessageCommand(messgae):
        if(message == "exit" or message == "さようなら"):
            return "さようなら。また、会いましょう。"
        else:
            return "そのメッセージに対する返答を、私は知りません。"

    def SendMessage(message):
        ret_var = _nameMessageCommand(message)
        if(ret_var != False):
            return nameCommand
        elif(messageList.has_key(message)):
            return messageList[message]
        else:
            ret_var = _otherMessageCommand(message)
            return ret_var

    def MainLoop(loopCount = 5):
        for i in range(loopCount):
            message = str( input("メッセージを入力してください："))
            print( _sendMessage( message ) ) 
        else:
            print("今日はもう眠いです。");
            
bot = CommunicationBot()
bot.MainLoop()
