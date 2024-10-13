import java.util.TreeSet;
import java.util.Scanner;

public class Main {
    public static TreeSet<Integer> s = new TreeSet<>();
    public static void main(String[] args) {
        // 여기에 코드를 작성해주세요.
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int m = sc.nextInt();
        for(int i = 0; i < m; i++){
            s.add(i+1);
        }
        for(int i = 0; i < n; i++){
            s.remove(sc.nextInt());
            System.out.println(s.last());
        }
    }
}