'''
Author: ni-jingzhe 1448976235@qq.com
Date: 2022-12-15 23:04:18
LastEditors: ni-jingzhe 1448976235@qq.com
LastEditTime: 2023-01-05 20:58:48
FilePath: \EleaiPet\main.py
Description: 这是默认设置,请设置`customMade`, 打开koroFileHeader查看配置 进行设置: https://github.com/OBKoro1/koro1FileHeader/wiki/%E9%85%8D%E7%BD%AE
'''
from eleaipet import EleaiPet
import openai
from config import cfg



openai.api_key=cfg.API_KEY

pet = EleaiPet()

if __name__ == "__main__":
 
    pet.pet_init()
    pet.start_coversation()