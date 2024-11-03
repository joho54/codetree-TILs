import java.util.Scanner;

class Mission{
    String code;
    String place;
    int time;
    public Mission(String code, String place, int time){
        this.code = code;
        this.place = place;
        this.time = time;
    }
}


public class Main {
    public static void main(String[] args) {
        // 여기에 코드를 작성해주세요.
        Scanner sc = new Scanner(System.in);
        String code = sc.next();
        String place = sc.next();
        int time = sc.nextInt();
        Mission mission = new Mission(code, place, time);
        System.out.println("secret code : " + mission.code);
        System.out.println("meeting point : " + mission.place);
        System.out.println("time : " + mission.time);

    }
}