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
        self.emotion = Emotion(self.dictionary)
        
        self.responder_Random = RandomResponder('Random', self.dictionary)    # RandomResponderを生成
        self.responder_Repeat = RepeatResponder('Repeat', self.dictionary)    # RepeatResponderを生成
        self.responder_Pattern = PatternResponder('Pattern', self.dictionary) # PatternResponderを生成
        
    def dialogue(self, input):
        """応答オブジェクトのresponse()を呼び出して、
            応答文字列を取得する
            
            ＠param input ユーザにより入力された文字列
            戻り値　応答文字列
        """
        self.emotion.update(input)
        
        x = random.randint(1, 100)                             # 0か1をランダムに生成
        
        if x <= 60:
            self.responder = self.responder_Pattern
        elif 61 <= x <= 90:
            self.responder = self.responder_Random
        else:
            self.responder = self.responder_Repeat
        return self.responder.response(input, self.emotion.mood)

    def get_responder_name(self):
        """ 応答オブジェクトの名前を返す """
        return self.responder.name
    
    def get_name(self):
        """ Kaguraオブジェクトの名前を返す """
        return self.name


class Emotion:
    """
        Kaguraの感情モデル
    """
    MOOD_MIN = -15             # 機嫌値の最低値と最高値と回復値
    MOOD_MAX = 15
    MOOD_RECOVERY = 0.5
    
    def __init__(self, dictionary):
        """
            ・Dictionaryオブジェクトをdictionaryに格納する
            ・機嫌値moodを０に初期化する

            @param dictionary Dictionaryオブジェクト
        """
        self.dictionary = dictionary
        self.mood = 0                 # 機嫌値を保持するインスタンス変数
        
    def update(self, input):
        """
            ・ユーザからの入力をパラメータinputで受け取り
            　パターン辞書にマッチさせて機嫌値を変動させる
            
            @param input ユーザからの入力
        """
        for patternItem in self.dictionary.pattern:     # パターン辞書の各行を繰り返しパターンマッチさせる
            if patternItem.match(input):
                self.adjust_mood(patternItem.modify)
                break
            
        if self.mood < 0:                               # 機嫌を徐々に戻していく処理
            self.mood += Emotion.MOOD_RECOVERY
        elif self.mood > 0:
            self.mood -= Emotion.MOOD_RECOVERY
            

    def adjust_mood(self, val):
        """
            ・機嫌値を増減させる
            
            @param val 機嫌変動値
        """
        self.mood += int(val)                           # 機嫌値moodの値を機嫌変動値により増減する
        
        if self.mood > Emotion.MOOD_MAX:                # MOOD_MAXとMOOD_MINと比較して、機嫌値が取り得る範囲に収める
            self.mood = Emotion.MOOD_MAX
        elif self.mood < Emotion.MOOD_MIN:
            self.mood = Emotion.MOOD_MIN



