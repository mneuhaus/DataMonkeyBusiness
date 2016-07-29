from textblob import TextBlob

text = '''
The titular threat of The Blob has always struck me as the ultimate movie
monster: an insatiably hungry, amoeba-like mass able to penetrate
virtually any safeguard, capable of--as a doomed doctor chillingly
describes it--"assimilating flesh on contact.
Snide comparisons to gelatin be damned, it's a concept with the most
devastating of potential consequences, not unlike the grey goo scenario
proposed by technological theorists fearful of
artificial intelligence run rampant.
'''

text = '''
The future is looking awesome #Gigafactory #tesla
'''

blob = TextBlob(text)

print(blob.tags)

print(blob.noun_phrases)

for sentence in blob.sentences:
    print("The future is looking bright #Gigafactory: ", sentence.sentiment.polarity)





# text = '''
# The future is looking grim #Gigafactory
# '''

# blob = TextBlob(text)

# for sentence in blob.sentences:
#     print("The future is looking grim #Gigafactory: ", sentence.sentiment.polarity)

# # 0.060
# # -0.341