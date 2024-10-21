import java.util.Scanner;

public class Main {

    public static int n, m;

    public static void main(String[] args) {
        // methods
        // input
        Scanner sc = new Scanner(System.in);

        n = sc.nextInt();
        m = sc.nextInt();
        int[] arr = new int[n];
        for(int i = 0; i < n; i++){
            arr[i] = sc.nextInt();
        }

        for(int i = 0; i < m; i++){
            int ans = sc.nextInt(); // get m numbers
            // System.out.println("Ans: " + ans);

            int left = 0, right = n - 1; // set pointers

            while (left <= right) { // basic condition for pointers
                int mid = (left + right) / 2; //
                if(arr[mid] == ans){ // found
                    System.out.println(mid+1);
                    break;
                }

                // modify pointers.
                if(arr[mid] < ans){ //if the arr[mid] is smaller then ans
                    // increase left
                    left = mid + 1;
                }
                else if (arr[mid] > ans){
                    right = mid - 1;
                }

                // we so sure when the pointer wraps here
                if (left > right){
                    System.out.println(-1);
                    break;
                }
                
            }


        }
    }
}