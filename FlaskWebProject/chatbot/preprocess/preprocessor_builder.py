'''Module to define the creational logic for a message preprocessor'''
import tokenizer_simple
import stopwords_remover_lenient
import stemming_lancaster
import preprocessor

def build():
    return preprocessor.MessagePreprocessor(tokenizer=tokenizer_simple.SimpleTokenizerProxy(),
                                        stopwordRemover=stopwords_remover_lenient.StopwordRemoverLenient(),
                                        stemmer=stemming_lancaster.Lancaster())
