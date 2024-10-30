import java.util.TreeSet;
import java.util.Scanner;

public class Main {

    public static TreeSet<Integer> s = new TreeSet<>();
    public static Scanner sc = new Scanner(System.in);
    public static int n = sc.nextInt();
    public static int m = sc.nextInt();
    public static int[] a = new int[n];
    // public static int[] seats = new int[m+1];

    public static void main(String[] args) {
        // 규칙이 널널한 사람 나중에 앉히기
        // lower
        for(int i = 0; i < n; i++){
            a[i] = sc.nextInt();
            s.add(a[i]);
            // 1. 규칙이 작은 사람을 먼저 꺼낸다.
            // 2. 규칙이 작은 사람이 앉을 수 있는 최대한 작은 자리에 앉힌다.
        }
        int seat_cnt = 0;
        for(int a_i: s){
            
            if (seat_cnt > a_i) break;
            // seats[seat_cnt] = 1; // mark the seat.
            seat_cnt += 1;
        }
        System.out.println(seat_cnt);

    }
}