'''
Author: ni-jingzhe 1448976235@qq.com
Date: 2022-12-12 15:51:57
LastEditors: ni-jingzhe 1448976235@qq.com
LastEditTime: 2023-01-06 15:37:48
FilePath: \ChatGPT\test.py
Description: 这是默认设置,请设置`customMade`, 打开koroFileHeader查看配置 进行设置: https://github.com/OBKoro1/koro1FileHeader/wiki/%E9%85%8D%E7%BD%AE
'''
import openai
from pre_processer import Pre_Processer
from memory import Memory
from personality import Personality
from config import cfg


class EleaiPet(object):



    def __init__(self) -> None:
        self.memory_model = Memory()
        self.personality_model = Personality()
        self.pre_processer = Pre_Processer()

    def pet_init(self):
        self.personality_model.personality_init()
        ##self.memory_model.set_master_info()
    '''
    def traslation(self, input, target):
        completions = openai.Completion.create(
            engine="text-davinci-002",
            prompt="Translate the sentence below into "+target+"\nand here are some tips you should pay attention to: "+cfg.translation_tips+input,
            max_tokens=1024,
            n=1,
            stop=[">>>"+self.personality_model.name+": ",">>>"],
            temperature=0.88,
            top_p=1
        )
        message_after_translation = completions.choices[0].text
        return message_after_translation.strip();
    '''
    def generate_answer(self, user_input):
        user_input = self.pre_processer.pre_process(user_input)
        
        self.memory_model.update_memory(user_input)
        
        completions = openai.Completion.create(
            engine="text-davinci-003",
            prompt="Your Infromation: "+self.personality_model.personality_description+
                   "\nInformation of your 主人: "+self.memory_model.master_info+
                   "\nDialogue summary: "+self.memory_model.memory+
                   "\nplease continue the conversation: \n"+self.memory_model.get_history_dialog()+self.personality_model.name+": ",
            max_tokens=1024,
            n=1,
            stop=[">>>"],
            temperature=0.88,
            top_p=1
        )
        message = completions.choices[0].text

        print(self.personality_model.name+": "+message.strip())

        
        self.memory_model.update_memory(">>>"+self.personality_model.name+": "+message.strip())
        
        
    def start_coversation(self):
        while True:
            user_input = input(">>> ")
            if user_input == "EXIT":
                exit(0)
            elif user_input == "APPEND_PET_INFO":
                self.personality_model.append_personality_info()
            elif user_input == "CHANGE_PET_INFO":
                self.personality_model.change_personality()
            elif user_input == "APPEND_MASTER_INFO":
                self.memory_model.append_master_info()
            elif user_input == "CHECK_MEMORY":
                print("\nMEMORY: \n"+self.memory_model.memory+"\n------------ END ------------")
            elif user_input == "CHECK_DIALOG_BUFFER":
                print("\nBUFFER: \n"+self.memory_model.dialog_buffer_to_string(self.memory_model.dialog_buffer)+"\n------------ END ------------")
            elif user_input == "CHECK_MASTER_INFO":
                print("\nMASTER_INFO: \n"+self.memory_model.master_info+"\n------------ END ------------")
            else:
                self.generate_answer(user_input)

            user_input = ""