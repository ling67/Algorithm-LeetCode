"""
Word Count Engine
Implement a document scanning function wordCountEngine, which receives a string document and
returns a list of all unique words in it and their number of occurrences,
sorted by the number of occurrences in a descending order.
If two or more words have the same count, they should be sorted according to their order in the original sentence.
Assume that all letters are in english alphabet. You function should be case-insensitive,
so for instance, the words “Perfect” and “perfect” should be considered the same word.
The engine should strip out punctuation (even in the middle of a word) and use whitespaces to separate words.
Analyze the time and space complexities of your solution.
Try to optimize for time while keeping a polynomial space complexity.
Examples:
input:  document = "Practice makes perfect. you'll only
                    get Perfect by practice. just practice!"
output: [ ["practice", "3"], ["perfect", "2"],
          ["makes", "1"], ["youll", "1"], ["only", "1"],
          ["get", "1"], ["by", "1"], ["just", "1"] ]
Important: please convert the occurrence integers in the output list to strings (e.g. "3" instead of 3).
We ask this because in compiled languages such as C#, Java, C++, C etc.,
it’s not straightforward to create mixed-type arrays (as it is, for instance,
in scripted languages like JavaScript, Python, Ruby etc.).
The expected output will simply be an array of string arrays.
Constraints:
[time limit] 5000ms
[input] string document
[output] array.array.string
"""

"""
use freq as idx to do bucket sort
"""
def word_count_engine(document):
    word_to_cnt = collections.defaultdict(int)

    # step 1: put all words to word_to_cnt
    words = document.split(" ")
    for i in range(len(words)):
        temp = ''
        for ch in words[i]:
            if ch.isalpha():
                temp += ch.lower()
        words[i] = temp

    for word in words:
        if word != "":
            word_to_cnt[word] += 1

    # step 2: create a bucket and put all words into bucket (index is the frequency)
    max_cnt = max(cnt for cnt in word_to_cnt.values())
    bucket = [[] for _ in range(max_cnt + 1)]
    for word in words:    # 注意不能去遍历word_to_cnt, 因为我们需要maintain relative order for words with same freq
        if word in word_to_cnt:
          bucket[word_to_cnt[word]].append(word)
          del word_to_cnt[word]   # delete it so that we don't add "practice" 3 times

    # step 3: generate res
    res = []
    for i in range(len(bucket) - 1, -1, -1):
        temp = []
        for word in bucket[i]:
            temp.append([word, str(i)])
        res += temp
    return res
