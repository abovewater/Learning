# learning

<h2>Wine Web Scraper</h2>
<p>I wanted to continue to learn how to best use beautiful soup to scrape the web to get details from a list or a number of results. While it is still really basic, this script scrapes the page from our wine club and presents the first page of results then prints them to a CSV file.</p>
<p><strong>What I learned from this project</strong></p>

<h4>Taking the results and striping the meta tags</h4>
<p>I was having a lot of trouble when it came to striping away the tags initially. I was driving me up the wall. I put the computer down and walked away. In the end I found that I could use</p>
```python
        wine.get_text(strip = True)
```
<p>This was placed inside the hard brackets before the for loop I called to locate all the div tags</p>
