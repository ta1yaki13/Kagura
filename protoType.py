from kagura import *
    
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

    
    