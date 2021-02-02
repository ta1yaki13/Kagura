""" Kaguraの辞書を扱うファイル """
import random
import re

class Dictionary:
    def __init__(self):
         # ランダム辞書を扱う
        self.random = []
        randomFile = open('dics/random.txt', 'r', encoding = 'utf-8') 
        randomLines = randomFile.readlines()
        randomFile.close()
        
        self.random = []
        for line in randomLines:
            str = line.rstrip('\n')
            if (str != ''):
                self.random.append(str)
                
        """ テスト用
        self.miss = []
        missFile = open('dics/miss.txt', 'r', encoding = 'utf-8')  # ランダム辞書を扱う
        missLines = missFile.readlines()
        missFile.close()
        
        
        self.miss = []
        for line in missLines:
            str = line.rstrip('\n')
            if (str != ''):
                self.miss.append(str)
        """
         # パターン辞書を扱う       
        patternFile = open('dics/pattern.txt', 'r', encoding = 'utf-8') 
        patternLines = patternFile.readlines()
        patternFile.close()
        
        self.newLines = []
        for line in patternLines:
            str = line.rstrip('\n')
            if (str != ''):
                self.newLines.append(str)


        self.pattern = []
        for line in self.newLines:
            ptn, prs = line.split('\t')
            self.pattern.append(ParseItem(ptn, prs))


class ParseItem:
    SEPARATOR = '^((-?\d+)##)?(.*)$'
    
    def __init__(self, pattern, phrases):
        """
            @param pattern パターン
            @param phrases パターン
        """
        m = re.findall(ParseItem.SEPARATOR, pattern)              # 辞書のパターンの部分にSEPARATORをパターンマッチさせる
        
        self.modify = 0
        if m[0][1]:                                               # マッチ結果の整数の部分が空でなければ値を再代入
            self.modify = int(m[0][1])
        
        self.pattern = m[0][2]
        self.phrases = []                                          # 応答例を保持するインスタンス変数
        self.dic = {}
        
        for phraseMatch in phrases.split('|'):                     # 引数で渡された応答例を'|'で分割し、
            m = re.findall(ParseItem.SEPARATOR, phraseMatch)       # 個々の要素に対してSEPARATORをパターンマッチさせる
            self.dic['need'] = 0                                   # self.phrases['need'  : 応答例の整数部分
            if m[0][1]:　　　　　　　　　　　　　　　　　　　　　　　　　　　 #　　　　　　　 　'phrase': 応答例の文字列部分]
                self.dic['need'] = int(m[0][1])                    # 'need'キーの値を整数部分m[0][1]にする
            self.dic['phrase'] = m[0][2]                           # 'phrase'キーの値を応答文字列m[0][2]にする
            self.phrases.append(self.dic.copy())                   # 作成した辞書をphrasesリストに追加
            
    def match(self, str):
        """
            ・self.pattern（各行ごとの正規表現）をインプット文字列にパターンマッチ
        """
        return re.search(self.pattern, str)
    
    
    def choice(self, mood):
        """
            ・インスタンス変数phrases(リスト)の要素
            
            @param mood 現在の機嫌値
        """
        choicesList = []
        
        for phrasesList in self.phrases:                            # self.phrasesが保持するリストの要素を反復処理する
            if (self.suitable(phrasesList['need'], mood)):          # self.pharasesの'need'キーの数値とパラメータmoodを
                choicesList.append(phrasesList['phrase'])           # suitable()に渡す
                
        if (len(choicesList) == 0):
            return None
        return random.choice(choicesList)
    
    
    def suitable(self, need, mood):
        """
            ・インスタンス変数phrases(リスト)の要素
            
            @param need 必要機嫌値
            @param mood 現在の機嫌値
        """
        if (need == 0):                                             # 必要機嫌値の判定
            return True
        elif (need > 0):
            return (mood > need)
        else:
            return (mood < need)
        