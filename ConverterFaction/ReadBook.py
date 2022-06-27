import pyttsx3
engine = pyttsx3.init() # object creation

""" RATE"""
rate = engine.getProperty('rate')   # getting details of current speaking rate
print (rate)                        #printing current voice rate
engine.setProperty('rate', 125)     # setting up new voice rate between 0~500


"""VOLUME"""
volume = engine.getProperty('volume')   #getting to know current volume level (min=0 and max=1)
print (volume)                          #printing current volume level
engine.setProperty('volume',1.0)    # setting up volume level  between 0 and 1

"""VOICE"""
voices = engine.getProperty('voices')       #getting details of current voice
#engine.setProperty('voice', voices[0].id)  #changing index, changes voices. o for male
'''
打印语音包详细信息并更换语音包id
'''
'''
#for 循环打印语音包的详细信息
for voice in voices:
    print("Voice:")
    print(" - ID: %s" % voice.id)
    print(" - Name: %s" % voice.name)
    print(" - Languages: %s" % voice.languages)
    print(" - Gender: %s" % voice.gender)
    print(" - Age: %s" % voice.age)
#把输出的中文、英文语音包id信息储存起来:'zh'为中文；'en'为英文
zh_voice_id = "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_ZH-CN_HUIHUI_11.0"
en_voice_id = "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_ZIRA_11.0"
engine.setProperty('voice', zh_voice_id)
'''

#engine.setProperty('voice', voices[1].id)  中的voices[]用来选择下标为'1'的语音包(下标从0开始)
engine.setProperty('voice', voices[0].id)   #changing index, changes voices. 1 for female

'''
poem=open("C:\\Users\XMILES\Desktop\work\plan\poem.txt",encoding="utf-8")
txt=[]
for line in poem:
    txt.append(line.strip())
print(txt)
engine.say(txt)
'''
engine.say("Hello World!")
engine.say("想要读中文，需要将voices的数组下标改为0；想要读英文，需要将voices的数组下标改为1")
engine.say('My current speaking rate is ' + str(rate))
engine.runAndWait()
engine.stop()

"""Saving Voice to a file"""
# On linux make sure that 'espeak' and 'ffmpeg' are installed
#生成一个test.mp3的文件到当前文件夹下面
engine.save_to_file('Hello World', 'test.mp3')
engine.runAndWait()