#! /usr/bin/env python3

import sys,csv, argparse

def product_dept_dict(products):
    print('>> Reading products file:',products)
    output_dict={}
    with open(products) as csvfile:
        csvreader=csv.DictReader(csvfile,delimiter=',')
        for row in csvreader:
            output_dict[int(row['product_id'])]=int(row['department_id'])
    return output_dict
        
def count_requests(order_products,p2d_dict):
    print('>> Reading order_products file:',order_products)
    output_dict={}
    with open(order_products) as csvfile:
        csvreader=csv.DictReader(csvfile,delimiter=',')
        for row in csvreader:
            try:
                dept=p2d_dict[int(row['product_id'])]
            except:
                sys.stderr.write("Error in: {0}\n\t department not found".format(row))
                continue
            if dept in output_dict:output_dict[dept][0]+=1
            else:output_dict[dept]=[1,0]
            if not int(row['reordered']):output_dict[dept][1]+=1
    return output_dict

def write_outputfile(outputf,count_dict):
    print('>> Writing output file:',outputf)
    depts=sorted(count_dict)
    with open(outputf,'w') as csvfile:
        csvwriter=csv.writer(csvfile,delimiter=',')
        csvwriter.writerow('department_id,number_of_orders,number_of_first_orders,percentage'.split(','))
        for dept in depts: csvwriter.writerow([dept]+count_dict[dept]+["{0:0.2f}".format(count_dict[dept][1]/count_dict[dept][0])])


if __name__=='__main__':
    
    parser=argparse.ArgumentParser()
    parser.add_argument('-p','--products',default='../input/products.csv',help='Input file path for products.csv')
    parser.add_argument('-op','--order_products',default='../input/order_products__train.csv',help='Input file path for order_products.csv')
    parser.add_argument('-o','--outputf',default='../output/report.csv',help='Output file path')
    args=parser.parse_args()


    p2d_dict=product_dept_dict(args.products)
    count_dict=count_requests(args.order_products,p2d_dict)
    write_outputfile(args.outputf,count_dict)
    
