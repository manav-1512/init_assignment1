MANAV SHAH
SE IT 60003180025
+91-9930447996 | manavhshah00@gmail.com

Assignment - 1:

The script files int the folder have the code for the regression operations performed on the dataset.

visualisation.py is used to create the image of pair plots of all significant features in the dataset
imdb_regression.py contains the code for random forest regression performed on some of the numeric columns of dataset and encoded the genre and/or the plot keywords.
imdb_regression.numeric_only.py contains the code for random forest regression performed on only numeric columns.
encoding.py contains the functions for encoding genre and the plot keywords

pairplot.png is the image of all pair plots made using seaborn.

The genre column is encoded using a custom function that may be substituted as N-Hot encoding.
The plot keyword columns is used to create a bag of words using Natural Language Processing Toolkit 

PCA or Principle Component Ananlysis is used to extract features from the dataset an thereby enhance the regression.

Some Numeric features and Genre columns are considered:
 
PS C:\Users\HP\Desktop\Movie_IMDB> cd 'c:\Users\HP\Desktop\Movie_IMDB';  & 'C:\Users\HP\AppData\Local\Programs\Python\Python38\python.exe' 'c:\Users\HP\.vscode\extensions\ms-python.python-2020.6.90262\pythonFiles\lib\python\debugpy\launcher' '60422' '--' 'c:\Users\HP\Desktop\Movie_IMDB\imdb_regression.py'
Enter 1 for including plot keyword or enter 0 0
Mean Squared Error = 0.47 

Some Numeric features, Genre and Plot Keyword columns are considered:

PS C:\Users\HP\Desktop\Movie_IMDB>  cd 'c:\Users\HP\Desktop\Movie_IMDB'; & 'C:\Users\HP\AppData\Local\Programs\Python\Python38\python.exe' 'c:\Users\HP\.vscode\extensions\ms-python.python-2020.6.90262\pythonFiles\lib\python\debugpy\launcher' '60431' '--' 'c:\Users\HP\Desktop\Movie_IMDB\imdb_regression.py'
Enter 1 for including plot keyword or enter 0 1
Mean Squared Error = 0.54

Only some Numeric features are considered:

PS C:\Users\HP\Desktop\Movie_IMDB>  cd 'c:\Users\HP\Desktop\Movie_IMDB'; & 'C:\Users\HP\AppData\Local\Programs\Python\Python38\python.exe' 'c:\Users\HP\.vscode\extensions\ms-python.python-2020.6.90262\pythonFiles\lib\python\debugpy\launcher' '60571' '--' 'c:\Users\HP\Desktop\Movie_IMDB\imdb_regression_numeric_only.py' 
Mean Squared Error = 0.59
