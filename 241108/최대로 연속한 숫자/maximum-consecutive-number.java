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

class Range implements Comparable<Range>{
    int start_num, end_num;
    int range_size;

    public Range(int start_num, int end_num){
        this.start_num = start_num;
        this.end_num = end_num;    
        this.range_size = end_num - start_num + 1; // think about offset
    }
    @Override
    public int compareTo(Range range){
        if(this.range_size != range.range_size) return range.range_size - this.range_size; // reversed order
        else return 0;
    }

}

public class Main {

    public static Scanner sc = new Scanner(System.in);
    public static TreeSet<Range> s = new TreeSet<>();
    public static void main(String[] args) {
        int n = sc.nextInt();
        int m = sc.nextInt();
        s.add(new Range(0, n));
        for(int j = 0 ; j < m; j++){
            int del_num = sc.nextInt();
            // we suppose del_num is always targeting head
            // if m is amoung head this is ok. but if not?
            Range head = s.first();// while?
            while(head.start_num > del_num || head.end_num < del_num){
                head = s.higher(head);
                // System.out.println("where are you~");
            }
            s.remove(head);
            Range r1 = new Range(head.start_num, del_num-1);
            Range r2 = new Range(del_num+1, head.end_num);
            s.add(r1);
            s.add(r2);
            System.out.println(s.first().range_size);
        }
    }
}