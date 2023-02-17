public class Solution {
    public boolean canFinish(int numCourses, int[][] prerequisites) {
        
        //map each vertex to its list of adjacent vertices
        HashMap<Integer, List<Integer>> map = new HashMap<Integer, List<Integer>>(); 
        for(int i = 0; i < numCourses; i++) 
        map.put(i, new LinkedList<Integer>());

        //record the in-degree of each vertex
        int[] indegree = new int[numCourses]; 

        for(int[] edge : prerequisites){
            indegree[edge[0]]++;
            map.get(edge[1]).add(edge[0]);
        }

        //determine all vertices with zero in-degree
        Queue<Integer> zeroVerts = new LinkedList<Integer>(); 
        for(int i = 0; i < numCourses; i++)
            if(indegree[i] == 0) 
               zeroVerts.offer(i);

        //number of courses could be put into the topological order
        int courseOrder = 0; 
        while(!zeroVerts.isEmpty()){
            int course = zeroVerts.poll(); 
            courseOrder++;
            //"remove" vertex by updating its neighbors
	        for(int c : map.get(course)){
	            indegree[c]--;
                //add any vertex that now has 0 in-degree to the queue
	            if(indegree[c] == 0) 
	               zeroVerts.offer(c);
	        }
        }
        return courseOrder == numCourses;   //must ==, if there is cicle, courseOrder with be 0, we should return false.
    }
}
