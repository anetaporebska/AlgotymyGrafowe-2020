#include <iostream>
#include <climits>
#include <queue>
#include<vector>

/*
 * 1. Find a perfect elimination ordering
 * 2. Form  a clique for each vertex v together with the neighbors of v that are later
 * than v in PEO.
 * 3. Test whether each of the resulting cliques is maximal.
 *
 * The largest maximal clique is a maximum clique, and, as chordal graphs are perfect,
 * the size of this clique equals the chromatic number of the chordal graph.
 * Chordal graphs are perfectly orderable: an optimal coloring may be obtained by applying
 * a greedy coloring algorithm to the vertices in the reverse of a perfect elimination ordering
 *
 *
 * TODO: linear lexBFS
 */


using namespace std;

int INF_val = INT_MAX;

void addEdge(vector<int> graph[], int x, int y){
    graph[x].push_back(y);
    graph[y].push_back(x);
}

bool containEdge(vector<int> graph[], int x, int y){
    for(auto it = graph[x].begin(); it!= graph[x].end(); ++it){
        if (*it == y){
            return true;
        }
    }
    return false;
}

bool empty(vector<int> arr[]){
    if (arr[0].empty() && arr[1].empty()){
        return true;
    }
    else return false;
}

vector<int> lexBFS(vector<int> graph[], int n){
    // array of vectors
    vector<vector<int>> arr;
    vector<int> set1;
    for(int i=0; i<n; i++){
        set1.push_back(i);
    }
    arr.push_back(set1);

    // visited vector
    vector<int> visited;

    while(!arr.empty()){
        int v = arr.back().back();
        arr.back().pop_back();
        if (arr.back().empty()){
            arr.pop_back();
        }
        visited.push_back(v);
        vector<vector<int>> new_arr;
        vector<int> current;
        vector<int> not_connected;
        vector<int> connected;
        for(auto i = arr.begin(); i != arr.end(); ++i){
            current=*i;

            for (auto j = current.begin(); j!= current.end(); ++j){
                int u = *j;
                if (containEdge(graph, v, u)){
                    connected.push_back(u);
                }
                else{
                    not_connected.push_back(u);
                }

            }
            if (!not_connected.empty()){
                new_arr.push_back(not_connected);
            }
            if (!connected.empty()){
                new_arr.push_back(connected);
            }

            connected.clear();
            not_connected.clear();

        }
        arr = new_arr;

    }
    return visited;

}

int solve(vector<int> graph[], int n){
    vector<int> visited = lexBFS(graph,n);
    // w visited mam PEO

    int color [n];

    for (int i=0; i<n; i++){
        color[i]=0;
    }
    int max_col = 0;
    for(auto it = visited.begin(); it!= visited.end(); ++it){
        int used [n]; // będę zaznaczać jakie kolory już były
        for (int i=0; i<n; i++){
            used[i]=0;
        }
        int v = *it;
        for (auto i = graph[v].begin(); i!= graph[v].end(); ++i) {
            int u = *i;
            used[color[u]]=1;
        }
        // szukam najmniejszego koloru, który nie występuje w zbiorze used
        int min_col;
        for (int i=1; i<n; i++){
            if(used[i]==0){
                min_col = i;
                break;
            }
        }
        color[v]=min_col;
        if (max_col<min_col){
            max_col=min_col;
        }

    }
    // jak graf to "sznurek" to odpowiedż to 2 a nie 1!!!


    return max_col-1;
}


int main() {


    int tests;
    cin>>tests;

    for(int i=0; i<tests; i++) {
        int n;
        int m;
        cin>>n>>m;
        vector<int> graph[n];
        int x;
        int y;
        for (int j=0; j<m; j++){
            cin>>x>>y;
            addEdge(graph, x-1,y-1);
        }
        if(m==n-1){
            cout<<2<<endl;
        }
        else{
            cout<<solve(graph,n)<<endl;
        }



    }


    return 0;
}
