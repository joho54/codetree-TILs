// ceiling is key.

import java.util.TreeSet;
import java.util.Scanner;

class Point implements Comparable<Point>{
    
    int x, y;
    
    public Point(int x, int y){
        this.x = x;
        this.y = y;
    }

    @Override
    public int compareTo(Point p){
        if (this.x != p.x){
            return this.x - p.x;
        }
        else return this.y - p.y;
    }
}

public class Main{

    public static int MAX_N = 100000;

    public static void main(String[] args){

        Scanner sc = new Scanner(System.in);
        TreeSet<Point> s = new TreeSet<>();
        Point[] points = new Point[MAX_N];
        int n = sc.nextInt();
        int m = sc.nextInt();
        for (int i = 0; i < n; i++){
            int x = sc.nextInt();
            int y = sc.nextInt();
            points[i] = new Point(x, y);
            s.add(points[i]);
        }

        // 이제 트리셋에 순서대로 점들이 다 들어갔고, 다음으로 할 일은?
        // 명령 k를 받아서, 점들을 제거하면 됨.
        for (int i = 0; i < m; i++){
            int k = sc.nextInt();
            // 제거를 하면 됨
            Point target = s.ceiling(new Point(k, 0));
            if (target == null){
                System.out.println("-1 -1");
            }
            else{
                System.out.println(target.x + " " + target.y);
                s.remove(target);
            }
            
            
        }


    }

}