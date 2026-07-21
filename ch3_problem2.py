letter = ''' Dear <|NAME|>,
        You are selected! 
        <|DATE|> '''

print(letter.replace("<|NAME|>", "Rutuja").replace("<|DATE|>", "6th June 2024"))