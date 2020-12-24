"""
Задание 2.
Написать программу, которая получает на вход имена bed файла и fasta файла,и должна вернуть fasta файл, содержащий последовательности из интервалов, описанных в bed-файле. Каждый интервал – отдельная запись. 
По заголовкам должно быть понятно, к какой исходной последовательности и интервалу относится запись.
"""
from argparse import ArgumentParser
from collections import OrderedDict


def fasta_opener(path) -> dict:
    data = OrderedDict()
    header = None
    f = open(path, 'r')
    for line in f:
        if line.startswith('>'):
            header = line[1:].strip().split(' ')[0]
            data[header] = []
        else:
            data[header].append(line.rstrip())
    f.close()
    for name in data:
        data[name] = ''.join(data[name])
    return data

def main():
    fasta = fasta_opener(args.fasta)
    with open(args.bed, 'r') as bed:
        for line in bed:
            line = line.strip().split()
            chrom = line[0] # change it if other labels
            if chrom in fasta:
                seq = fasta[chrom]
                header = ">" + "_".join(line)
                start, stop = int(line[1]), int(line[2])
                outline = header + '\n' + seq[start:stop]
                print (outline)
                if args.output:
                    outbed = open(args.output + ".fasta", "a")
                    outbed.writelines(outline + "\n")


if __name__ == "__main__":
    parser = ArgumentParser(description="file.fasta filering by file.bed")
    group_required = parser.add_argument_group('Required options')
    group_required.add_argument('-f', '--fasta', type=str, 
                                required=True, help="input fasta file")
    group_required.add_argument('-b', '--bed', type=str, 
                                required=True, help="input bed file")
    group_required.add_argument('-o', '--output', type=str, 
                                default=False, help='output file prefix')
    args = parser.parse_args()
    main()
