""" Kaguraの辞書を扱うファイル """

class Dictionary:
    def __init__(self):
        self.random = []
        randomFile = open('dics/random.txt', 'r', encoding = 'utf-8')  # ランダム辞書を扱う
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
                
        patternFile = open('dics/pattern.txt', 'r', encoding = 'utf-8')  # パターン辞書を扱う
        patternLines = patternFile.readlines()
        patternFile.close()
        
        self.newLines = []
        for line in patternLines:
            str = line.rstrip('\n')
            if (str != ''):
                self.newLines.append(str)


        self.pattern = {}
        for line in self.newLines:
            ptn, prs = line.split('\t')
            self.pattern.setdefault('pattern', []).append(ptn)
            self.pattern.setdefault('phrases', []).append(prs)
