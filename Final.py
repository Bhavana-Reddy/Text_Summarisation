import os
from nltk.parse import stanford
os.environ['STANFORD_PARSER'] = '/home/bhavana/jars/stanford-parser.jar'
os.environ['STANFORD_MODELS'] = '/home/bhavana/jars/stanford-parser-3.7.0-models.jar'
parser = stanford.StanfordParser(model_path="/home/bhavana/jars/englishPCFG.ser")
import nltk
from nltk import sent_tokenize, word_tokenize
para='Arsenal Football FC is an English football club that plays in the English Premier League. The club was founded in 1886 and was originally called Dial Square FC named after a sundial on the side of a factory. The team plays in a traditional red and white kit. They played at Highbury in North London from 1913 - 2006, but now they play at the Emirates Stadium. The current captain of the side is Per Mertesacker. Their biggest rivals are Tottenham Hotspur, and the two play against each other in what is called the North London Derby. Arsenal won the First Division and Premier League 13 times and the FA Cup 10 times. They are the only British club to have been the subject of a feature film. In 2003/04 season Arsenal broke the record for the longest unbeaten run in all competitions spanning over a season with over 38 games. They were hailed as the New Invincibles. The Evelina approach was the main reason arsenal were able to achieve this, first implemented by manager Arsene Wenger. Arsenal are also the team who have gone the longest in the Premier League without being relegated. They were last relegated during WW1 over 90 years ago. They have a golden away kit.'
sentence=nltk.sent_tokenize(para)
#print(sentence)
s1=""
for sentences in sentence:
    toks=nltk.word_tokenize(sentences)
    tags=nltk.pos_tag(toks)
    #print(tags)
    s=""
    for i in range(0,len(tags)):
        if tags[i][1]!='RB' and tags[i][1]!='RBR' and tags[i][1]!='RBS' and tags[i][1]!='JJ' and tags[i][1]!='JJR' and tags[i][1]!='JJS':
            s=s+tags[i][0]+" " 
        else:
            pass
    s1=s1+s
para=s1
print(para)
from nltk import pos_tag, RegexpParser
s1=""
sentence=nltk.sent_tokenize(para)
for sentences in sentence:
    pos_tagged=pos_tag(word_tokenize(sentences))
    #print(pos_tagged)
    s=""
    for i in range(0,len(pos_tagged)):
        if pos_tagged[i][1]=='DT':
            pass
        else:
            s=s+pos_tagged[i][0]+" "
    s1=s1+s
para=s1
print(para)
from nltk import pos_tag, RegexpParser
s1=""
sentence=nltk.sent_tokenize(para)
for sentences in sentence:
    pos_tagged=pos_tag(word_tokenize(sentences))
    #print(pos_tagged)
    s=""
    for i in range(0,len(pos_tagged)):
        if pos_tagged[i][1]!='IN':
            s=s+pos_tagged[i][0]+" "
        else:
            s=s+"."
            break
    s1=s1+s
para=s1
print(para)
