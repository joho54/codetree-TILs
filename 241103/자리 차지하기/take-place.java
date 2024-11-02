import java.util.TreeSet;
import java.util.Scanner;

public class Main {
    public static TreeSet<Integer> e = new TreeSet<>();
    public static Scanner sc = new Scanner(System.in);
    public static int n = sc.nextInt();
    public static int m = sc.nextInt();
    public static int[] a = new int[n];

    public static void main(String[] args) {
        for(int i = 0; i < n; i++){
            a[i] = sc.nextInt();
        }
        for (int i = 1; i < m+1; i++){
            e.add(i);
        }

        for(int a_i: a){
            if(e.floor(a_i) != null) {
                e.remove(e.floor(a_i));
            }
            else{
                break;
            }
        }
        System.out.println(m-e.size());
    }
}