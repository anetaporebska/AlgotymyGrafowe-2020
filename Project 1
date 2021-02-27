#include <iostream>
#include <climits>

using namespace std;

int INF_val = INT_MAX;

void bellman_ford(int ** capacity, int ** cost, int n, int * dist, int *parent, int s) {
    for (int i = 0; i < n; i++) {
        dist[i] = INF_val;
        parent[i] = -1;
    }
    dist[s] = 0;


    for (int i = 0; i < n - 1; i++) {
        bool stop = true;
        for (int j = 0; j < n; j++) {
            for (int k = 0; k < n; k++) {
                if (capacity[j][k] != 0 && dist[k] > dist[j] + cost[j][k] && dist[j]!=INF_val) {
                    dist[k] = dist[j] + cost[j][k];
                    parent[k] = j;
                    stop = false;
                }

            }
        }
        if (stop){
            break;
        }

    }


}

// minimum-cost flow problem
// for a given value K, we have to find a flow of this quantity, and among all flows of this quantity we have
// to choose the flow with the lowest cost


//void dijkstra(int ** capacity, int ** cost, int n, int * dist, int *parent, int s){
    //
//}


// K to jest liczba meczy, dokładnie tyle chcemy mieć przeplywu
int min_cost(int **capacity, int **cost, int n, int s, int t, int K){



    // At each iteration of the algorithm we find the shortest path in the residual graph from s to t
    // We look for the shortest path in terms of the cost of the path
    // if the path was found, we increase the flow by it: we find the minimal residual capacity of the path
    // and reduce the back edges by the same amount
    // if there doesn't exist a path anymore, then the algorithm terminates

    // if at some point the flow reaches the value K, then we stop the algorithm


    int F = 0;   //reached flow
    int C = 0;   //actual cost

    int dist[n]; //for Bellman-Ford algorithm
    int parent[n];


    bellman_ford(capacity,cost, n, dist, parent, s);
    while(dist[t]!=INF_val){

        int f = INF_val;
        int curr = t;
        while (curr!=s){
            f = min(f,capacity[parent[curr]][curr]);
            curr = parent [curr];
        }

        // apply flow
        F += f;
        //C += f*dist[t];
        curr = t;
        while (curr!=s){
            capacity[parent[curr]][curr] -=f;
            capacity[curr][parent[curr]] +=f;
            C+= f*cost[parent[curr]][curr];
            curr = parent[curr];
        }
        bellman_ford(capacity,cost, n, dist, parent, s);
    }

    if(F==K) return C;
    return INF_val;



}

int game_index(int a, int b, int N){
    if(a<b){
        int idx = b-a;
        for (int i=1; i<=a; i++){
            idx+=(N-i);
        }
        return idx;
    }
    else{
        int idx =a-b;
        for (int i=1; i<=b; i++){
            idx+=(N-i);
        }
        return idx;
    }
}



int func(int x, int **G, int N){

    // number of vertices = number of games + number of players + s + 2 x t
    int games = N*(N-1)/2;
    int n = games +N + 3;
    int s = 0;
    int t1 = n-2;
    int t2 = n-1;

    int ** capacity = new int*[n];
    for (int j=0; j<n; j++) {
        capacity[j] = new int[n];
        for (int i=0; i<n; i++){
            capacity[j][i] = 0;
        }
    }


    // cost per unit of flow
    int ** cost = new int*[n];
    for (int j=0; j<n; j++) {
        cost[j] = new int[n];
        for (int i=0; i<n; i++){
            cost[j][i] = 0;
        }
    }

    int first_game = 1;
    int king_index = first_game+games;

    // muszę wiedzieć pod jakim indeksem występuje dana gra -> game_index


    // łączę każdą grę z graczami, którzy mogą ją wygrać
    for (int i=0; i<N; i++){
        for (int j=0; j<N; j++){

            if (G[i][j]!=-1){

                int idx = game_index(i,j, N);
                int winner_idx = king_index+j;
                int loser_idx = king_index+i;
                // każdą grę może wygrać jeden z nich, loser jeśli zapłacimy
                capacity[idx][winner_idx] = 1;
                capacity[idx][loser_idx] = 1;
                cost[idx][winner_idx] = 0;
                cost[idx][loser_idx] = G[i][j];
                cost[loser_idx][idx] = -G[i][j]; //////////////////////////////////


            }



        }
    }
    // łączę źródło s z każdą grą
    for (int i=1; i<king_index; i++){
        capacity[s][i] = 1;
        cost[s][i]=0;
    }
    // łączę każdego gracza (oprócz króla) z t1
    for(int i=king_index+1; i<t1; i++){
        capacity[i][t1]=x;
        cost[i][t1]=0;
    }
    // łączę króla z t2
    capacity[king_index][t2] = x;
    cost[king_index][t2]=0;


    // łączę t1 z t2
    capacity[t1][t2] = games - x;
    cost[t1][t2] = 0;


    return min_cost(capacity, cost, n, s, t2, games);




}



void kings_game(int **G, int n, int B){
    int min_cost = INF_val;

    // total number of wins that king can achieve without restoring to bribery
    int t =0;
    for (int i=0; i<n; i++){
        if(G[i][0]!=-1){
            t+=1;
        }
    }
    for(int i=0; i<n-t; i++){
        int x = t+i;
        // cout<<"x: "<<x<<endl;
        min_cost=min(min_cost, func(x,G,n));
        if(min_cost<=B){
            cout<<"TAK"<<endl;
            return;
        }

    }
    cout<<"NIE"<<endl;

}





int main() {


    int tests;
    cin>>tests;

    for(int i=0; i<tests; i++){
        int B;
        int n;
        cin>>B>>n;
        int x;
        int y;
        int w;
        int b;

        int ** G = new int*[n];
        for (int j=0; j<n; j++){
            G[j] = new int [n];
            for (int k=0; k<n; k++){
                G[j][k] = -1;
            }

        }

        for (int j=0; j<n*(n-1)/2; j++){
            cin>>x>>y>>w>>b;
            if (w==x) G[y][w]=b;
            else G[x][w]=b;

        }

        if (n==1){
            cout<<"TAK"<<endl;
        }
        else kings_game(G,n,B);
    }






    return 0;
}
