class Solution(object):
    def simplifyPath(self, path):
        """
        :type path: str
        :rtype: str
        """
        stack = []
        sep = path.split("/")

        for p in sep:
            if p == "." or not p:
                continue
            elif p =="..":
                if stack:
                    stack.pop()
            else:
                stack.append(p)
        return "/" + '/'.join(stack)

        