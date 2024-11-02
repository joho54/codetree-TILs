import java.util.TreeSet;
import java.util.Scanner;

public class Main {


    public static TreeSet<Integer> s = new TreeSet<>();
    public static TreeSet<Integer> e = new TreeSet<>();
    public static Scanner sc = new Scanner(System.in);
    public static int n = sc.nextInt();
    public static int m = sc.nextInt();
    public static int[] a = new int[n];
    public static int seatNum = 1;

    public static void main(String[] args) {
        for(int i = 0; i < n; i++){
            a[i] = sc.nextInt();
        }
        for (int i = 1; i < m+1; i++){
            e.add(i);
        }

        // 트리셋의 특징; 들어오는 숫자를 크기순으로 배열한다. 
        // 이 문제: 일단 배정을 순서대로 해주고, 의자 번호를 할당해주면 된다. 
        // 의자번호가 있다고 치고, 일단 먼저 풀고, 예외를 처리해보자. 

        for(int a_i: a){
            // a_i동일한 값이 없는 경우
            if(!s.contains(a_i)) {
                s.add(a_i);
                e.remove(a_i);
                }
            // a_i
            else //동일한 값이 있는데, 
            {
                //앞에 공간 있는 경우
                // i=6. 1 2 4 5 6 //  3 //빈 값이 뭔지 어떻게 알지?
                //      3   e.lower(6) = 3이 되겠지? 빈자리 트리셋을 관리하면 되지 않을까?
                // 빈자리 트리셋은 모든 add에 대해 역으로 제거.
                if(e.lower(a_i) != null){
                    int tmp = e.lower(a_i);
                    s.add(tmp);
                    e.remove(tmp);
                }

                //앞에 공간 없는 경우
                // i=6. 1 2 3 4 5 6 
                else{
                    // 종료 조건임.
                    System.out.println("no seat" + a_i);
                }

            }
        }
        System.out.println(s.size());

    }
}