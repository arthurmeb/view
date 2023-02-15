import openai
import csv
import os
import json
import pandas as pd
import ftfy

openai.api_key = os.getenv("OPENAI_API_KEY")

# Set the path to the lyrics text file
corrupt_file = ["Eminem.txt", "Immortal Technique.txt", "Joey Bada$$.txt"]

# Fix file
for file in corrupt_file:
    count = 1
    name = file.replace('.txt', '')
    with open(file, 'r', encoding='utf-8') as f_in, open('%s_fixed.txt' % name, 'w', encoding='utf-8') as f_out:
        text = f_in.read()
        fixed_text = ftfy.fix_text(text)
        # file that will be iterated on
        f_out.write(fixed_text)
        fixed_file = '%s_fixed.txt' % name

    # Read lines of fixed file
    with open(fixed_file, "r") as f:
        lines = f.readlines()

    # Remove leading and trailing whitespace from each line
    lines = [line.strip() for line in lines]

    # Split the lines into verses based on empty lines
    verses = []
    verse = []
    for line in lines:
        if line:
            verse.append(line)
        else:
            # Only append the verse if it is not empty
            if verse:
                verses.append(verse)
            verse = []
    # Add the last verse if it is not empty
    if verse:
        verses.append(verse)

    lyric_data = list()
    choruses = ['']

    for verse in verses:
        verse_str = ' '.join(verse)
        choruses.append(verse_str)

    # Open a new CSV file
    lyricfile = "%s.csv" % name
    with open(lyricfile,"w", newline="") as csvfile:
        # Create a CSV writer object
        writer = csv.writer(csvfile)
        # Iterate through the verses
        for verse_str in choruses:
            # Check if the verse is a duplicate
            if choruses.count(verse_str) > 1:
                prompt = "Write me a chorus in the style of %s: " % name
                completion = verse_str + "###"
                writer.writerow([prompt, completion])
                lyric_data.append({'prompt': prompt, 'completion': completion})
            else:
                prompt = "Write a rap verse in the style of %s: " % name
                completion = verse_str + "###"
                # Write the prompt and completion to the CSV file
                writer.writerow([prompt, completion])
                # add the data to list
                lyric_data.append({'prompt': prompt, 'completion': completion})

    # save dataframe as csv
    df = pd.read_csv(lyricfile)
    df.to_csv('%s.csv' %name, index=False)

    # Write the data to json file
    with open('%s.jsonl' % name, 'w') as outfile:
        for i in lyric_data:
            json.dump(i, outfile)
            outfile.write('\n')
