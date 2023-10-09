all: main

main:
	cd ./Arbre-B/src && python3 AffichageGraphique.py

btree:
	cd ./Arbre-B/src && python3 Btree.py

test:
	cd ./Arbre-B/test && python3 TestNode.py
	cd ./Arbre-B/test && python3 TestBtree.py
	cd ./Arbre-B/test && python3 TestComplexity.py

install:
	pip install matplotlib
	pip install PyQt5
	pip install graphviz
	