#  https://leetcode.com/problems/simplify-path/

class Solution:
    def cd(list_path):
        if len(list_path) != 0:
            list_path.pop()

    def simplifyPath(self, path: str) -> str:
        res = []
        for s in path.split('/'):
            if s == "..":
                Solution.cd(res)
            elif s != "" and s != ".":
                res.append(s)
        return '/' + '/'.join(res)

s = Solution()
print(s.simplifyPath("/a/./b/../../c/"))
print(s.simplifyPath("/../a/./b/../../c/.."))
