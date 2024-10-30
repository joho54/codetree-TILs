import java.util.TreeSet;
import java.util.Scanner;
import java.util.Iterator;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        TreeSet<Integer> s = new TreeSet<>();
        s.add(0);
        int n = sc.nextInt();
        int ans = Integer.MAX_VALUE;
        for(int i = 0; i < n; i++){
            
            int val = sc.nextInt();
            
            s.add(val);

            Integer higher = s.higher(val);
            Integer lower = s.lower(val);
            
            // update ans
            if (higher != null) {
                int sub1 = higher - val;
                if (sub1 < ans) ans = sub1;
            }
                
            if (lower != null) {
                int sub2 = val - lower;
                if (sub2 < ans) ans = sub2;
            }

            System.out.println(ans);
        }

        




    }
}