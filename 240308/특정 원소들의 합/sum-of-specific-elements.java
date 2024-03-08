import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        // 여기에 코드를 작성해주세요.
        Scanner sc = new Scanner(System.in);
        int[][] arr = new int[4][4];
        int ans = 0;
        for(int i = 0; i<4; i++){
            for(int j = 0; j<4; j++){
                arr[i][j] = sc.nextInt();
                if(i>=j){
                    ans += arr[i][j];
                }
            }
        }
        System.out.println(ans);
    }
}