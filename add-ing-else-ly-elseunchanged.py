def add_ing(string):
    if (len(string) > 2):
        if ((string[-1] == 'g') and (string[-2] == 'n') and (string[-3] == 'i')):
            return (string + 'ly')
        else:
            return (string + 'ing')
    else:
        return (string)



print(add_ing('ra'))