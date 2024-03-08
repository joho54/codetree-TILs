import java.util.Scanner;

public class Main {
    public static void fillNumbers(int n){
        int[][] arr = new int[n][n];
        int val = 1;
        for (int i = 0; i <n; i++){
            for (int j = 0; j < n; j++){
                arr[i][j] = val;
                val++;
                if (val==10)
                    val = 1;
            }
        }
        for (int i = 0; i <n; i++){
            for (int j = 0; j < n; j++){
                System.out.print(arr[i][j] + " ");

            }
            System.out.println("");
        }
        
    }

    public static void main(String[] args) {
        // 여기에 코드를 작성해주세요.
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        fillNumbers(n);
    }
}