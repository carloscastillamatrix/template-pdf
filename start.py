
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
output_filename = "test.pdf"

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


def generate_transactions(var=10):
    transactions = []
    for n in range(var):
        transactions.append({"consumer": "07-Nov",
                            "commerce": "Rappi", "amount": "-S/"+str(random.randint(10, 50))+".00",
                             "tea": "21.70",
                             })
    return transactions


# # Main program
if __name__ == "__main__":
    # pisa.showLogging()
    convert_html_to_pdf(addValuesToTemplateHTML(
        source_html, {
            "first_name": "Raico",
            "credit_line": "1,000.00",
            "credit_line_available": "1,000.00",
            "total_mount_payment": "3,000.00",
            "minimum_payment": "500.00",
            "total_transactions": "500.00",
            "account": "1234",
            "tea": "21.70",
            "tea_fee": "51.70",
            "statement_open_date": "18/05/2022",
            "statement_close_date": "17/07/2022",
            "payment_date_payment_last": "12/07/2022",
            "payments": generate_transactions(10),
            "purchase": generate_transactions(10),
        }), output_filename)
