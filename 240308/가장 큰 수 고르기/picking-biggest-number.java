import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        // 여기에 코드를 작성해주세요.
        Scanner sc = new Scanner(System.in);
        int[] arr = new int[10];
        int MAX_INT = Integer.MIN_VALUE;
        int ans = MAX_INT;
        // for (int i = 0; i<1)
        for (int i = 0; i <10; i++){
            arr[i] = sc.nextInt();
            if(arr[i]>ans){
                ans = arr[i];
            }
        }
        System.out.println(ans);
    }
}