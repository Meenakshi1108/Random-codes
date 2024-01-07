class Solution:
    
    def max_util(node,score,value,flag,l):
        if(flag==1):
            for i in adj[node]:
                tk+=max_util(i,score+value[i],value,1,l-1)
            return tk
        if(flag==0):
            for i in adj[node]:
                ntk=max_util(i,score,value,1,l-1)
                tk=max_util(i,score,value,0,l-1)
                
            
    
    
    
    
    def maximumScoreAfterOperations(self, edges: List[List[int]], values: List[int]) -> int:
        score = 0
        adj = {i: [] for i in range(n)}  

        for i in range(len(edges)):
            adj[edges[i][0]].append(edges[i][1])
            adj[edges[i][1]].append(edges[i][0])
        
        queue=[0]
        
        while(len(queue)!=0):
            node=queue.pop(0)
            l=len(adj[node])
            max_score=0
            for neighbour in adj(node):
                take_root=self.max_util(neighbour,max_score+values[node],values,0,l-1)
                not_take_root=self.max_util(neighbour,max_score,values,1,l-1)
                