//i ce biti counter, pocinje od 0
@i
M = 0

(LOOP_START)
    //odi na adresu "i" i spremi vrijednost u D
    @i
    A = M
    D = M

    //odi na adresu "max" i spremi vrijednost u nju
    @max
    M = D
    
        (INNER_LOOP)
        //uzmi vrijednost iz i
        @i
        D = M

        //4 - i
        @4
        D = A - D
    
    // check je li dosao na kraj
    @LOOP_END
    D; JLE
    
    //dohvati max 
    @max
    D = M
    
    //povecaj counter, odi na iducu adresu i provjeri koji je veci (M - D, ukoliko je negativan broj, znamo da je drugi veci)
    @i
    M = M + 1
    A = M
    D = M - D
    
    // value - max > 0
    @LOOP_START
    D; JGT
    
    @INNER_LOOP
    0; JMP
    
(LOOP_END)

//dohvati max i upisi u R5
@max
D = M

@5
M = D

(END)
@END
0; JMP