import tkinter as tk
from kagura import *

"""グローバル変数の定義"""
entry = None                # 入力エリアのオブジェクトを保持
response_area = None        # 応答エリアのオブジェクトを保持
logListBox = None           # ログ表示用のリストボックスを保持
action = None               # 'オプション'メニューの状態を保持
kagura = Kagura('kagura')   # Kaguraのオブジェクトを保持

def putlog(str):
    """
       対話ログをリストボックスに追加する関数
       @str  入力文字列または、応答メッセージ
    """
    logListBox.insert(tk.END, str)
    
def prompt():
    """
        Kaguraのプロンプトを作る関数
    """
    kaguraName = kagura.name
    if (action.get()) == 0:
        kaguraName += ':' + kagura.responder.name
    return kaguraName + '> '

def talk():
    """
        対話を行う関数
        ・Kaguraクラスのdialogue()を実行して応答メッセージを取得する
        ・入力文字列および、応答メッセージをログに出力する
    """
    value = entry.get()
    
    if not value:       # 入力エリアが未入力の場合
        response_area.configure(text='なに？')
    else:               # 入力エリアに入力されていた場合
        response = kagura.dialogue(value)       # 入力文字列を引数にしてdialogue()の結果を表示する
        response_area.configure(text=response)  # 応答メッセージを表示する
        putlog('> ' + value)                    # 入力文字列引数にしてputlog()を呼ぶ
        putlog(prompt() + response)             # 応答メッセージを引数にしてputlog()を呼ぶ
        entry.delete(0, tk.END)                 # 入力エリアをクリアする
        
"""
###############################################################################################
# 画面を描画する関数
###############################################################################################
"""

def run():
    global entry, response_area, logListBox, action    # グローバル変数を使用するための記述
    
    """ メインウィンドウ """
    root = tk.Tk()                  # メインウィンドウの作成する
    root.geometry('880x590')        # ウィンドウのサイズの設定
    root.title('Kagura of Pal')     # ウィンドウのタイトルの設定
    font = ('Helevetica', 14)       # フォントの設定
    font_log = ('Helevetica', 11)   # フォントの設定
    
    """ メニューバー """
    menuBar = tk.Menu(root)
    root.config(menu = menuBar)
    
    """ 「ファイル」メニュー """
    fileMenu = tk.Menu(menuBar)
    menuBar.add_cascade(label  = 'ファイル', menu    = fileMenu)
    fileMenu.add_cascade(label = '閉じる',  command  = root.destroy)
    
    """ 「オプション」メニュー """
    action = tk.IntVar()
    optionMenu = tk.Menu(menuBar)
    menuBar.add_cascade(label = 'オプション', menu = optionMenu)
    optionMenu.add_radiobutton(
        label    = 'Responderを表示',    # アイテム名
        variable = action,              # 選択時の値を格納するオブジェクト
        value    = 0                    # actionの値を０にする
        )
    optionMenu.add_radiobutton(
        label    = 'Responderを表示しない',    # アイテム名
        variable = action,                   # 選択時の値を格納するオブジェクト
        value    = 1                         # actionの値を1にする
        )
    
    """ キャンバスの作成 """
    canvas = tk.Canvas(
        root,                # 親要素をメインウィンドウに設定する
        width  = 500,        # 幅の設定
        height = 300,        # 高さの設定
        relief = tk.RIDGE,   # 枠線の表示
        bd     = 2           # 枠線の幅の設定
        )
    canvas.place(x = 370, y = 0)                                  # メインウィンドウ上に配置する
    img = tk.PhotoImage(file = 'kaguraPngFile/kaguraUsual.png')   #  表示するイメージを用意
    canvas.create_image(                                          # キャンバス上にイメージを配置する
        0,                                                        # x座標
        0,                                                        # y座標
        image = img,                                              # 配置するイメージオブジェクトを指定する
        anchor = tk.NW                                            # 配置の起点となる位置を左上隅に指定する
        )
    
    """ 応答エリアを作成 """
    response_area = tk.Label(
        root,                             # 親要素をメインウィンドウに設定
        width  = 45,                      # 幅の設定
        height = 7,                       # 高さの設定
        bg     = 'salmon',                # 背景色の設定
        font   = font,                    # フォントの設定
        relief = tk.RIDGE,                # 枠線の種類の設定
        bd     = 2                        # 枠線の幅の設定
        )
    response_area.place(x = 370, y = 305)  # メインウィンドウ上に配置
    
    """ フレームの作成 """
    frame = tk.Frame(
        root,                             # 親要素をメインウィンドウに設定する
        relief      = tk.RIDGE,           # ボーダーの種類
        borderwidth = 4                   # ボーダー幅の設定
        )
    
    """ 入力ボックスの作成 """
    entry = tk.Entry(
        frame,                            # 親要素はフレーム
        width = 60,                       # 幅の設定
        font  = font                      # フォントの設定
        )
    entry.pack(side = tk.LEFT)            # フレームに左詰めで配置する
    entry.focus_set()                     # 入力ボックスに焦点を当てる
    
    """ ボタンの作成 """
    button = tk.Button(
        frame,                            # 親要素はフレーム
        width   = 15,                     # 幅の設定
        text    = '話す',                  # ボタンに表示するテキスト   
        command = talk                    # クリック時にtalk()関数を呼ぶ
        )
    button.pack(side = tk.LEFT)           # フレームに左詰めで配置する
    frame.place(x = 30, y = 520)          # フレームを画面上に配置する
    
    """ リストボックスを作成 """
    logListBox = tk.Listbox(
        root,                             # 親要素はメインウィンドウ
        width  = 42,                      # 幅の設定
        height = 20,                      # 高さの設定
        font   = font_log                 # フォントの設定
        )
    
    """ 縦のスクロールバーを生成 """
    verticalScrollBar = tk.Scrollbar(
        root,                             # 親要素はメインウィンドウ
        orient  = tk.VERTICAL,            # 縦方向のスクロールバーにする
        command = logListBox.yview           # スクロール時に、listBoxのyview()メソッドを呼ぶ
        )
    
    """ 横のスクロールバーの生成 """
    horizontalScrollBar = tk.Scrollbar(
        root,                             # 親要素はメインウィンドウ
        orient  = tk.HORIZONTAL,          # 横方向のスクロールバーにする
        command = logListBox.xview           # スクロール時に、listBoxのxview()メソッドを呼ぶ
        )
    
    """ リストボックスとスクロールバーの連動を行う """
    logListBox.configure(yscrollcommand = verticalScrollBar.set)
    logListBox.configure(xscrollcommand = horizontalScrollBar.set)
    
    """ grid()でリストボックス、スクロールバーを画面上に配置する """
    logListBox.grid(row = 0, column = 0)
    verticalScrollBar.grid(row   = 0, column = 1, sticky = tk.NS)
    horizontalScrollBar.grid(row = 1, column = 0, sticky = tk.EW)
    
    """ メインループ """
    root.mainloop()
    
    
"""
###############################################################################################
# プログラムの起点
###############################################################################################
"""

if __name__ == '__main__':
    run()
    
