age=int(input('Please enter your age :'))
a=list(range(1,16))
b=list(range(16,35))
if age in a:
    print('What type of cartoon would you like to watch ?')
    print('doremon\nnaruto\nchota bheem')
    cart=str(input(''))
    print('You have Choosen :',cart)
    print('Please find the links below\nhttps://%s.com/'%(cart))
elif age in b:
    print('Movies or Anime ?')
    adult=str(input())
    if adult == 'movies':
        print('transformers\nmatrix\navengers')
        mov=str(input(''))
        print('You have Choosen :',mov)
        print('Please find the links below\nhttps://%s.com/'%(mov))
    else:
        print('naruto\nbleach\nfullmetalalchemist')
        anime=str(input(''))
        print('You have Choosen :',anime)
        print('Please find the links below\nhttps://%s.com/\nhttps://en.wikipedia.org/wiki/Bleach_(TV_series)'%(anime))
else:
    print('Ohh!! we have something great for you\nhttps://www.youtube.com/watch?v=gLPrStGNfq4&list=RDgLPrStGNfq4&start_radio=1')
        

