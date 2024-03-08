import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        // 여기에 코드를 작성해주세요.
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int[] arr = new int[n];
        for (int i = 0; i<n; i++){
            arr[i] = sc.nextInt();
        }
        final int MIN_INT = Integer.MAX_VALUE;
        int ans = MIN_INT;
        for (int i = 0; i<n; i++){
            for (int j = i+1; j<n; j++){
                if(Math.abs(arr[i]-arr[j]) < ans)
                    ans = Math.abs(arr[i]-arr[j]);
            }
        }
        System.out.println(ans);
    
    }
}