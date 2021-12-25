class Solution:
    def findAllRecipes(self, recipes: List[str], ingredients: List[List[str]], supplies: List[str]) -> List[str]:
        s = set(supplies)
        i = list(map(set, ingredients))
        b = True
        while b:
            b = False
            for j, r in enumerate(recipes):
                if i[j].issubset(s) and r not in s:
                    s.add(r)
                    b = True
        return list(s & set(recipes))