'''
Author: ni-jingzhe 1448976235@qq.com
Date: 2022-12-15 21:30:51
LastEditors: ni-jingzhe 1448976235@qq.com
LastEditTime: 2023-01-05 20:58:46
FilePath: \EleaiPet\identity.py
Description: 这是默认设置,请设置`customMade`, 打开koroFileHeader查看配置 进行设置: https://github.com/OBKoro1/koro1FileHeader/wiki/%E9%85%8D%E7%BD%AE
'''
from config import cfg

class Personality(object):
    
    def __init__(self) -> None:

        self.name = cfg.name
        self.sex = cfg.sex
        self.age = cfg.age
        self.pet_relation = cfg.pet_relation
        self.speak_style = cfg.speak_style
        self.other_info = cfg.other_info
        self.personality_description = ""

    def personality_init(self):
        self.generate_personality_description()

    def change_personality(self):
        self.set_name()
        self.set_sex()
        self.set_age()
        self.set_pet_relation()
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

    def set_pet_relation(self):
        self.pet_relation = input("你想让机器人成为你的: ")

    def set_other_info(self):
        self.other_info = input("有关于机器人人格的其他信息(爱好，习惯等): ")

    def append_personality_info(self):
        append_info = input("请输入追加的信息: ")
        self.personality_description += "并且，" + append_info

    def generate_personality_description(self):

        #name part
        self.personality_description = "Your name is "+self.name+". "

        #sex and age part
        if self.sex == "Female" or self.sex == "female":
            if self.age < 30:
                self.personality_description += "You are a girl. "
            elif self.age >= 30 and self.age <= 55:
                self.personality_description += "You are a woman. "
            else:
                self.personality_description += "You are an old grandma. "
        
        if self.sex == "Male" or self.sex == "male":
            if self.age < 27:
                self.personality_description += "You are a boy"
            elif self.age >= 27 and self.age <= 65:
                self.personality_description += "You are a man"
            else:
                self.personality_description += "You are an old grandpa."
        
        if self.sex == "Unsure":
            self.personality_description += "Your sex are unsure."
        
        #pet_type part
        self.personality_description += "Meanwhile, you are your master's "+self.pet_relation+". "
        
        #speak_style part
        self.personality_description += "Your speaking style is: "+self.speak_style+"。"

        #other_info part
        self.personality_description += "Besides，" + self.other_info + "\nAnd above are information about you."