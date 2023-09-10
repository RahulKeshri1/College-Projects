#include<iostream>
#include<conio.h>

using namespace std;

int main()
{
    intarr[3][3];
    int i,j,first,second;

    cout<<"Enter the distance ";
    for(i=0;i<3;i++)
    {
        for(j=0;j<3;j++)
        {
            cin>>arr[i][j];
        }
    }

    cout<<"Enter the first point\t";
    cin>>first;
    cout<<"Enter the second point\t";
    cin>>second;

    cout<<"Cost of the distance travelling\t"<<arr[first][second];
    getch();
    return 0;
}