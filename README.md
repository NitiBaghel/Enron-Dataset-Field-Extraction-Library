This function extracts data for the given header list from the Enron email dataset. 
It provides flexibilty to choose which fields needs to be extracted.
        
The header list provided by the user are the tags in the email of Enron dataset, eg. Date, Subject etc. 
By default, if no header is provided, this function returns only the email text body of the Enron dataset.
        
Arguments:
1) data: Dataframe It is the Enron dataset with column headings. This argument can not be kept empty.
2) structured_fields: List It is a of tags for which data needs to be extracted. Example: ['Date', 'Subject', 'X-To']. This argument 		can be droppped if not required.
3) extract_pyload: Boolean True if email text body is required. False in case only structured_fields needs to be extracted. This field can alo be dropped while calling the function. In case nothing is specified, default boolean value True is used.

return: Dataframe A dataframe with specified fields along with the original columns passsed as the data argument.
        

		Steps to use this library:

		1) Clone this repository or download the zip folder and extarct it.

		2) Once step 1 is done: In the terminal move to the folder 'dist' and run the command 'pip install dist/extractenronlib-0.1.0-py3-none-any.whl' 

		3) Step 2 will install the library and its ready to use. In order to use the library, just use 'from extractenronlib import extractenron' to import the library. Then 'extract' method can be used as follows:
		
		a) Only Specific Tags:
		emails_extracted = extractenron.extract(emails, ['Date', 'Subject'], extract_payload=False) 

		b) Only Payload (Email message):
		emails_extracted = extractenron.extract(emails)

		c) Some Specific Tags and Payload:
		emails_extracted = extractenron.extract(emails, ['Date', 'Subject'], extract_payload=True)


This function is created to take off the burden of extracting desired fields from the Enron dataset. However, this does not clean the data, eg. it does not remove the empty rows or columns. Neither it does the pre-processing of data like lowercase and removal of unwanted characters.
        
In order to make it more powerful, above functions can be added. 
