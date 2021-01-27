class Kagura:
    """カグラの本体クラス"""
    def __init__(self, name):
        """Kaguraオブジェクトの名前をnameに格納する
        　　Responderオブジェクトを生成してresponderに格納する
        
            @param name  Kaguraオブジェクトの名前
        """
        self.name = name
        self.responder = Responder('What')
        
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
    
class Responder:
    """応答クラス
    """
    def __init__(self, name):
        """Responderオブジェクトの名前をnameに格納する

            @param name Responderオブジェクトの名前
        """
        self.name = name
        
    def response(self, input):
        """応答文字列を作って返す

            @param input 入力された文字列
        """
        return '{}ってなに？'.format(input)
    
#################################################################################################
    #実行ブロック
#################################################################################################
    
def prompt(obj):
    """カグラのプロンプトを作成する関数
        戻り値　'Kaguraオブジェクト名:応答オブジェクト名 > '
    """
    return obj.get_name() + ':' + obj.get_responder_name() + '> '

print('Kagura System prototype : Kagura') #プログラムの情報を表示
kagura = Kagura('kagura')                 #kaguraオブジェクトを生成する

while True:
    inputs = input('> ')
    if not inputs:
        print('バイバイ')
        break
    response = kagura.dialogue(inputs)    #応答文字列を取得する
    print(prompt(kagura), response)       #プロンプトと応答文字列をつなげて表示する

    
    