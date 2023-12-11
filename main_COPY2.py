def view_the_log()  -> 'str' :
    contents = []
    with open('vsearch.log') as log :
        for line in log:
            contents.append([])
            for item in line.split('|') :
  #              print(item)
                contents[-1].append(item)
 #               print(contents)
# print(contents)
    return str(contents)


abc=view_the_log()
print(abc)

            