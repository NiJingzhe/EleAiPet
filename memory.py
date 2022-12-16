'''
Author: ni-jingzhe 1448976235@qq.com
Date: 2022-12-15 21:22:00
LastEditors: ni-jingzhe 1448976235@qq.com
LastEditTime: 2022-12-16 23:57:51
FilePath: \EleaiPet\memory.py
Description: 这是默认设置,请设置`customMade`, 打开koroFileHeader查看配置 进行设置: https://github.com/OBKoro1/koro1FileHeader/wiki/%E9%85%8D%E7%BD%AE
'''
import openai

class Memory(object):

    def __init__(self):
        self.memory = ""
        self.dialog_buffer = []
        self.buffer_max_size = 10
        self.memory_max_length = 200
        self.master_info = ""

    def dialog_buffer_to_string(self, buffer):
        dialog_string = "";
        for str in buffer:
            dialog_string += str+"\n"

        return dialog_string
    
    def summary_content(self, prompt):
        completions = openai.Completion.create(
            engine="text-davinci-003",
            prompt="概括以下对话内容: "+prompt,
            max_tokens=1000,
            n=1,
            stop=None,
            temperature=0.3,
        )
        message = completions.choices[0].text
        return message.strip()

    def summary_dialog(self, dialog):
        self.memory += self.summary_content(self.dialog_buffer_to_string(dialog))+"\n"
        if(len(self.memory) > self.memory_max_length):
            self.memory = self.summary_content(self.memory)

    #Function need to be called outside the class
    def set_master_info(self):
        input_info = input("输入和你自己有关的信息，包括但不限于姓名，年龄，身份等以获得更好的使用体验(用完整的句子说): ")
        self.master_info = "以下是你的主人的信息: \n"+input_info+"\n记住，他\她是只是你的主人，不是别人的的主人"

    def append_master_info(self):
        append_info = input("请输入追加的信息: ")
        self.master_info += "并且，" + append_info

    def get_history_dialog(self):
        return self.dialog_buffer_to_string(self.dialog_buffer)

    def update_memory(self, sentense):
        self.dialog_buffer.append(sentense)
        if len(self.dialog_buffer) > self.buffer_max_size:
            self.summary_dialog(self.dialog_buffer)
