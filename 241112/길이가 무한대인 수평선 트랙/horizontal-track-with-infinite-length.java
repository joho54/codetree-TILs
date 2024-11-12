import java.util.Scanner;
import java.util.TreeSet;

class Runner implements Comparable<Runner>{
    int speed, place;
    public Runner(int speed, int place){
        this.speed = speed;
        this.place = place;
    }

    @Override
    public int compareTo(Runner other){
        if(this.place != other.place) return this.place - other.place;
        else return this.speed - other.speed;
    }
}



public class Main {
    public static void main(String[] args) {
        // Scanner sc = new Scanner(System.in);
        TreeSet<Runner> s = new TreeSet<>();
        TreeSet<Runner> new_s = new TreeSet<>();

        int N = sc.nextInt();
        int T = sc.nextInt();
        for(int i = 0; i < N; i++){
            int place = sc.nextInt();
            int speed = sc.nextInt();
            Runner runner = new Runner(speed, place);
            s.add(runner);
            // System.out.println(runner.speed + " " + runner.place);
        }
        // iterate by time
        for(int t = 0; t < T; t++){
            // System.out.println("-----------");
            while(!s.isEmpty()) // how can i remove?
            {
                // get every same place runners
                Runner runner1 = s.first();
                s.remove(runner1);
                if(s.isEmpty()){
                    new_s.add(runner1);
                    continue;
                }
                int std_place = runner1.place;
                Runner runner2 = s.first();
                int min_speed = runner1.speed;
                if(std_place == runner2.place)
                {
                    while(std_place == runner2.place){
                        // System.out.println("same same");
                        // System.out.println("place: " + runner1.place + " place:" + runner2.place);
                        // update
                        s.remove(runner2);
                        if(s.isEmpty()) break;
                        min_speed = Math.min(min_speed, runner2.speed);
                        runner2 = s.first();
                    }
                    int new_place = std_place + min_speed;
                    // System.out.println("merged speed:" + min_speed + " place:" + new_place);
                    new_s.add(new Runner(min_speed, new_place));
                }


                else{ // forget the runner2
                    // update runner1 place.
                    runner1.place = runner1.place + runner1.speed; 
                    new_s.add(runner1);
                    // System.out.println("appended directly place:" + runner1.place + " speed:" + runner1.speed);
                }
            }
            // switch new_s with s
            s = new_s;
            new_s = new TreeSet<>();

        }

        System.out.println(s.size());
    }
}

// 속력 = 거리/시간
// T분일 때 사람의 위치 = 달리기 시작한 위치 + 이동 거리
// 이동 거리 = 1/속력 * 시간(최대 T)

// 문제풀이 초안
// 일단 시간마다 이터레이션은 너무 큼. 근데 이게 생각나는 방법이긴 함.
// 자 이걸 한다 치면, 아마 복잡도는 높은 확률로 O(N^2)임.
// 이걸 줄이기 위해서는? 
// 시간 복잡도 O(N^2)(정확히는 O(N*T))의 풀이에서 할 것: 
// 각 이터레이션에서 할 것 = 현재 선수들의 위치 계산, 만나면 그룹으로 만들기. 
// 목표는 O(N LogT) 정도? 혹은 O(TlogN)
// 근데 T는 어쩔수 없는 거 같은데. 일단 O(T log N)으로 간다면? 
// 각 사람의 위치 정보를 트리셋으로 저장, 어차피 같은 값은 같은 그룹으로 치면 되기 때문에// 그냥 동일 값 생각할 필요 없음.
// 1. 위치 정보가 같은 값들을 모두 꺼낸다. 최댓값을 구할수는 있는데 같은지는 어떻게 알지?
// 1-1. 사람 정보를 (위치, 속도)로 생각했을 때, 뭐라고 해야 할까?
// 일단 복잡도 큰 방법: 위치 정보로 줄 세우고, 위치 정보가 달라질 때까지 꺼내고 삭제해서, 최저 속도값 구해서
// 새로 사람 생성해서 집어넣기.
// ㅇㅇ 이러면 풀수는 있음. 근데 트리의 자동 정렬 기능을 적극 활용할 수가 없음.
// 위치에 대해서만 트리를 따로 만들어서, 뽑아서, 그 위치인 모든 노드를 뽑는 방법은 없나?
// 위치 트리랑 속도 트리를 따로 만들어서 이터레이션? 복잡도는? O(N^2)이하. 
// 값의 특성을 활용해서 트리를 만드는 방법은?
// 트리의 정의: (각자의 위치, 위치, 위치) - (위치, 위치 위치) T에서의 위치
// 로그 트리가 있다 치면,
// (속도1, 위치1) , (속도2, 위치2) -> (최저속도, 다음 위치) 이거 하는데 logn인가? ㄴㄴ 갈수록
// 계산이 줄어들긴 하지만...아 갈수록 줄어들면 logn 맞지 않음?
// n -> n//2 -> n//2^2 ...이러면. 그러면 Tlogn이 맞긴 한데.
// 이때 위치 1을 비교 위치로 놓고, 다음에 꺼내서 삭제한 노드의 위치 값이 다르면 비교 위치를 갱신
// 이러면 한번의 이터레이션에 대해서 n이 소요되는데? 이거를 t 번 반복하면 가뿐히 n^2이 걸림.
// 연산 자체에 계산을 녹여내는 방법은 없나? 그럼 자료를 다시 만들어야지.
// 위치를 기준으로 다 저장해버리면, 위치1, 위치2, 위치3...위치n 이 생기겠지.
// 위치1이 아닐떄까지 꺼내서, 새 값 집어넣고, 이것도 시간은 오지게 걸림. 
// 아 nlogn 노래를 불러도 잘 모르겠네. 
// 2. 속도 정보가 가장 낮은 값과 위치 정보를 통해 새로운 사람을 생성
// 