import java.util.*;

class Graph {
    int dist[];
    Set<Integer> visited;
    PriorityQueue<Node> q;
    int V; // Number of vertices
    List<List<Node> > adj_list;

    //class constructor
    public Graph(int V) {
        this.V = V;
        dist = new int[V];
        visited = new HashSet<Integer>();
        // by default implement min Priority Queue
        q = new PriorityQueue<Node>(V, new Node());
    }

    // Dijkstra's Algorithm implementation
    public void dijkstra(List<List<Node>> adj_list, int src) {
        this.adj_list = adj_list;

        for (int i = 0; i < V; i++)
            dist[i] = Integer.MAX_VALUE;

        // Distance to the source from itself is 0
        dist[src] = 0;

        // first add source vertex to PriorityQueue
        q.add(new Node(src, 0));

        while (visited.size() != V) {

            // u is removed from PriorityQueue and has min distance
            int u = q.remove().node;

            // add node to finalized list (visited)
            visited.add(u);
            process_neighbours(u);
        }
    }

    // this methods processes all neighbours of the just visited node
    private void process_neighbours(int u)   {
        int edgeDistance = -1;
        int newDistance = -1;

        // process all neighbouring nodes of u
        for (int i = 0; i < adj_list.get(u).size(); i++) {
            Node v = adj_list.get(u).get(i);

            //  proceed only if current node is not in 'visited'
            if (!visited.contains(v.node)) {

                // compare distances    - not [d(v) < d(u) + w(u,v)]
                if (dist[u] + v.cost < dist[v.node])
                    dist[v.node] = dist[u] + v.cost;

                // Add the current vertex to the PriorityQueue
                q.add(new Node(v.node, dist[v.node]));
            }
        }
    }
}

class Graph2 {
    public static void main(String arg[])   {
        int V = 6;
        int source = 0;
        // adjacency list representation of graph
        List<List<Node> > adj_list = new ArrayList<List<Node> >();
        // Initialize adjacency list for every node in the graph
        for (int i = 0; i < V; i++) {
            List<Node> item = new ArrayList<Node>();
            adj_list.add(item);
        }

        // Input graph edges
        adj_list.get(0).add(new Node(1, 5));
        adj_list.get(0).add(new Node(2, 3));
        adj_list.get(0).add(new Node(3, 2));
        adj_list.get(0).add(new Node(4, 3));
        adj_list.get(0).add(new Node(5, 3));
        adj_list.get(2).add(new Node(1, 2));
        adj_list.get(2).add(new Node(3, 3));

        // call Dijkstra's algo method
        Graph graph = new Graph(V);
        graph.dijkstra(adj_list, source);

        // Print the shortest path from source node to all the nodes
        System.out.println("The shorted path from source node to other nodes:");
        System.out.println("Source\t\t" + "Node#\t\t" + "Distance");
        for (int i = 0; i < graph.dist.length; i++)
            System.out.println(source + " \t\t\t " + i + " \t\t\t "  + graph.dist[i]);
    }
}

// Node class
class Node implements Comparator<Node> {
    public int node;
    public int cost;
    public Node() { } //empty constructor

    public Node(int node, int cost) {
        this.node = node;
        this.cost = cost;
    }

    @Override
    public int compare(Node node1, Node node2) {
        if (node1.cost < node2.cost)
            return -1;
        if (node1.cost > node2.cost)
            return 1;
        return 0;
    }
}
