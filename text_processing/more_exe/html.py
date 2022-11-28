header = input()
article = input()
print(f"<h1>\n    {header}\n</h1>")
print(f"<article>\n    {article}\n</article>")

text = input()

while text != "end of comments":
    print(f"<div>\n    {text}\n</div>")
    text = input()