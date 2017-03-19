number	=	23

running	=	True
while	running:
    guess = int(input('Enter	an	integer	:	'))
    if guess == number:
        print('Congratulation you guess it!\n')
        break  #continue
    elif guess < number:
        print('NO,it\'s a litter higher than that')
    else:
        print('NO,it\'s a litter lower than that')
print('Done')
