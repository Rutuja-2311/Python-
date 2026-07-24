# write a program to fill in a letter template with name and date

letter = ''' Dear <|NAME|>,
        You are selected! 
        <|DATE|> '''

print(letter.replace("<|NAME|>", "Rutuja").replace("<|DATE|>", "6th June 2024"))
