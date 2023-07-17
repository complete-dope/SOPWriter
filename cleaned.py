store = []

with open('values.txt', 'r') as f:
    lines = f.readlines()
    store.append(lines)

# print(store)


new_val =[]
for i in store[0]:
    s = i
    new_val.append('https://scholar.google.com' + i[:-1])
    
# print(new_val)
with open('links.txt' , 'w') as f:
    for lines in new_val:
        f.write(f"\n{lines}")

# citations?view_op=view_citation&hl=en&user=iYN86KEAAAAJ&pagesize=100&citation_for_view=iYN86KEAAAAJ:VLnqNzywnoUC

# /citations?view_op=view_citation&hl=en&user=iYN86KEAAAAJ&pagesize=100&citation_for_view=iYN86KEAAAAJ:kNdYIx-mwKoC