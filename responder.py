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
        
        
    def response(self, input):
        """
　　　　　　　オーバーライドを前提としたresponse()メソッド

            @param input 入力された文字列
            戻り値　空の文字列
        """
        return ''
    
    def get_name(self):
        """ 応答オブジェクトの名前を返す """
        return self.name



class RepeatResponder(Responder):
    """ オウム返しのためのサブクラス """
    def response(self, input):
        """
           応答文字列を作成して返す
        
           @param input 入力された文字列
        """
        return '{}ってなに？'.format(input)



class RandomResponder(Responder):
    """ ランダムな応答のためのサブクラス """    
    def response(self, input):
        """
           応答文字列を作って返す

           @param input 入力された文字列
           戻り値　リストからランダムに抽出した文字列
        """
        return random.choice(self.dictionary.random)



class PatternResponder(Responder):
    """ パターンに反応するためのサブクラス """
    def response(self, input):
        """
            パターンにマッチした場合に応答文字列を生成して返す
            
            @param input 入力された文字列
        """
        for ptn, prs in zip(                          # pattern['pattern]と['phrases']に対して反復処理を行う
            self.dictionary.pattern['pattern'],
            self.dictionary.pattern['phrases']
            ):
            m = re.search(ptn, input)
            if m:                                     # 応答フレーズ(ptn[1])を'|'で切り分けて、ランダムに１文を取り出す
                resp = random.choice(prs.split('|'))
                return re.sub('%match%', m.group(), resp)
        return random.choice(self.dictionary.random)  # パターンにマッチしない場合は、ランダム辞書から返す







