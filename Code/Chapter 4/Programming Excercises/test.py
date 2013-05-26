def main():
    seconds = int(input('Enter a number of seconds: '))

    if seconds < 86400:
        if seconds < 3600:
            if seconds < 60:
                print(seconds, 'seconds.')
            else:
                print(format(seconds / 60, ',.1f'), 'minutes.')
        else:
            print(format(seconds / 3600, ',.1f'), 'hours')
    else:
        print(format(seconds / 86400, ',.1f'), 'days')

main()