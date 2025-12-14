split_middle(String, Left, Right) :-
    string_length(String, Len),
    0 is Len mod 2,
    Half is Len // 2,
    sub_string(String, 0, Half, _, Left),
    sub_string(String, Half, Half, 0, Right).

list_digits(Int, Digits) :-
    list_digits_aux(Int, [], Digits).
list_digits_aux(Int, Digits, [Int|Digits]) :- Int < 10.
list_digits_aux(Int, Digits, Acc) :-
    NextInt is Int div 10,
    NextInt > 0,
    D is Int rem 10,
    list_digits_aux(NextInt, [D|Digits], Acc).

collect_same_halves([S-E | T],O) :-
    collect_same_halves(T,O);
    between(S,E,O),
    number_string(O,STR),
    split_middle(STR, L, R),
    L = R.

sum_same_halves(Ranges, Sum) :-
	findall(O, collect_same_halves(Ranges, O), Nums),
    sum_list(Nums, Sum).

repeated_n_times([], _, 0).
repeated_n_times(Big, Small, N) :-
    N > 0,
    append(Small, Rest, Big),
    N1 is N - 1,
    repeated_n_times(Rest, Small, N1).

collect_same_nths([S-E | T], O) :-
    collect_same_nths(T,O);
    between(S,E,O),
    list_digits(O,Os),
    append(A1,_,Os),
    length(A1,L1),
    length(Os,L2),
    L1 > 0,
    L2 > L1,
    N is L2 / L1,
    repeated_n_times(Os,A1,N),
    N > 1.
   
sum_same_nths(Ranges, Sum) :-
    findall(O,collect_same_nths(Ranges, O), Nums),
    sort(Nums, Uniq),
    sum_list(Uniq, Sum).