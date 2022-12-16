'''
Author: ni-jingzhe 1448976235@qq.com
Date: 2022-12-15 20:37:31
LastEditors: ni-jingzhe 1448976235@qq.com
LastEditTime: 2022-12-15 23:35:33
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
10.能帮我把水杯拿来吗: 祈使句 '''

        self.attitude_train_data = '''
1.请打开电视机: 中性 
2.你真的很厉害呢: 夸奖 
3.对！这件事情是非常惊人的: 赞叹 
4.原来如此。你今天过得怎么样？: 友好 
5.是这样啊！难道不是吗: 肯定
6.不行啊这样: 否定
7.你很聪明哦!: 夸奖 
8.没毛病: 肯定
9.你能告诉我这个问题的解吗？: 感兴趣 
10.这是错误的!: 否定
11.我不行啊: 消沉
12.害，别说了，再说真的要伤心了: 消沉'''

    def type_judge(self, prompt):
        completions = openai.Completion.create(
            engine="text-ada-001",
            prompt="Please classify the sentense type based on the example: "+self.type_train_data+" 11."+prompt+": ",
            max_tokens=512,
            n=1,
            stop=["12."],
            temperature=0.3,
        )
        message = completions.choices[0].text
        return message.strip()

    def attitude_judge(self, prompt):
        completions = openai.Completion.create(
            engine="text-babbage-001",
            prompt="Please classify speaker's attitude based on the example: "+self.attitude_train_data+" 13."+prompt+": ",
            max_tokens=512,
            n=1,
            stop=["14."],
            temperature=0.3,
        )
        message = completions.choices[0].text
        return message.strip()

    def constructe_better_input(self, prompt, type, attitude):

        if type == "陈述句":
            prompt = "我陈述道: "+prompt
        
        elif type == "感叹句":
            prompt = "我感叹道: "+prompt+"!"

        elif type == "反问句":
            prompt = "我反问道: "+prompt+"？"

        elif type == "疑问句":
            prompt = "我提问道: "+prompt+"？"

        elif type == "祈使句":
            prompt = "我命令道: "+prompt
        
        else:
            prompt = "我说: "+prompt

        prompt = "带着"+attitude+"的语气, "+prompt
        
        return prompt

    #Function need to be called outside the class
    def pre_process(self, user_input):

        return ">>>"+self.constructe_better_input(user_input, self.type_judge(user_input), self.attitude_judge(user_input))
