import java.util.TreeSet;
import java.util.Scanner;

public class Main {
    public static final int MAX_INT = Integer.MAX_VALUE;
    public static int ptr_val = MAX_INT;
    public static Scanner sc = new Scanner(System.in);
    public static TreeSet<Integer> s = new TreeSet<>();
    public static void main(String[] args) {
        int n = sc.nextInt();
        int k = sc.nextInt();

        for(int i = 0; i < n; i++){
            s.add(sc.nextInt());
        }
        for(int i = 0; i < k; i++){
            System.out.print(s.lower(ptr_val) + " ");
            ptr_val = s.lower(ptr_val);
        }
    }
}