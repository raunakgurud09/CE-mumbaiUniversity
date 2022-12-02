#include <iostream>
using namespace std;

void insertionSort(int arr[], int n)
{
    int i,j,key;
    for( i = 1 ;i<n;i++){
        key = arr[i];
        j = i-1;
        while( j >=0 && arr[j]>key){
            arr[j+1] = arr[j];
            j--;
        }
        arr[j+1] = key;
    }
}

void printArray(int arr[],int n){
    for(int i=0;i<n;i++){
        cout<<arr[i]<<" ";
    }
    cout<<endl;
}

int main()
{

    int arr[]= {13,11,14,5,6};
    int n = sizeof(arr)/sizeof(arr[0]);

    insertionSort(arr,n);
    printArray(arr,n);



    return 0;
}