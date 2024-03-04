def getTalk(type="shout"):
 
    def shout(word="да"):
        return word.capitalize()+"!"
 
    def whisper(word="да") :
        return word.lower()+"..."
 
    if type == "shout":

        return shout
    else:
        return whisper
 
talk = getTalk()
 
print(talk)
print(talk())
 
print(getTalk("whisper")())
