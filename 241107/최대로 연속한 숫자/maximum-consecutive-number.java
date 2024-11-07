// how can i get longest consequantial numbrs, lcn, by treeset?
// add treeset, orders ascendingily. 
// how about removal?
// length.
// 1. i can call s.higher(curr_i) and compare it and set max legnth.
// 2. don't know..
// O(nm)
// 1 2 3 5
// or put deleted nubmers in another set.
// 4 6 
// then? compare
// smallest = s.first() 
// largest = s.last()
// curr_num = s.first()
// legnth = initiated
// next_num = s.higher(curr_num)
// compare: next_num - curr_num = 4-1, (1, 2, 3)
// while(next_num != largest())

// m= numbers2del
// 1, 2, 3,4 ,5
// del 2
// 1 3 4 5

import java.util.Scanner;
import java.util.TreeSet;

public class Main {

    public static Scanner sc = new Scanner(System.in);
    public static TreeSet<Integer> s = new TreeSet<>();
    public static void main(String[] args) {
        int n = sc.nextInt();
        int m = sc.nextInt();
        s.add(n+1);
        s.add(-1);
        int ans = -1;// where should i init backup?
        int backup = -1;
        for(int j = 0 ; j < m; j++){ // what? /
            int del_num = sc.nextInt();
            s.add(del_num);
            // compoare
            int tmp1 = del_num - s.lower(del_num) - 1;
            int tmp2 = s.higher(del_num) - del_num - 1 ;
            // 0 1 2 3 4 5 6 7 8
            // 0 1 2   4 5 6 7 8 
            // 0 1 2   4 5   7 8
            int tmp = Math.max(tmp1, tmp2); // first compare occurs here
            tmp = Math.max(tmp, backup);
            System.out.println(tmp);

            backup = Math.min(tmp1, tmp2);
        }

    }
}