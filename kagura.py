from responder import *
from dictionary import *

class Kagura:
    """カグラの本体クラス"""
    def __init__(self, name):
        """Kaguraオブジェクトの名前をnameに格納する
        　　Responderオブジェクトを生成してresponderに格納する
        
            @param name  Kaguraオブジェクトの名前
        """
        self.name = name
        self.dictionary = Dictionary()                       # Dictionaryを生成する
        
        self.responder_Random = RandomResponder('Random', self.dictionary)    # RandomResponderを生成
        self.responder_Repeat = RepeatResponder('Repeat', self.dictionary)    # RepeatResponderを生成
        self.responder_Pattern = PatternResponder('Pattern', self.dictionary) # PatternResponderを生成
        
    def dialogue(self, input):
        """応答オブジェクトのresponse()を呼び出して、
            応答文字列を取得する
            
            ＠param input ユーザにより入力された文字列
            戻り値　応答文字列
        """
        
        x = random.randint(1, 100)                             # 0か1をランダムに生成
        
        if x <= 60:
            self.responder = self.responder_Pattern
        elif 61 <= x <= 90:
            self.responder = self.responder_Random
        else:
            self.responder = self.responder_Repeat
        return self.responder.response(input)

    def get_responder_name(self):
        """ 応答オブジェクトの名前を返す """
        return self.responder.name
    
    def get_name(self):
        """ Kaguraオブジェクトの名前を返す """
        return self.name
