import java.util.TreeSet;
import java.util.Scanner;
import java.util.Iterator;

public class Main {

    public static Scanner sc = new Scanner(System.in);
    public static TreeSet<Integer> s = new TreeSet<>();
    public static TreeSet<Integer> t = new TreeSet<>();
    public static int n = sc.nextInt();
    public static int m = sc.nextInt();
    public static final int MAX_INT = Integer.MAX_VALUE;
    public static int ans = MAX_INT;

    
    public static void main(String[] args) {
        // 여기에 코드를 작성해주세요.
        for(int i = 0; i < n; i++){
            s.add(sc.nextInt()); 
        }

        for (int x: s){
            // celing and floor each
            // x+m
            if (s.ceiling(x+m) != null){
                // update
                ans = Math.min(s.ceiling(x+m)-x, ans);
            }

            if (s.floor(x-m) != null){
                ans = Math.min(x - s.floor(x-m), ans);
            }
        }

        if(ans == MAX_INT) System.out.println(-1);
        else System.out.println(ans);
    }
}