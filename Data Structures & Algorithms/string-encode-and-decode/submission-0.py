class Solution:

    def encode(self, strs: List[str]) -> str:
        result=''
        for word in strs:
            result+=str(len(word))+"#"+word
        return result

    def decode(self, s: str) -> List[str]:
        result1=[]
        i=0
        while i<len(s):
            j=s.find('#',i)
            length=int(s[i:j])
            word=s[j+1:j+length+1]
            result1.append(word)

            i=j+length+1
        return result1    