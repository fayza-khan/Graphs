"""
Given two words beginWord and endWord, and a dictionary wordList, return the length of the shortest transformation sequence 
from beginWord to endWord, such that:

Only one letter can be changed at a time.
Each transformed word must exist in the word list.
Return 0 if there is no such transformation sequence.


Example 1:

Input: beginWord = "hit", endWord = "cog", wordList = ["hot","dot","dog","lot","log","cog"]
Output: 5
Explanation: As one shortest transformation is "hit" -> "hot" -> "dot" -> "dog" -> "cog", return its length 5.
Example 2:

Input: beginWord = "hit", endWord = "cog", wordList = ["hot","dot","dog","lot","log"]
Output: 0
Explanation: The endWord "cog" is not in wordList, therefore no possible transformation.
 

Constraints:

1 <= beginWord.length <= 100
endWord.length == beginWord.length
1 <= wordList.length <= 5000
wordList[i].length == beginWord.length
beginWord, endWord, and wordList[i] consist of lowercase English letters.
beginWord != endWord
All the strings in wordList are unique.

"""


from collections import defaultdict
class Solution:
    def ladderLength(self, beg: str, end: str, word: List[str]) -> int:
        # Edge case
        if end not in word:
            return 0
        if len(end) == 1 and len(beg) == 1:
            return 2
        word = [beg] + word
        g = defaultdict(list)
        for one in word:
            for i in range(len(one)):
                main = one[:i]+"_"+one[i+1:]
                g[main].append(one)
        dic = defaultdict(list)
        
        # create a dictionary.
        
        for key in g:
            for val in g[key]:
                for others in g[key]:
                    if others != val and others not in dic[val]:
                        dic[val].append(others)
        
        # using graph's shortest path algorithm - Dijkstra's algorithm
       
        n = len(word)
        dist = [float("inf")]*n
        startindex = word.index(beg)
        endindex = word.index(end)
        dist[startindex] = 0
        vis = set()
        
        # checking validity of the indices
        
        def isvalid(visited, distance, words):
            mn = float("inf")
            index = None
            for i in range(len(words)):
                if distance[i] < mn and words[i] not in visited:
                    mn = distance[i]
                    index = i
            return index
        for _ in range(n):
            u = isvalid(vis, dist, word)
            if u is not None:
                vis.add(word[u])
                for v in dic[word[u]]:
                    ind = word.index(v)
                    if v not in vis and (dist[u] + 1) < dist[ind]:
                        dist[ind] = dist[u] + 1
        if dist[endindex] == float("inf"):
            return 0
        return dist[endindex] + 1
            
        
