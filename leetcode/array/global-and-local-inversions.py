bool isIdealPermutation(int* A, int ASize){
    // size_t n = sizeof(A)/sizeof(int);
    bool inv = false;
    for(int i = 0; i < ASize; i++) {
        if(inv) {
            inv = false;
            if(A[i] != i - 1)
                return false;
        }
        else {
            if(A[i] == i + 1)
                inv = true;
            else if(A[i] != i)
                return false;
        }
    }
    return true;
}
