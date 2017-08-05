import argparse

parser = argparse.ArgumentParser(description='User details through argparse')

parser.add_argument('--name', action='store', dest='name', required=True)
parser.add_argument('--age', action='store',dest='age', type=int, required=False)

given_args = parser.parse_args()

print('Name : {}'.format(given_args.name))
print('Age : {}'.format(given_args.age))