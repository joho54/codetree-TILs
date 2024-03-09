import java.util.Scanner;

public class Main {
    public static boolean checkPelindrom(char[] charArray){
        int n = charArray.length;
        int i, j;
        i = 0;
        j = n-1;
        boolean isPelindrome = true;
        while(isPelindrome && i<n/2){
            if (charArray[i] != charArray[j])
                isPelindrome = false;
            i += 1;
            j -= 1;
        }
        return isPelindrome;
    }
    public static void main(String[] args) {
        // 여기에 코드를 작성해주세요.
        Scanner sc = new Scanner(System.in);
        String str = sc.next();
        System.out.println(str);
        char[] charArray = str.toCharArray();
        boolean isPelindrome = checkPelindrom(charArray);
        System.out.println(isPelindrome);
        
    }
}