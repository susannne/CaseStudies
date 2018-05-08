set paths := p1 p2 p3 p4 p5 p6;

set trips := A B C;

set depots := d1 d2 d3;

param:req_seats := 
A 50
B 40
C 30;

param:node_seq :=
p1 (d1 A d1)
p2 (d2 B d2)
p3 (d3 C d3)
p4 (d1 A B d1)
p5 (d1 A C d1)
p6 (d2 B C d2) ;


param:costs :=
p1 100
p2 150
p3 400
p4 200
p5 400
p6 450;
