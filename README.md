# **Wiki**

![](https://upload.wikimedia.org/wikipedia/en/thumb/6/6c/Wiki_letter_w.svg/200px-Wiki_letter_w.svg.png )

[![](https://img.shields.io/badge/author-@atefdodo-blue.svg?style=flat)](https://github.com/atefdodo)    ![](https://img.shields.io/badge/build-HTML5-red.svg?style=flat) [![](https://img.shields.io/badge/Valid-W3C_CSS-green.svg?style=flat)](http://jigsaw.w3.org/css-validator) ![](https://img.shields.io/badge/build-font_awasome-blueviolet.svg?style=flat)   ![](https://img.shields.io/badge/Python-v 3.1.3-blue.svg?style=flat)   ![](https://img.shields.io/pypi/djversions/djangorestframework)

**> Design a Wikipedia-like online encyclopedia.**


  - Index page (home page).
  - Images search page.
  - Advanced search page.

## **Demo Link!**

  - [You Tube screencast ](https://youtu.be/j75pYUqBWgw "You Tube screencast ")


## **Specification**
> #### Entry Page
 ```
Visiting /wiki/TITLE, where TITLE is the title of an encyclopedia entry, should render a page that displays the contents of that encyclopedia entry.
 The view should get the content of the encyclopedia entry by calling the appropriate util function.
If an entry is requested that does not exist, the user should be presented with an error page indicating that their requested page was not found.
 If the entry does exist, the user should be presented with a page that displays the content of the entry. The title of the page should include the name of the entry.
 ```
> #### Index Page
  ```
Update index.html such that, instead of merely listing the names of all pages in the encyclopedia, user can click on any entry name to be taken directly to that entry page.
 ```
#### Search
  ```
Allow the user to type a query into the search box in the sidebar to search for an encyclopedia entry.
 If the query matches the name of an encyclopedia entry, the user should be redirected to that entry’s page.
If the query does not match the name of an encyclopedia entry, the user should instead be taken to a search results page that displays a list of all encyclopedia entries that have the query as a sub-string. For example, if the search query were Py, then Python should appear in the search results.
Clicking on any of the entry names on the search results page should take the user to that entry's page.
 ```
#### New Page
  ```
Clicking "Create New Page" in the sidebar should take the user to a page where they can create a new encyclopedia entry.
 Users should be able to enter a title for the page and, in a text-area, should be able to enter the Markdown content for the page.
Users should be able to click a button to save their new page.
When the page is saved, if an encyclopedia entry already exists with the provided title, the user should be presented with an error message.
Otherwise, the encyclopedia entry should be saved to disk, and the user should be taken to the new entry's page.
 ```
 #### Edit Page
  ```
On each entry page, the user should be able to click a link to be taken to a page where the user can edit that entry’s Markdown content in a textarea.
The textarea should be pre-populated with the existing Markdown content of the page. (i.e., the existing content should be the initial value of the textarea).
The user should be able to click a button to save the changes made to the entry.
Once the entry is saved, the user should be redirected back to that entry's page.
 ```
 #### Random Page
  ```
Clicking “Random Page” in the sidebar should take user to a random encyclopedia entry.
 ```
 #### Markdown to HTML Conversion
  ```
I tried using python-markdown2 but still have a bug type" object 'Markdown' has no attribute 'markdown' " so I manage to find alternative way by using templatetags inside the project itself.
 ```
# Wiki
# Wiki
# Wiki
# Wiki
