def word_break(s, words):
    d = [False] * len(s)
    for i in range(len(s)):
        for w in words:#开头和结尾都为True，那么d[i]为true
            if w == s[i-len(w)+1:i+1] and (d[i-len(w)] or i-len(w) == -1):#i-len(w)表示比如leet是从leetcode的首字母开始，刚开始d中都是false，只能从这句话判断真伪
                d[i] = True
        print(d)
    return d[-1]


s = 'appleapin'#"leetcode" # 'applepinapple' 'apple,pin'
words = ['apple','pin']
word_break(s,words)