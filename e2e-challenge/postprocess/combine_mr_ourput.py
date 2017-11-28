from itertools import izip

import sys


def zip_mr_and_output(das_filename = "input/dev_exp-das.txt",output_filename="input/output.txt", zip_filename="zip_mr_output.csv"):

    f3 = open(zip_filename, 'wb')

    with open(das_filename) as textfile1, open(output_filename) as textfile2:
        for x, y in izip(textfile1, textfile2):
            x = x.strip()
            y = y.strip()
            z = (x,y)
            #print z
            #f3.write(z)
            #f3.write(str(x) + "," + str(y))
            print>> f3, ("'{0}'\t'{1}'".format(x, y))

    f3.close()

if __name__ == '__main__':
    das_filename= sys.argv[1]
    output_filename= sys.argv[2]
    zip_filename = sys.argv[3]
    zip_mr_and_output(das_filename, output_filename, zip_filename)



