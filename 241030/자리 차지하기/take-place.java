import java.util.TreeSet;
import java.util.Scanner;

public class Main {


    public static TreeSet<Integer> seats = new TreeSet<>();
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
            // 1. 규칙이 작은 사람을 먼저 꺼낸다.
            // 2. 규칙이 작은 사람이 앉을 수 있는 최대한 작은 자리에 앉힌다.
        }
        int seat_cnt = 0;
        for(int a_i: a){
            
            // if (seat_cnt > a_i) break;
            // seats[seat_cnt] = 1; // mark the seat.
            // queries 만들어서 값들을 순서대로 보면서 lower가 나랑 같으면 브레이크?

            if(seats.lower(a_i) != null){
                if(seats.lower(a_i) == a_i) break;
                }
            
            seat_cnt += 1; // 계산 자체는 맞는데.
            // seat treeset을 따로 만들어서 거기에다 a_i를 순서대로 집어넣고, 
            // queries를 따로 순서대로 돌면서 아니아니
            // 여기서 집어넣기 전에 a_i에 대해 lower 돌리고, 같으면 브레이크 걸면 되지..
            // System.out.println(a_i + " so " + seat_cnt);
            seats.add(a_i);
        }
        System.out.println(seat_cnt);

    }
}