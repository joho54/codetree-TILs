import java.util.TreeSet;
import java.util.Scanner;
import java.util.Iterator;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        TreeSet<Integer> s = new TreeSet<>();
        s.add(0);
        int n = sc.nextInt();
        for(int i = 0; i < n; i++){
            s.add(sc.nextInt());
            int ans = 10000000;
            Iterator iter = s.iterator();
            while (iter.hasNext()){
                int val = (int)iter.next();
                Integer h = s.higher(val);
                if (h != null)
                {
                    int sub = h-val;
                    if (sub < ans) ans = sub;
                }
            }
            System.out.println(ans);
        }

        




    }
}