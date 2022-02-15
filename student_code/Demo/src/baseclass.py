class SearchEngineBase(object):
	def __init__(self):
		pass

	def add_corpus(self, file_path):
		"""添加语料库
		add_corpus() 函数负责读取文件内容，将文件路径作为 ID，连同内容一起送到 process_corpus 中。
		"""
		with open(file_path, 'r') as fin:
			text = fin.read()
		self.process_corpus(file_path, text)

	def process_corpus(self, id, text):
		"""索引器/过程语料库
		process_corpus 需要对内容进行处理，然后文件路径为 ID ，将处理后的内容存下来。处理后的内容，就叫做索引（index）。
		"""
		raise Exception('process_corpus not implemented.')

	def search(self, query):
		"""检索器/搜查"""
		raise Exception('search not implemented.')


class SimpleEngine(SearchEngineBase):
	def __init__(self):
		super(SimpleEngine, self).__init__()
		self.__id_to_texts = {}

	def process_corpus(self, id, text):
		self.__id_to_texts[id] = text

	def search(self, query):
		results = []
		for id, text in self.__id_to_texts.items():
			if query in text:
				results.append(id)
		return results


def main(search_engine):
	for file_path in ['../data/1.txt', '../data/2.txt', '../data/3.txt', '../data/4.txt', '../data/5.txt']:
		search_engine.add_corpus(file_path)

	while True:
		# pass
		query = input("请输入你要查询的内容：>>>")
		results = search_engine.search(query)
		print('found {} result(s):'.format(len(results)))
		for result in results:
			print(result)


search_engine = SimpleEngine()
main(search_engine)
