# PROGETTO AI
#TOMMASO FIORAVANTI 5938832

Versione Python utilizzata: 2.7

#Nel file DecisionTreeLearning.py è presente l'implementazione dell'algoritmo decision_tree_learning ripreso da R&N 2009 §18.3.

#Nel file CreateDatasets.py sono implementate le funzioni per creare il dataset dopo aver preso in input il file di testo che contiene tutti i dati. La funzione create_dataset_iono() serve per creare il dataset del file ionosphere.txt poichè per l'utilizzo corretto della funzione stratified-k-cross-fold-validation() è necessario che gli esempi siano ordinati per classificazione (esempi con la stessa classificazione si devono trovare tutti in sequenza). La funzione get_values() serve per prendere ordinati ed unici tutti i valori di ogni attributo per il dataset scelto. #Per la stampa dell'albero si chiama il metodo display della classe DecisionTree.

#Nel file ClassError.py è implementata la funzione per calcolare la 10-fold cross validation stratificata che utilizza la funzione create_class_list() la quale divide gli esempi con classificazione diversa in liste diverse. Dopodichè ogni lista è divisa in 10 sottogruppi ed ad ogni iterazione viene unito ogni gruppetto di ogni lista diversa per formare il test set, l'unione dei restanti gruppi sarà il training test.

#Per la stampa e la costruzione dell'albero in DecisionTree.py è utilizzato un booleano nella funzione add() per vedere se gli esempi aggiunti hanno valore maggiore o minore della soglia. Infatti nella funzione display() ,che serve a stampare l'albero, si fa un controllo sul booleano ed a seconda del valore si stampa il nome dell'attributo maggiore o minore della soglia.  
 
#Per eseguire il programma si deve eseguire il file Main.py. Per esegurilo scegliere il dataset da testare nel file TestDataset.py, modificare i parametri passati alla funzione get_values in DecisionTreeLearner(si deve passare il file di testo corrispondente al dataset scelto e il numero di attributi di questo). Nel file Main è richiamata la funzione stratified_k_fold_cross_validation a cui si deve passare il dataset scelto, il numero dei fold (10) e il numero di attributi del dataset. Il programma riporterà la media e la deviazione standard dell'errore sul train e sul test set (in percentuale).

#Per il calcolo della media e della deviazione standard sono state utilizzate le funzioni mean e std di numpy. Sono state utilizzate anche le librerie "random" (per mischiare gli esempi), "math"(per il calcolo del logaritmo nell'entropia) e "print_function"(per la stampa dell'albero)

#La stampa dell'albero, la struttura della funzione decision tree learning e delle funzioni utilizzate da questa (file DecisionTreeLearning.py) e la struttura del dataset sono state riprese dal repository di aima (https://github.com/aimacode/aima-python/blob/master/learning.py questo il link) con opportune modifiche ed aggiunte per l'apprendimento di attributi continui.
