This function extracts data for the given header list from the Enron email dataset. 
It provides flexibilty to choose which fields needs to be extracted.
        
The header list provided by the user are the tags in the email of Enron dataset, eg. Date, Subject etc. 
By default, if no header is provided, this function returns only the email text body of the Enron dataset.
        
        Arguments:
        1) data: Dataframe It is the Enron dataset with column headings. This argument can not be kept empty.
        2) structured_fields: List It is a of tags for which data needs to be extracted. Example: ['Date', 'Subject', 'X-To']. This argument 		can be droppped if not required.
        3) extract_pyload: Boolean True if email text body is required. False in case only structured_fields needs to be        extracted. This 	field can alo be dropped while calling the function. In case nothing is specified, default boolean value True is used.
        
        return: Dataframe A dataframe with specified fields along with the original columns passsed as the data argument.
        
This function is created to take off the burden of extracting desired fields from the Enron dataset. However, this does not clean the data, eg. it does not remove the empty rows or columns. Neither it does the pre-processing of data like lowercase and removal of unwanted characters.
        
In order to make it more powerful, above functions can be added. 
