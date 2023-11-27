from mrjob.job import MRJob
from mrjob.step import MRStep
import re

WORD_RE = re.compile(r"[\w']+")

class MRWordCountInvertedIndex(MRJob):

    def steps(self):
        return [
            MRStep(mapper=self.mapper_count_words,
                   combiner=self.combiner_count_words,
                   reducer=self.reducer_count_words),
            MRStep(reducer=self.reducer_build_inverted_index)
        ]

    def mapper_count_words(self, _, line):
    	file_name = getattr(self, 'input_path', None) or getattr(self, 'options', {}).get('map_input_file')

    	for word in WORD_RE.findall(line):
    	    yield (word.lower(), (file_name, 1))


    def combiner_count_words(self, word, doc_counts):
        total_count = sum(count for file_name, count in doc_counts)
        yield (word, (doc_counts[0][0], total_count))

    def reducer_count_words(self, word, doc_counts):
        yield None, (word, doc_counts)

    def reducer_build_inverted_index(self, _, word_doc_counts):
        for word, doc_counts in word_doc_counts:
            yield word, doc_counts

if __name__ == '__main__':
    MRWordCountInvertedIndex.run()

