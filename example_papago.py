
from translation_api.papago import Papago
from translation_api.utils import read_json

translator = Papago(**read_json('./data/papago.json'))

sentence = input('ko->en ? ')

print(sentence)
print(translator.en2ko_translate(sentence))

