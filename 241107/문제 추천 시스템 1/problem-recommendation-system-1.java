// Problem.idx, Problem.level
// comparator: level -> idx
// x=1, get proSet.last()
// x=-1 get proSet.first()
// ad P L ,, proSet.put(new Problem(P, L))
// sv P L proSet.remove(target)

import java.util.TreeSet;
import java.util.Scanner;

class Pro implements Comparable<Pro>{
    int idx;
    int level;

    public Pro(int idx, int level){
        this.idx = idx;
        this.level = level;
    }

    @Override
    public int compareTo(Pro pro){
        // if level is differ
        if(this.level != pro.level){
            return this.level - pro.level;
        }
        else{
            return this.idx - pro.idx;
        }
    }
}

public class Main {

    public static Scanner sc = new Scanner(System.in);
    public static TreeSet<Pro> s = new TreeSet<>();
    public static void main(String[] args) {
        int n = sc.nextInt();
        for(int i = 0; i < n; i++){
            int P = sc.nextInt();
            int L = sc.nextInt();//level
            s.add(new Pro(P, L));
        }
        int m = sc.nextInt();
        for(int i = 0; i < n; i++){
            String o = sc.next();
            if(o.equals("ad")){
                // add pro
                int P = sc.nextInt();
                int L = sc.nextInt();
                Pro target = new Pro(P, L);
                s.add(target);
            }
            else if(o.equals("sv")){
                // remove pro
                int P = sc.nextInt();
                int L = sc.nextInt();
                Pro target = new Pro(P, L);
                s.remove(target);
            }
            else if(o.equals("rc")){
                // -1 or 1
                int j = sc.nextInt();

                if(j == 1){
                    Pro target = s.last();
                    System.out.println(target.idx);
                }
                else if(j == -1){
                    Pro target = s.first();    
                    System.out.println(target.idx);
                }
            }
        }
    }
}