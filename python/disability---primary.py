# Kuan V, Denaxas S, Gonzalez-Izquierdo A, Direk K, Bhatti O, Husain S, Sutaria S, Hingorani M, Nitsch D, Parisinos C, Lumbers T, Mathur R, Sofat R, Casas JP, Wong I, Hemingway H, Hingorani A, 2023.

import sys, csv, re

codes = [{"code":"100648.0","system":"med"},{"code":"107968.0","system":"med"},{"code":"1278.0","system":"med"},{"code":"1362.0","system":"med"},{"code":"1680.0","system":"med"},{"code":"16855.0","system":"med"},{"code":"1787.0","system":"med"},{"code":"27691.0","system":"med"},{"code":"28740.0","system":"med"},{"code":"28962.0","system":"med"},{"code":"302.0","system":"med"},{"code":"32820.0","system":"med"},{"code":"33949.0","system":"med"},{"code":"34174.0","system":"med"},{"code":"34734.0","system":"med"},{"code":"36045.0","system":"med"},{"code":"36143.0","system":"med"},{"code":"37867.0","system":"med"},{"code":"37887.0","system":"med"},{"code":"37911.0","system":"med"},{"code":"39016.0","system":"med"},{"code":"39412.0","system":"med"},{"code":"42520.0","system":"med"},{"code":"42589.0","system":"med"},{"code":"42886.0","system":"med"},{"code":"4477.0","system":"med"},{"code":"45133.0","system":"med"},{"code":"46504.0","system":"med"},{"code":"4672.0","system":"med"},{"code":"4825.0","system":"med"},{"code":"50606.0","system":"med"},{"code":"50751.0","system":"med"},{"code":"50947.0","system":"med"},{"code":"51268.0","system":"med"},{"code":"51622.0","system":"med"},{"code":"51954.0","system":"med"},{"code":"52602.0","system":"med"},{"code":"54179.0","system":"med"},{"code":"54881.0","system":"med"},{"code":"55560.0","system":"med"},{"code":"55848.0","system":"med"},{"code":"56547.0","system":"med"},{"code":"56577.0","system":"med"},{"code":"57199.0","system":"med"},{"code":"59407.0","system":"med"},{"code":"60062.0","system":"med"},{"code":"60473.0","system":"med"},{"code":"60913.0","system":"med"},{"code":"6123.0","system":"med"},{"code":"63273.0","system":"med"},{"code":"6516.0","system":"med"},{"code":"65468.0","system":"med"},{"code":"66383.0","system":"med"},{"code":"66783.0","system":"med"},{"code":"70008.0","system":"med"},{"code":"70102.0","system":"med"},{"code":"71196.0","system":"med"},{"code":"71632.0","system":"med"},{"code":"90276.0","system":"med"},{"code":"98100.0","system":"med"},{"code":"98293.0","system":"med"},{"code":"98342.0","system":"med"},{"code":"99774.0","system":"med"}];
REQUIRED_CODES = 1;
with open(sys.argv[1], 'r') as file_in, open('intellectual-disability-potential-cases.csv', 'w', newline='') as file_out:
    csv_reader = csv.DictReader(file_in)
    csv_writer = csv.DictWriter(file_out, csv_reader.fieldnames + ["disability---primary-identified"])
    csv_writer.writeheader();
    codes_identified = 0;
    for row in csv_reader:
        newRow = row.copy();
        for cell in row:
            # Iterate cell lists (e.g. codes)
            for item in re.findall(r'\(([^,]*)\,', row[cell]):
                if(item in list(map(lambda code: code['code'], codes))): codes_identified+=1;
                if(codes_identified>=REQUIRED_CODES):
                    newRow["disability---primary-identified"] = "CASE";
                    break;
            if(codes_identified>=REQUIRED_CODES): break;
        if(codes_identified<REQUIRED_CODES):
            newRow["disability---primary-identified"] = "UNK";
        codes_identified=0;
        csv_writer.writerow(newRow)
