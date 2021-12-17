
#include <iostream>

using namespace std; 


bool model_trajectory(int vx, int vy){

    int currx = 0; 
    int curry = 0; 
    int highest = -1; 

    while(true){
        currx += vx; 
        curry += vy; 

        if(vx < 0){
            vx += 1; 
        }
        else if (vx > 0){
            vx -= 1; 
        }
        else{
            vx = 0; 
        }

        vy -=1; 

        if(currx >= 236 && currx <= 262 && curry >= -78 && curry <= -58){
            return true; 
        }

        if(curry < -78 && vy < 0){
            return false; 
        }

    }
}

int main(){
    int count = 0 ; 
    for(int i=0; i < 300; i++){
        for(int j=-2000; j < 2000; j++){

            bool res = model_trajectory(i, j); 

            if(res == true){
                count += 1; 
            }

        }
    }

    cout << count << endl; 
}