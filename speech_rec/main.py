# importing libraries
import speech_recognition as sr
from speech_rec.utils.logger import logger, Colorize
import spacy
import re


PATH = '/opt/dna/speech_recognition/datalake/medroom/transient/'
NER = spacy.load("pt_core_news_sm")


class SpeechRecognition:

    def __init__(self,audio_file):

        self.audio_file = audio_file

        super().__init__()
    
    @classmethod
    def call_processor(self, audio_file):

        # Initialize recognizer class (for recognizing the speech)
        r = sr.Recognizer()

        # Reading Audio file as source
        # listening the audio file and store in audio_text variable

        with sr.AudioFile(PATH + audio_file) as source:
            
            audio_text = r.listen(source)
            
        # recoginize_() method will throw a request error if the API is unreachable, hence using exception handling
            try:
                
                # using google speech recognition
                text = r.recognize_google(audio_text, language = "pt-BR")
                logger.info('Converting audio transcripts into text ...')
                logger.info(text)
            
            except:
                logger.info('Sorry.. run again...')

        return text
    
    @classmethod
    def ner(self,text, parser='spacy', ner_type = '', anonymizer = False, custom_anonymizer = '<UNK>'):
        
        output = []
        
        if isinstance(ner_type, str):
            ner_type = [ner_type]
            
        if parser == 'spacy':

            ner = NER(text)
            for entidade in ner.ents:   

                if anonymizer:
                    if len(ner_type) == 0:
                        print('WARNING: Please Specify An Entity Type.')
                        return text

                    for ner in ner_type:
                        if entidade.label_ == ner:
                            try:
                                text = re.sub(entidade.text, custom_anonymizer, text)
                            except:
                                text = text
                    output = text
                else:
                    output.append(
                        self.detect_pattern(entidade.text, entidade.text, entidade.label_, entidade.start_char, entidade.end_char)
                    )
        else:
            print('Invalid Parser.')

        return output
        

    @classmethod
    def detect_pattern(self, match, key, ner_type, start_index, end_index):
        # TODO: add score 
        return {
            "entity": match,
            "value": key,
            "type": ner_type, 
            "startIndex": start_index,
            "endIndex": end_index,
        }