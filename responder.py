import random
import re


class Responder:
    """ 応答クラス """
    def __init__(self, name, dictionary):
        """
　　　　　　　Responderオブジェクトの名前をnameに格納する

            @param name       Responderオブジェクトの名前
            @param dictionary Dictionaryオブジェクト
        """
        self.name = name
        self.dictionary = dictionary
        
        
    def response(self, input, mood):
        """
　　　　　　　オーバーライドを前提としたresponse()メソッド

            @param input 入力された文字列
            @param mood  機嫌値
            戻り値　空の文字列
        """
        return ''
    
    def get_name(self):
        """ 応答オブジェクトの名前を返す """
        return self.name



class RepeatResponder(Responder):
    """ オウム返しのためのサブクラス """
    def response(self, input, mood):
        """
           応答文字列を作成して返す
        
           @param input 入力された文字列
           @param mood  機嫌値
        """
        return '{}ってなに？'.format(input)



class RandomResponder(Responder):
    """ ランダムな応答のためのサブクラス """    
    def response(self, input, mood):
        """
           応答文字列を作って返す

           @param input 入力された文字列
           @param mood  機嫌値
           戻り値　リストからランダムに抽出した文字列
        """
        return random.choice(self.dictionary.random)



class PatternResponder(Responder):
    """ パターンに反応するためのサブクラス """
    def response(self, input, mood):
        """
            パターンにマッチした場合に応答文字列を生成して返す
            
            @param input 入力された文字列
            @param mood  機嫌値
        """
        self.resp = None
        
        for patternItem in self.dictionary.pattern:                # match()でインプット文字列にパターンマッチを行う
            m = patternItem.match(input)
            if (m):
                self.resp = patternItem.choice(mood)
            
            if self.resp != None:
                return re.sub('%match%', m.group(), self.resp)
        return random.choice(self.dictionary.random)               # パターンマッチしない場合はランダム辞書から返す







