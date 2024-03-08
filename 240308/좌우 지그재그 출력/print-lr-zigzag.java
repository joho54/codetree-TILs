import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        // 여기에 코드를 작성해주세요.
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int cnt = 1;
        for (int i = 1; i <= n*n; i+=n){
            if (cnt%2==1){
                for (int j = i; j < i+n; j++) {
                    System.out.print(j + " ");
                }
            }
            else {
                for (int j = i+n-1; j >= i; j--) {
                    System.out.print(j + " ");
                }
            }
            cnt++;
            System.out.println("");
        }
    }
}