try:
    f = open("ab.txt")
    a= 10
    b= 0
    print(a/b)
    for line in f:
        print(line)

#except (FileNotFoundError, ZeroDivisionError) :      #   this gives us the error name-   except Exception as e:
 #   print("Unable to find file")                                                        #print(e)

except ZeroDivisionError:
    print("Zero division error bro")
except FileNotFoundError:
    print("file not foundd")
#write print(dir(e)) to find what all e can show.

# i= 0/0
# We added it here just for fun

