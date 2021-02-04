import email
import pandas as pd

def extract(data, structured_fields=[], extract_payload=True):
    r"""This function extracts data for the given header list from the Enron email dataset. 
        It provides flexibilty to choose which fields needs to be extracted.
        
        The header list provided by the user are the tags in the email of Enron dataset, eg. Date, Subject etc. 
        By default, if no header is provided, this function returns only the email text body of the Enron dataset.
        
        Arguments:
        1) data: Dataframe It is the Enron dataset with column headings. This argument can not be kept empty.
        2) structured_fields: List It is a of tags for which data needs to be extracted. Example: ['Date', 'Subject', 'X-To']. This argument can be droppped if not required.
        3) extract_pyload: Boolean True if email text body is required. False in case only structured_fields needs to be        extracted. This field can alo be dropped while calling the function. In case nothing is specified, default boolean value True is used.
        
        return: Dataframe A dataframe with specified fields along with the original columns passsed as the data argument.
        
        This function is created to take off the burden of extracting desired fields from the Enron dataset. However, this does not clean the data, eg. it does not remove the empty rows or columns. Neither it does the pre-processing of data like lowercase and removal of unwanted characters.
        
        In order to make it more powerful, above functions can be added. 
        """
    
    headers=data.columns
    emails = data.rename(columns={headers[0]:'email_path', headers[1]:'email'})
    
    #getting structured text 
    def create_dict(dictionary, key, value):
        if key in dictionary:
            values = dictionary.get(key)
            values.append(value)
            dictionary[key] = values
        else:
            dictionary[key] = [value]
        return dictionary

    def get_structured_data(df, fields):
        structured_data = {}
        messages = df["email"]
        for message in messages:
            e = email.message_from_string(message)
            for header in fields:
                header_data = e.get(header)
                create_dict(dictionary = structured_data, key = header, value = header_data)
        return pd.DataFrame(structured_data)
      

    #getting unstructured text
    def get_unstructured_email(df):
        messages = []
        for item in df["email"]:
            e = email.message_from_string(item)    
            message_body = e.get_payload()
            #message_body = message_body.lower()
            messages.append(message_body)
        return messages

    
    if extract_payload == True:
        email_body = get_unstructured_email(emails)
        emails["Message-Body"] = email_body
        structured_data = get_structured_data(emails, structured_fields)
        emails = pd.concat([emails, structured_data], axis=1)
        
    else:
        structured_data = get_structured_data(emails, structured_fields) 
        emails = pd.concat([emails, structured_data], axis=1)

    return emails