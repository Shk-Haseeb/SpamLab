from spamfilter import SpamFilter

def main():
    spam_filter = SpamFilter('spamcount.txt', 'hamcount.txt')

    print("spam_play.txt →", spam_filter.classify_from_file('spam_play.txt'))
    print("ham_play.txt →", spam_filter.classify_from_file('ham_play.txt'))
    # You can also classify from keyboard input:
    # print("Your message →", spam_filter.classify_from_input())

if __name__ == '__main__':
    main()
