from responder import *

class Kagura:
    """カグラの本体クラス"""
    def __init__(self, name):
        """Kaguraオブジェクトの名前をnameに格納する
        　　Responderオブジェクトを生成してresponderに格納する
        
            @param name  Kaguraオブジェクトの名前
        """
        self.name = name
        self.responder = RandomResponder('Random')
        
    def dialogue(self, input):
        """応答オブジェクトのresponse()を呼び出して、
            応答文字列を取得する
            
            ＠param input ユーザにより入力された文字列
            戻り値　応答文字列
        """
        return self.responder.response(input)
    
    def get_responder_name(self):
        """応答オブジェクトの名前を返す
        """
        return self.responder.name
    
    def get_name(self):
        """Kaguraオブジェクトの名前を返す
        """
        return self.name