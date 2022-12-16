'''
Author: ni-jingzhe 1448976235@qq.com
Date: 2022-12-15 21:30:51
LastEditors: ni-jingzhe 1448976235@qq.com
LastEditTime: 2022-12-15 23:25:13
FilePath: \EleaiPet\identity.py
Description: 这是默认设置,请设置`customMade`, 打开koroFileHeader查看配置 进行设置: https://github.com/OBKoro1/koro1FileHeader/wiki/%E9%85%8D%E7%BD%AE
'''
class Personality(object):
    
    def __init__(self) -> None:

        self.name = ""
        self.sex = ""
        self.age = 0
        self.speak_style = ""
        self.other_info = ""
        self.personality_description = ""

    def personality_init(self):
        self.set_name()
        self.set_sex()
        self.set_age()
        self.set_speak_style()
        self.set_other_info()
        self.generate_personality_description()

    def set_name(self):
        self.name = input("给机器人起个名字吧(别太长): ")     

    def set_sex(self):
        self.sex = input("设定性别(输入Male或Female或Unsure): ")

    def set_age(self):
        self.age = int(input("设定年龄(别给我整负数啊小数啊这样的幺蛾子): "))     

    def set_speak_style(self):
        self.speak_style = input("设定说话风格: ")

    def set_other_info(self):
        self.other_info = input("有关于机器人人格的其他信息(爱好，习惯等): ")

    def append_personality_info(self):
        append_info = input("请输入追加的信息: ")
        self.personality_description += "并且，" + append_info

    def generate_personality_description(self):

        #name part
        self.personality_description = "你的名字是"+self.name+"。"

        #sex and age part
        if self.sex == "Female" or self.sex == "female":
            if self.age < 30:
                self.personality_description += "你是一位女孩。"
            elif self.age >= 30 and self.age <= 55:
                self.personality_description += "你是一位女士。"
            else:
                self.personality_description += "你是一位老奶奶。"
        
        if self.sex == "Male" or self.sex == "male":
            if self.age < 27:
                self.personality_description += "你是一位男孩。"
            elif self.age >= 27 and self.age <= 65:
                self.personality_description += "你是一位男士。"
            else:
                self.personality_description += "你是一位老爷爷。"

        if self.sex == "Unsure":
            self.personality_description += "你的性别不确定。"

        #speak_style part
        self.personality_description += "你说话的风格是: "+self.speak_style+"。"

        #other_info part
        self.personality_description += "与此同时，" + self.other_info + "\n以上是你的信息。"