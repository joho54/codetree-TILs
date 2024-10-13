import java.util.TreeSet;
import java.util.Scanner;


public class Main {
    //vars
    public static int m, n;
    public static TreeSet<Integer> s = new TreeSet<>();
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        n = sc.nextInt();
        m = sc.nextInt();
        for(int i = 0; i < n; i++){
            s.add(sc.nextInt());
        }
        for(int i = 0; i < m; i++){
            int v = sc.nextInt();
            if(s.ceiling(v) == null){
                System.out.println(-1);
            }
            else{
                System.out.println(s.ceiling(v));
            }
        }


    }
}