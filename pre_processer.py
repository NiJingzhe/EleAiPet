'''
Author: ni-jingzhe 1448976235@qq.com
Date: 2022-12-15 20:37:31
LastEditors: ni-jingzhe 1448976235@qq.com
LastEditTime: 2023-01-06 15:32:12
FilePath: \EleaiPet\lib\pre_processer.py
Description: 这是默认设置,请设置`customMade`, 打开koroFileHeader查看配置 进行设置: https://github.com/OBKoro1/koro1FileHeader/wiki/%E9%85%8D%E7%BD%AE
'''
import openai

class Pre_Processer(object):

    def __init__(self) -> None:
        
        self.type_train_data = '''
1.请打开电视机: 祈使句 
2.你真的很厉害呢: 感叹句 
3.对！这件事情是非常惊人的: 陈述句 
4.原来如此。你今天过得怎么样？: 疑问句 
5.是这样啊？难道不是吗: 反问句 
6.帮我把那件衣服拿过来: 祈使句 
7.你很聪明哦!: 感叹句 
8.没毛病: 陈述句 
9.你能告诉我这个问题的解吗？: 疑问句 
10.能帮我把水杯拿来吗: 祈使句
11.哈喽呀!!: 问候语
12.你好捏: 问候语
13.Hei bro!: 问候语'''

        self.attitude_train_data = '''
1.请打开电视机: a neutral tone;
2.你真的很厉害呢: a praise tone;
3.对！这件事情是非常惊人的: an admiring tone;
4.原来如此。你今天过得怎么样？: a friendly tone;
5.是这样啊！难道不是吗: an affirmative tone;
6.不行啊这样: a negative tone;
7.很好！: a praise tone;
8.没毛病: an affirmative tone;
9.你能告诉我这个问题的解吗？: an interested tone; 
10.这是错误的!: a negative tone;
11.我不行啊: a depressed tone;
12.害，别说了，再说真的要伤心了: a depressed tone;'''

    def type_judge(self, prompt):
        completions = openai.Completion.create(
            engine="text-davinci-001",
            prompt="基于以下样例完成句式分类"+self.type_train_data+"\n13."+prompt+": ",
            max_tokens=512,
            n=1,
            stop=["14."],
            temperature=0.3,
            top_p=0.5
        )
        message = completions.choices[0].text
        ##print(message.strip())
        return message.strip()

    def attitude_judge(self, prompt):
        completions = openai.Completion.create(
            engine="text-davinci-001",
            prompt="Please classify tone based on the example:\n"+self.attitude_train_data+"\n13."+prompt+": ",
            max_tokens=512,
            n=1,
            stop=[";","."],
            temperature=0.3,
            top_p=0.5
        )
        message = completions.choices[0].text
        return message.strip()

    def constructe_better_input(self, prompt, type, attitude):

        if type == "陈述句":
            prompt = "I stated: "+prompt
        
        elif type == "感叹句":
            prompt = "I exclaimed: "+prompt+"!"

        elif type == "反问句":
            prompt = "I asked rhetorically: "+prompt+"？"

        elif type == "疑问句":
            prompt = "I asked:: "+prompt+"？"

        elif type == "祈使句":
            prompt = "I commanded: "+prompt
        
        elif type == "问候语":
            prompt = "I extend my greeting and said:"+prompt
        else:
            prompt = "I said: "+prompt

        prompt = "With "+attitude+", "+prompt
        
        return prompt

    #Function need to be called outside the class
    def pre_process(self, user_input):

        return ">>>"+self.constructe_better_input(user_input, self.type_judge(user_input), self.attitude_judge(user_input))
