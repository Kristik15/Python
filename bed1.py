"""
Задание 1.
Написать программу, которая получает на вход имена двух bed файлов и возвращает bed файл, содержащий результат пересечения интервалов из двух входных файлов.
"""
from argparse import ArgumentParser

def main():
    result = []
    tmp_list = []
    with open (args.input[0]) as bed_1:
        for line_1 in bed_1:
            line_1 = line_1.strip().split()
            with open (args.input[1]) as bed_2:
                for line_2 in bed_2:
                    line_2 = line_2.strip().split()
                    if line_1[0] == line_2[0]:
                        chrom = line_1[0]
                        start_1, start_2 = int(line_1[1]), int(line_2[1])
                        stop_1, stop_2 = int(line_1[2]), int(line_2[2])
                        if stop_1 > start_2:
                            start = max([start_1, start_2])
                            stop = min([stop_1, stop_2])
                            tmp_list.append([chrom, start, stop])
    chrom_prev = None
    print(tmp_list)
    for i in range(len(tmp_list)):
        chrom = tmp_list[i][0]
        start, stop = tmp_list[i][1], tmp_list[i][2] # current start and stop
        if chrom == chrom_prev or chrom_prev == None:
            start_prev, stop_prev = tmp_list[i-1][1], tmp_list[i-1][2]
            if result:
                result = result[:-1]
            result.append([chrom, str(max([start, start_prev])), str(min([stop, stop_prev]))])
        else:
            result.append([chrom, str(start), str(stop)])
        chrom_prev = tmp_list[i][0]
    for i in result:
        print("\t".join(i))            
        if args.output:
            outline = "\t".join(i) + "\n"
            outbed = open(args.output + ".bed", "a")
            outbed.writelines(outline)
    print('------')
