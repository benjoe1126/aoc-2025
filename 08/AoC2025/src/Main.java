import java.io.File;
import java.io.FileNotFoundException;
import java.util.*;

class Coordinate3D {
    private final long x,y,z;
    public Coordinate3D(long x,long y,long z){
        this.x = x;
        this.y = y;
        this.z = z;
    }

    public final long getX(){
        return x;
    }
    public double length() {
        return Math.sqrt(x * x + y * y + z * z);
    }

    public double distanceFrom(Coordinate3D other){
        return new Coordinate3D(x - other.x, y - other.y, z - other.z).length();
    }
    @Override
    public String toString(){
        return String.format("{%d, %d, %d}",this.x, this.y, this.z);
    }
}

class Edge {
    private final Coordinate3D start;
    private final Coordinate3D end;
    private final double weight;
    public Edge(Coordinate3D x, Coordinate3D y, double weight){
        start = x;
        end = y;
        this.weight = weight;
    }
    public Coordinate3D getStart(){
        return start;
    }

    public Coordinate3D getEnd() {
        return end;
    }

    public double getWeight(){
        return weight;
    }
}

public class Main {
    private static ArrayList<Coordinate3D> fromFile(String fileName) throws FileNotFoundException {
        var ret = new ArrayList<Coordinate3D>();
        var f = new File(fileName);
        Scanner sc = new Scanner(f);
        while(sc.hasNextLine()){
            String line = sc.nextLine();
            var splitted = line.split(",");
            ret.add(new Coordinate3D(Integer.parseInt(splitted[0]),Integer.parseInt(splitted[1]),Integer.parseInt(splitted[2])));
        }
        return ret;
    }
    private static int[] getTwoClosestIndex(double[][] distances, boolean[][] inCircuitTable){
        var ret = new int[]{0, 0};
        double min = Double.MAX_VALUE;
        for(int i = 0; distances.length > i; i++){
            for(int j = i + 1; distances.length > j; j++){
                if(distances[i][j] < min && !inCircuitTable[i][j]){
                    min = distances[i][j];
                    ret = new int[]{i,j};
                }
            }
        }
        return ret;
    }

    private static ArrayList<Edge> edgesFromDistances(ArrayList<Coordinate3D> cords, double[][] distances){
        var ret = new ArrayList<Edge>();
        for(int i = 0; distances.length > i; i++){
            for(int j = i + 1; distances.length >j; j++){
                ret.add(new Edge(cords.get(i),cords.get(j),distances[i][j]));
            }
        }
        return ret;
    }

    private static long productLastAdded(ArrayList<Edge> edges, int n){
        edges.sort((x,y) -> x.getWeight() > y.getWeight() ? 1: -1);
        Set<Coordinate3D> endpoints = new HashSet<Coordinate3D>();
        Edge prev = edges.get(0);
        for(var edge: edges){
            if (endpoints.size() == n) break;
            if(endpoints.contains(edge.getStart()) && endpoints.contains(edge.getEnd())) continue;
            prev = edge;
            endpoints.add(edge.getEnd());
            endpoints.add(edge.getStart());
        }
        return prev.getEnd().getX() * prev.getStart().getX();
    }

    private static List<Integer> nLargestComponents(boolean[][] adj, int n) {
        int len = adj.length;
        boolean[] visited = new boolean[len];
        List<Integer> sizes = new ArrayList<>();

        for (int i = 0; i < len; i++) {
            if (!visited[i]) {
                int size = bfsComponentSize(adj, visited, i);
                sizes.add(size);
            }
        }
        sizes.sort(Collections.reverseOrder());
        return sizes.subList(0, Math.min(n, sizes.size()));
    }

    private static int bfsComponentSize(boolean[][] adj, boolean[] visited, int start) {
        Queue<Integer> queue = new LinkedList<>();
        queue.add(start);
        int size = 0;
        while (!queue.isEmpty()) {
            int node = queue.poll();
            if (visited[node]) continue;
            visited[node] = true;
            size++;
            for (int neigh = 0; neigh < adj.length; neigh++) {
                if (adj[node][neigh] && !visited[neigh]) {
                    queue.add(neigh);
                }
            }
        }
        return size;
    }

    public static void main(String[] args) throws FileNotFoundException {
        var coordinates = fromFile("input.txt");
        var distanceTable = new double[coordinates.size()][coordinates.size()];
        var inCircuitTable = new boolean[coordinates.size()][coordinates.size()];
        for(int i = 0; coordinates.size() > i;i++){
            for(int j = 0; coordinates.size() > j; j++){
                distanceTable[i][j] = coordinates.get(i).distanceFrom(coordinates.get(j));
                inCircuitTable[i][j] = false;
            }
        }
        //part one
        for(int i = 0; 1000 > i; i++){
            var foundClosest = getTwoClosestIndex(distanceTable,inCircuitTable);
            inCircuitTable[foundClosest[0]][foundClosest[1]] = true;
            inCircuitTable[foundClosest[1]][foundClosest[0]] = true;
        }
        var largest = nLargestComponents(inCircuitTable,3);
        long sum = 1;
        for(var num: largest){
            sum *= num;
        }
        System.out.println(sum);
        // part two
        var toEdges = edgesFromDistances(coordinates,distanceTable);
        System.out.println(productLastAdded(toEdges,coordinates.size()));
    }
}
