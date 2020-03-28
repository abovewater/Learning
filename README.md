# Learning

<h2>Wine Web Scraper</h2>
<p>I wanted to continue to learn how to best use beautiful soup to scrape the web to get details from a list or a number of results. While it is still really basic, this script scrapes the page from our wine club and presents the first page of results then prints them to a CSV file.</p>

<p><strong>What I learned from this project</strong></p>

<h4>Taking the results and striping the meta tags</h4>
<p>I was having a lot of trouble when it came to striping away the tags initially. I was driving me up the wall. I put the computer down and walked away. In the end I found that I could use</p>
```python
        list_bottles = [wine.get_text(strip = True) for wine in soup.find_all('div',{'class':'name'})]
```
<p>I found a thread on stack overflow that was essentially showed me how I could achieve removing the tags from the list while at the same time passing it into my list. I was originally printing the content to the console because as I progress through Treehouse that is where all of the content is being taught. But I really wanted to step it up and move on to actually accomplishing something.</p>
<h4>Creating a CSV file</h4>
<p>So the next step was to scrape content from the web and then pass that to a CSV file. I am still not fully across the use of the CSV module in Python but for the interim, I was able to take the list that I downloaded and write that to a CSV file. My initial challenge was that it was writing all the content to a single row. I wanted the list in a column. I solved that issue by adding the for loop in the csv module.</p>
```python
for drink in list_bottles:
        wr.writerow([drink])
```
<p>This solved that issue. However the next issue I had was there was a gap in between each of the items. After more googling and a lot more searching on stack overflow, I found that in order to remove the space between the items was to add newline</p>
```python
with open('wine_list.csv', 'w', newline='') as myfile:
```
<p>So by adding newline to the with statement I was able to print the list to csv file and all in one column.</p>

<h4>Final Thoughts</h4>
<p>This was a fun little project, building on the skills I picked up the other day scraping the web for a share price. Little projects like this are helping to see what a useful language Python is.</p>
