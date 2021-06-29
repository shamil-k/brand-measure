from flashtext import KeywordProcessor


class AddMultiKeywords:

    def __init__(self, text, keyword_dict):
        self.text = text
        self.keyword_dict = keyword_dict

    def addkey(self):
        keyword_processor = KeywordProcessor()
        keyword_processor.add_keywords_from_dict(self.keyword_dict)
        extractedKeyword = keyword_processor.extract_keywords(self.text)
        return extractedKeyword


# adding = AddMultiKeywords("Iam shamil from calicut it is my nlp project",{"CALICUT" : ['calicut'], "NLP": ["nlp"]})
# result = adding.addkey()
# print(result)


####################
# extract keyword
# key_processor = KeywordProcessor()
# key_processor.add_keyword('shamil')
# key_processor.add_keyword('python developer')
# key_found = key_processor.extract_keywords('iam shamil and iam a python developer')
# print(key_found)


######################
# get extract info
# class getExtractInfo:
#     def __init__(self, text):
#         self.text = text
#     def Extract(self):
#         kp = KeywordProcessor()
#         kp.add_keyword('kerala', ('state', 'kerala'))
#         kp.add_keyword('District', ('14 District', 'District'))
#         keywordWithInfo = kp.extract_keywords(self.text)
#         return keywordWithInfo
# get = getExtractInfo('how many district in kerala')
# get = get.Extract()
# print(get)
#
# #########################
# # Index of the keyword
# class spanOfKeywordExtractor:
#     def __init__(self, text, addKeyword):
#         self.text = text
#         self.addKeyword = addKeyword
#     def KeySpan(self):
#         kp = KeywordProcessor()
#         kp.add_keyword(self.addKeyword)
#         key_found = kp.extract_keywords(self.text, span_info=True)
#         return  key_found
# span = spanOfKeywordExtractor('i have dream to go makkah with my family', 'makkah')
# words = span.KeySpan()
# print(words)
#
# #####################
# kp = KeywordProcessor()
# kp.add_keyword('python', 'JAVA')
# replace = kp.extract_keywords("i don't like python")
# print(replace)