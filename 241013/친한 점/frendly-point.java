import java.util.TreeSet;
import java.util.Scanner;

import java.util.TreeSet;

class Pair implements Comparable<Pair> {
    int x, y;

    public Pair(int x, int y) {
        this.x = x;
        this.y = y;
    }

    @Override
    public int compareTo(Pair p) {         
        if(this.x != p.x)
            return this.x - p.x;  
        else                      
            return this.y - p.y;  
    }
};

public class Main {
    public static void main(String[] args) {
        TreeSet<Pair> s = new TreeSet<>();  
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int m = sc.nextInt();
        
        for(int i = 0; i < n; i++){
            int x = sc.nextInt();
            int y = sc.nextInt();
            s.add(new Pair(x, y));

        }

        for(int i = 0; i < m; i++){
            int x = sc.nextInt();
            int y = sc.nextInt();
            Pair bestPoint = s.ceiling(new Pair(x, y));
            if(bestPoint != null)
                System.out.println(bestPoint.x + " " + bestPoint.y);
            else    
                System.out.println(-1 + " " + -1);

        }
    }
}