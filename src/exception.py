import sys
import logging

def error_messages_details(error, error_detail:sys):
    _, _, error_tb = error_detail.exc_info()
    filename = error_tb.tb_frame.f_code.co_filename
    line_num = error_tb.tb_lineno
    error_message = "Error occurred in python script name [{0}], line number [{1}], error message [{2}]".format(filename, line_num, str(error))
    
    return error_message

class CustomException(Exception):
    def __init__(self, error_message, error_detail:sys):
        super().__init__(error_message)

        self.error_message = error_messages_details(error_message, error_detail)
        
        
    def __str__(self) -> str:
        return self.error_message
