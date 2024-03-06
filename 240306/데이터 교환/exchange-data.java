public class Main {
    public static void main(String[] args) {
        // 여기에 코드를 작성해주세요.
        int a, b, c;
        a = 5;
        b = 6;
        c = 7;
        int tmp1, tmp2;
        tmp1 = b;
        tmp2 = c;
        b = a;
        c = tmp1;
        a = tmp2;
        System.out.println(a);
        System.out.println(b);
        System.out.println(c);

    }
}