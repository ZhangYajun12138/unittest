#coding:utf-8
def print_multiple_chart(n):
    for i in range(1,n):
        for j in range(1,i+1):
            # print(j,'*',i,'=',i*j,end=' ')
            print('%d*%d=%-2d'%(j,i,(i*j)),end=' ')#%-2d表示左对齐
        print('')
if __name__ == "__main__":
    print_multiple_chart(10)