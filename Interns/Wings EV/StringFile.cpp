//#include <iostream>

#include <stdio.h>
#include <iterator>
#include <map>
#include <bits/stdc++.h>

using namespace std;

void insert(map<string, string> &fileMap, map<string, string> &timeMap, string, string);
void play(map<string, string> &fileMap, map<string, string> &timeMap);

std::string timeNow()
{
    std::time_t curr = std::time(nullptr);
    char cstr[128] ;

    std::strftime( cstr, sizeof(cstr), "%Y%m%d%H%M%S", std::localtime(&curr) ) ;

    return cstr ;
}

int main()
{   int data;
    int n = 5;
    
        // empty set container
    map<string, string> fileName2timeStamp;
    map<string, string> timeStamp2fileName;
    
    for (int i=0; i < n; i++){
        //cin >> data;
        scanf("%d", &data);
        
        switch (data)  {
        case 1:
            insert(fileName2timeStamp, timeStamp2fileName, "SpeechFile1.wav", timeNow());
            break;

        case 2:
            insert(fileName2timeStamp, timeStamp2fileName, "SpeechFile2.wav", timeNow());
            break;
    
        case 3:
            insert(fileName2timeStamp, timeStamp2fileName, "SpeechFile3.wav", timeNow());
            break;
    
        case 4:
            insert(fileName2timeStamp, timeStamp2fileName, "SpeechFile4.wav", timeNow());
            break;    

        case 5:
            insert(fileName2timeStamp, timeStamp2fileName, "SpeechFile5.wav", timeNow());
            break;
    
        case 6:
            insert(fileName2timeStamp, timeStamp2fileName, "SpeechFile6.wav", timeNow());
            break;
            
        case 7:
            insert(fileName2timeStamp, timeStamp2fileName, "SpeechFile7.wav", timeNow());
            break;
            
        case 8:
            insert(fileName2timeStamp, timeStamp2fileName, "SpeechFile8.wav", timeNow());
            break;
    
        default:
            break;
        }

    }
    
    play(fileName2timeStamp, timeStamp2fileName);
    return 0;
}


    
void insert(map<string, string> &fileMap, map<string, string> &timeMap, string fileName, string timeStamp){
    
    if (fileMap.find(fileName) == fileMap.end()){
        fileMap.insert(pair<string, string>(fileName, timeStamp));
        timeMap.insert(pair<string, string>(timeStamp, fileName));
    }
}

void play(map<string, string> &fileMap, map<string, string> &timeMap){
    
    map<string, string>::iterator itr;

    for (itr = timeMap.begin(); itr != timeMap.end(); ++itr) {
        printf("%s\n", itr->second.c_str());
        //cout << itr->second << '\n';
    }
    cout << endl;
    
    for (itr = timeMap.begin(); itr != timeMap.end(); ++itr) {
        fileMap.erase(itr->second);
        timeMap.erase(itr->first);
    }

}












