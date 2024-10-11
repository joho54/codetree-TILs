import java.util.Scanner;
import java.util.TreeSet;

public class Main {

    // 변수 선언
    public static int n;
    public static void main(String[] args) {

        Scanner sc = new Scanner(System.in);
        // num of test data sets
        int T = sc.nextInt();
        
        // for each tests
        for(int i = 0; i < T; i++){
            // new tree set
            TreeSet<Integer> s = new TreeSet<>();

            int k = sc.nextInt();

            // for each instructions
            for(int j = 0; j < k; j++){
                String instruction = new String();

                instruction = sc.next();

                if (instruction.equals("I")){
                    int v = sc.nextInt();
                    s.add(v);
                } 

                else if(instruction.equals("D")){
                    int flag = sc.nextInt();
                    
                    // remove max
                    if(!s.isEmpty()){
                        if (flag == 1){
                            s.remove(s.last());
                        }
                        // remove min
                        else {
                            s.remove(s.first());

                        }
                    }
                }
            }
            if(s.isEmpty()) System.out.println("EMPTY");
            else{ 
                s.descendingSet().forEach(number -> System.out.print(number + " "));
                System.out.println();
            }

        }
        
    }
}