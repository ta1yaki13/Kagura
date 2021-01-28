import random


class Responder:
    """応答クラス
    """
    def __init__(self, name):
        """Responderオブジェクトの名前をnameに格納する

            @param name Responderオブジェクトの名前
        """
        self.name = name
        
    def response(self, input):
        """オーバーライドを前提としたresponse()メソッド

            @param input 入力された文字列
            戻り値　空の文字列
        """
        return ''
    
    def get_name(self):
        """応答オブジェクトの名前を返す
        """
        return self.name
    
class RepeatResponder(Responder):
    """オウム返しのためのサブクラス
    """
    def response(self, input):
        """応答文字列を作成して返す
        
           @param input 入力された文字列
        """
        return '{}ってなに？'.format(input)
    
class RandomResponder(Responder):
    """ランダムな応答のためのサブクラス
    """
    def __init__(self, name):
        """1 Responderオブジェクトの名前を引数にして、
                スーパークラスの__init__()を呼び出す
           2 ランダムに抽出するメッセージを格納したリストを作成する
           
           @param name Responderオブジェクトの名前
        """
        super().__init__(name)
        self.responses = ['いい天気だね', 'ご飯食べた？', '遊びにいこうー']
        
    def response(self, name):
        """応答文字列を作って返す

           @param input 入力された文字列
           戻り理　リストからランダムに抽出した文字列
        """
        return (random.choice(self.responses))
    
