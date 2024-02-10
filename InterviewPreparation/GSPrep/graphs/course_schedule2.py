def courseSchedule2(numCourses: int, prerequisites: list[list[int]]) -> list[int]:
    prereq = {c: [] for c in numCourses}
    cycle = set()
    visit = set()
    output = []
    for crs, pre in prerequisites:
        prereq[crs].append(pre)

    def dfs(crs):
        if crs in cycle:
            return False
        if crs in visit:
            return True

        cycle.add(crs)
        for pre in prerequisites[crs]:
            if dfs(pre) == False:
                return False
        cycle.remove(crs)
        visit.add(crs)
        output.add(crs)

        return True

    for c in range(numCourses):
        if dfs(c) == False:
            return []
    
    return output