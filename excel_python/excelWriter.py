#!usr/bin/python

import xlsxwriter
import argparse


def get_args():
  parser = argparse.ArgumentParser(description='Program write data from .txt file to .xlsx')
  parser.add_argument('-f', '--file', help='File which data should come from (.txt)', required=True)
  parser.add_argument('-x', '--xlsx', help='File in which data should be written (.xlsx)', required=True)
  args = parser.parse_args()

  if (args.xlsx[-5:] == ".xlsx" and args.file[-4:] == ".txt"):
    return args
  return False


def get_data(name):
  f = open(name)
  data = f.read().splitlines()
  f.close()
  return data


def write_data(data, workbook):
  worksheet = workbook.add_worksheet()
  worksheet.set_column('A:D', 20)
  style = workbook.add_format({'bg_color': 'yellow'})
  style2 = workbook.add_format({'bold': True})
  style3 = workbook.add_format({'bg_color': "red"})
  style.set_align('center')
  worksheet.write('A1', 'Name', style)
  worksheet.write('B1', 'Surname', style)
  worksheet.write('C1', 'Profession', style)
  worksheet.write('D1', 'Date of Birth', style)

  for i in range(len(data)):
    line = data[i].split(", ")
    for j in range(len(line)):
      if (line[2] == "Developer" and int(line[3][:4]) > 1985):
        worksheet.write(i + 1, j, line[j], style3)
      else:
        worksheet.write(i + 1, j, line[j], style2)
  return ""


def main():
  dataArgs = get_args()
  if (dataArgs):
    workbook = xlsxwriter.Workbook(dataArgs.xlsx)
    data = get_data(dataArgs.file)
    write_data(data, workbook)
    workbook.close()
  else:
    print("Invalid arguments")


if __name__ == "__main__":
  main()
