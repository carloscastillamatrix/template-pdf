
# import python module
from xhtml2pdf import pisa
from jinja2 import Environment, BaseLoader
import random
# open text file in read mode
text_file = open("./index.html", "r")
# read whole file to a string
source_html = text_file.read()
# close file
text_file.close()


# Define your data
output_filename = "eecc-v1.pdf"

# Utility function


def addValuesToTemplateHTML(source_html, data):
    rtemplate = Environment(loader=BaseLoader).from_string(source_html)
    html = rtemplate.render(data)

    return html


def convert_html_to_pdf(source_html, output_filename):
    # open output file for writing (truncated binary)
    result_file = open(output_filename, "w+b")

    # convert HTML to PDF
    pisa_status = pisa.CreatePDF(
        source_html,                # the HTML to convert
        dest=result_file)           # file handle to recieve result

    # close output file
    result_file.close()                 # close output file

    # return False on success and True on errors
    return pisa_status.err


def generate_transactions_paid(var=10):
    transactions = []
    for n in range(var):
        transactions.append({"transaction_date": "07-nov",
                            "description": "Rappi", "amount": "+S/"+str(random.randint(10, 3000))+".00",
                             "tea": "21.70",
                             })
    return transactions

def generate_transactions(var=10):
    transactions = []
    for n in range(var):
        transactions.append({"transaction_date": "07-nov",
                            "description": "Rappi", "amount": "-S/"+str(random.randint(10, 3000))+".00",
                             "tea": "21.70",
                             })
    return transactions


# # Main program
if __name__ == "__main__":
    # pisa.showLogging()
    convert_html_to_pdf(addValuesToTemplateHTML(
        source_html, {
            "credit_line_limit": "S/ 10,000.00",
            "available_credit_line":"S/ 6,782.50",
            "total_consumed_credit_line":"S/ 3,217.50",
            "minimum_payment": "S/ 5.00",
            "transactions_total_amount": "-S/ 2,237.50",
            "card_mask": "1234",
            "tea": "21.70%",
            "tim": "51.70%",
            "billing_cycle_start_date": "18/05/2022",
            "billing_cycle_close_date": "17/07/2022",
            "transactions_paid": generate_transactions_paid(10),
            "transactions_comsumed": generate_transactions(10),
            "previous_balance":"S/449.00",
            "total_payments":"(S/1,000.00)",
            "total_consumption":"S/3,237.50",
            "billed_total_payment":"S/ 3,000.00",
            "minimun_payment":"S/ 500.00",
            "statement_close_date":"30/05/2022",
            "first_name":"Jhon",
            
            "date_day_name":"Domingo",
            "date_format_ll":"12 feb 23",
            "interest_compensatory":"S/36.90",
            "interest_late":"S/16.90",
            "desgravamen_insurance":"S/1.03",
        }), output_filename)
