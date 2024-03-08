import java.util.Scanner;

class IntWrapper{
    int value;
    public IntWrapper(int value){
        this.value = value;
    }
}


public class Main {
    public static void modify(IntWrapper n, IntWrapper m){
        int tmp = n.value;
        n.value = m.value;
        m.value = tmp;
    }
    public static void main(String[] args) {
        // 여기에 코드를 작성해주세요.  
        Scanner sc = new Scanner(System.in);
        int tmpn = sc.nextInt();
        int tmpm = sc.nextInt();
        IntWrapper n = new IntWrapper(tmpn);
        IntWrapper m = new IntWrapper(tmpm);
        modify(n,m);
        System.out.println(n.value + " " + m.value);
        
    }
}