def main():


  f = open("quotes.txt")
  quotes = f.readlines()
  f.close()

  print(quotes[13])

if __name__== "__main__":
  main()
