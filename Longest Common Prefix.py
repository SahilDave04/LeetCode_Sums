#Write a function to find the longest common prefix string amongst an array of strings. If there is no common prefix, return an empty string "".
def longestCommonPrefix(self, strs: List[str]) -> str:
  szs = []
  for i in range(0,len(strs)):
          szs.append(len(strs[i]))
  sz = (sorted(szs))[0]  
  cnt = -1
  for j in range(0,sz):
          comp = []
          for l in range(0,len(strs)):
                  comp.append((strs[0])[j])
          #print(comp)
          wrd = []
          for k in range(0,len(strs)):
                  itm = (strs[k])[j]
                  wrd.append(itm)
          #print(wrd)
          if wrd == comp:
                  #print(True)
                  cnt += 1
          else:
                  break
  prfx = (strs[0])[0:cnt+1]
  return prfx
