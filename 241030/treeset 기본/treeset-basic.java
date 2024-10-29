import java.util.Scanner;
import java.util.TreeSet;

public class Main {    
    // 변수 선언
    public static int n;
    public static TreeSet<Integer> s = new TreeSet<>();

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        // 입력:
        n = sc.nextInt();

        for(int i = 0; i < n; i++) {
            String command = sc.next();
            int x;

            if(command.equals("add")) {
                x = sc.nextInt();
                s.add(x);
            }
            else if(command.equals("remove")) {
                x = sc.nextInt();
                s.remove(x);
            }
            else if(command.equals("find")) {
                x = sc.nextInt();
                if(s.contains(x))
                    System.out.println("true");
                else
                    System.out.println("false");
            }
            else if(command.equals("lower_bound")) {
                x = sc.nextInt();
                if(s.ceiling(x) != null)
                    System.out.println(s.ceiling(x));
                else
                    System.out.println("None");
            }
            else if(command.equals("upper_bound")) {
                x = sc.nextInt();
                 if(s.higher(x) != null)
                    System.out.println(s.higher(x));
                else
                    System.out.println("None");
            }
            else if(command.equals("largest")) {
                if(!s.isEmpty())
                    System.out.println(s.last());
                else
                    System.out.println("None");
            }
            else {
                if(!s.isEmpty())
                    System.out.println(s.first());
                else
                    System.out.println("None");
            }
        }
    }
}