from argparse import ArgumentParser
from main import plotgreengraph


def process():
   parser = ArgumentParser(description = "Look at green space between two locations.")

   parser.add_argument('loc1')
   parser.add_argument('loc2')

   arguments= parser.parse_args()
   
   plotgreengraph(arguments.loc1, arguments.loc2)
   
if __name__ == "__main__":
    process() 