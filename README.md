# takeshoboscrape
Scraper for mangalifewin.takeshobo.co.jp
---
### Usage
Just run it as is.

```python
> py takeshoboscraper.py                                                                   
> Takeshobo Scraper                                                                           
> Made for Made in Abyss                                                                      
> -----Sample Link------                                                                      
> http://mangalifewin.takeshobo.co.jp/global-image/manga/tsukushiakihito/madeinabyss/034/book/
>                                                                                             
> Enter Link: 
```

You can also call it as a module and invoke the `download` command.

```python
> py 
>>> import takeshoboscraper                                                                       
>>> takeshoboscraper.download("http://mangalif...kihito/madeinabyss/034/book/", "path/to/my/directory")                                                                      

```

### Dependencies
 * parse
 * requests