# Missing Value Filling Function
This short function is built to go into a provided dataframe object and searches for the missing nan values. 
It automatically detect the datatype and suggests the filling method based on mode or mean strategy. 

Limitations
Only considers data type of Object and Float as a result of np.nan replacement
Dataframe must be initially replaced with np.nan 
Uses only mode and mean to replace the missing values depending on the datatype. (Recurring data or Linearly increasing data)

