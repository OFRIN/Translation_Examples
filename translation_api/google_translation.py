from googletrans import Translator

class google_translation:
    def __init__(self):
        self.translator = Translator()

    def detect(self, text):
        return self.translator.detect(text).lang

    def translate(self, data, source='ko', target='en'):
        dataset = self.translator.translate(data, src=source, dest=target)
        