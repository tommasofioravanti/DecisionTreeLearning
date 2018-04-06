from ClassError import stratified_k_fold_cross_validation
import TestDataset
#stratified_k_fold_cross_validation(TestDataset.sonar_dataset, 10, 60)
#stratified_k_fold_cross_validation(TestDataset.iono_dataset, 10, 34)
#stratified_k_fold_cross_validation(TestDataset.wine_dataset,10,13)
stratified_k_fold_cross_validation(TestDataset.iris_dataset,10,4)
#stratified_k_fold_cross_validation(TestDataset.banknote_daataset,10,4)
