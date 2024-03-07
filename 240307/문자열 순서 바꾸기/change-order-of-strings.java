import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        // 여기에 코드를 작성해주세요.
        Scanner sc = new Scanner(System.in);
        String s = sc.next();
        String t = sc.next();
        String tmp = s;
        s = t;
        t = tmp;

        System.out.println(s);
        System.out.println(t);
    }
}