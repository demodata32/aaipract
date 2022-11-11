go:-
hypothesis(Disease),
write('I believe you have: '),
write(Disease),
nl,
undo.

hypothesis(cold) :- cold.
hypothesis(flu) :- flu.

cold :-
verify(headache),
verify(runny_nose),
verify(sneezing),
verify(sore_throat),
nl.

flu :-
verify(fever),
verify(headache),
verify(chills),
verify(body_ache),
nl.

ask(Question) :-
write('Does the patient have following symptom: '),
write(Question),
write('?'),
read(Response),
nl,
( (Response == yes ; Response == y)
->
assert(yes(Question));
assert(no(Question)), fail).

:- dynamic yes/1,no/1.
verify(S) :-
 (yes(S)
  ->
   true ;
    (no(S)
     ->
      fail;
       ask(S))).

undo :- retract(yes(_)),fail.
undo :- retract(no(_)),fail.
undo.
