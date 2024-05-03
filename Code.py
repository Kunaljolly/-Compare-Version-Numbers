class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        v1 = version1.split(".")
        v2 = version2.split(".")
        while(len(v1)!=len(v2)):
            if len(v1)>len(v2):
                v2.append("0")
            if len(v2)>len(v1):
                v1.append("0")
        for x in range(len(min(v1,v2))):
            if int(v1[x]) > int(v2[x]):
                return 1
            if int(v2[x]) > int(v1[x]):
                return -1
        return 0


