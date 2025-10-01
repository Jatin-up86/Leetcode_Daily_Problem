import heapq
class TaskManager:

    def __init__(self, tasks: List[List[int]]):
        self.tasks=list()
        self.taskmap=defaultdict(tuple)
        for u,t,p in tasks:
            heapq.heappush(self.tasks,(-p,-t,u))
            self.taskmap[t]=(p,u)
        

    def add(self, userId: int, taskId: int, priority: int) -> None:
        heapq.heappush(self.tasks,(-priority,-taskId,userId))
        self.taskmap[taskId]=(priority,userId)
        

    def edit(self, taskId: int, newPriority: int) -> None:
        prev_p,u=self.taskmap[taskId]
        self.taskmap[taskId]=(newPriority,u)
        heapq.heappush(self.tasks,(-newPriority,-taskId,u))

    def rmv(self, taskId: int) -> None:
        self.taskmap[taskId]=(-1,-1)
        

    def execTop(self) -> int:
        while self.tasks:
            p,t,u=self.tasks[0]
            p=-p
            t=-t
            real=self.taskmap[t]
            if real[0]==p:
                self.rmv(t)
                return real[1]
            heapq.heappop(self.tasks)
        return -1
        


# Your TaskManager object will be instantiated and called as such:
# obj = TaskManager(tasks)
# obj.add(userId,taskId,priority)
# obj.edit(taskId,newPriority)
# obj.rmv(taskId)
# param_4 = obj.execTop()