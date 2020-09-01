from translation_api.twinword import Twinword
from translation_api.utils import read_json

translator = Twinword(**read_json('./data/twinword.json'))

print(translator.get('asset'))

