'''
Author: ni-jingzhe 1448976235@qq.com
Date: 2022-12-15 21:22:00
LastEditors: ni-jingzhe 1448976235@qq.com
LastEditTime: 2023-01-05 22:18:17
FilePath: \EleaiPet\memory.py
Description: 这是默认设置,请设置`customMade`, 打开koroFileHeader查看配置 进行设置: https://github.com/OBKoro1/koro1FileHeader/wiki/%E9%85%8D%E7%BD%AE
'''
import openai
from config import cfg

class Memory(object):

    def __init__(self):
        self.memory = ""
        self.dialog_buffer = []
        self.buffer_max_size = 7
        self.memory_max_length = 100
        self.master_info = cfg.master_info+"以上是你主人的信息，主人只是你的主人，不是别人的。"

    def dialog_buffer_to_string(self, buffer):
        dialog_string = "";
        for str in buffer:
            dialog_string += str+"\n"

        return dialog_string
    
    def summary_content(self, prompt):
        completions = openai.Completion.create(
            engine="text-davinci-003",
            prompt="Please summary the content below with 100 words: "+prompt,
            max_tokens=1000,
            n=1,
            stop=None,
            temperature=0.88,
            top_p=1
        )
        message = completions.choices[0].text
        return message.strip()

    def summary_dialog(self, dialog):
        self.memory += self.summary_content(self.dialog_buffer_to_string(dialog))+"\n"
        self.master_info += self.summary_master_info(self.dialog_buffer_to_string(dialog)) + "\n"
        if(len(self.memory) > self.memory_max_length):
            self.memory = self.summary_content(self.memory)
        if(len(self.master_info) > self.memory_max_length):
            self.master_info = self.summary_content(self.master_info)
        ##self.dialog_buffer = []

    def summary_master_info(self, prompt):
        completions = openai.Completion.create(
            engine="text-davinci-003",
            prompt="Fetch and summary all the information about 主人的 hobbie and habit through the text below.\n"+prompt,
            max_tokens=1000,
            n=1,
            stop=None,
            temperature=0.88,
            top_p=1
        )
        message = completions.choices[0].text
        return message.strip()

    #Function need to be called outside the class
    '''
    def set_master_info(self):
        input_info = input("输入和你自己有关的信息，包括但不限于姓名，年龄，身份等以获得更好的使用体验(用完整的句子说): ")
        self.master_info = "Below are information about your master: \n"+input_info+"\nRemember, master only belongs to you but not anyone else."
    '''
    def append_master_info(self):
        append_info = input("请输入追加的信息: ")
        self.master_info += "Beside，" + append_info

    def get_history_dialog(self):
        return self.dialog_buffer_to_string(self.dialog_buffer)

    def update_memory(self, sentense):
        self.dialog_buffer.append(sentense)
        if len(self.dialog_buffer) > self.buffer_max_size:
            self.summary_dialog(self.dialog_buffer)
            self.dialog_buffer = []
