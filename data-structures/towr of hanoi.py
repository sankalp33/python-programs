def movetower(height,source,destination,intermediate):
    if height >= 1:
        movetower(height-1,source,intermediate,destination)
        movedisk(source,destination)
        movetower(height-1,intermediate,destination,source)

def movedisk(fp,tp):
    print("Moving Disk from ",fp," to ",tp)

movetower(4,"A","B","C")
