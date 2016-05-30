# Web page scraper

**Author**: Claude Gibert 2016.

## Foreword

I apologise for greatly over-engineering this test. I could have hard-coded the program using Beautiful Soup into a program which would have been hardly longer than the main program here. However I have written page scrapers in the past and I know that if all the web page orgnisation is in the code logic, it is costly to maintain those programs everytime they break, as this requires understanding the code logic again.
I wanted to take up the challenge of describing the web page organisation in a 'scenario' file and write generic code to find all the pieces of information needed from the page(s). This took longer than 2 hours but there was a long week-end.

## Description

Scraping HTML pages is a fragile process which can break everytime the contents or the style of a web page is changed. In order to increase the robustness of the process, it is often tempting to be as little specific as possible regarding the tags which are searched. However, this may cause worse problems that breakage: this may cause *capturing the wrong information without even knowing it*.

As an example of this, in the page describing one particular ripe fruit, we find:

```html
<h3 class="productDataItemHeader">Description</h3>
<div class="productText">
<p>Apricots</p>
<p>
</div>

<h3 class="productDataItemHeader">Nutrition</h3>
<div class="productText">
<div>
<p>
<strong>Table of Nutritional Information</strong>
</p>
...
</div>

<h3 class="productDataItemHeader">Size</h3>
<div class="productText">
<p>5Count</p>
</div>

...
```

If we look for div, class="productText" we will find more than one tag. We could decide that the description if the first one found, but a change in the order, or the insertion of another tag before would break the system. In that case it probably pays off to be specific about what we are looking for. So the strategy is to look for h3, class="productDataItemHeader", check that it contains the string *Description*, take the next sibling tag and search for the *paragraph* tag.

## Design

We decide that the application should raise an exception if the expected conditions for a web page are not met. It is important to be notified if the application fails to find tags as this may mean that the page was changed.

#### 1. Define the different types of search needed and the data needed

Implement those searches using Beautiful Soup and make sure they raise an exception if the tag is not found. This is found in the TagFinder and TagUtils classes.

#### 2. Create tools

Create re-usable tools to support the application: the classes Config, Factory, PageFetcher, TagConsumer

#### 3. Define a format for describing the "geography" of web pages

This is done using a yaml text file, please see the scenarios section and implement support classes: Child, Parent, Sibling

#### 4. Make a map of all tags needed by the application

Access to each tag is given using a hierarchical path (please see also the scenarios section)

#### 5. Write the application to produce what is needed.

This part is completely application dependent and quite 'hard-coded'.

## The scenarios file

The file describes which tag we are looking for in a particular HTML file and how to find them. It also enables the user to name paths to the tags. Here is the file included in the project:

```yaml
ripe fruits:                  <---- name of the scenario corresponding to a web page
    type: parent              <---- type parent: can find more than one tage and returns a list
    name: product             <---- this will be used to create the path
    tag_name: div             <---- we are looking for <div class="product ">
    attr:
      class_: "product "
    inner:                    <---- embedded tags
      - type: parent
        name: productInfo
        tag_name: div         <---- we look for <div class="productInfo">
        attr:
          class_: productInfo
        inner:                <---- embedded tags
          - type: child       <---- this is the final tag, no more embeded ones
            name: link        <---- this tag will be mapped as product.productInfo.link
            tag_name: a       <---- we look for <a ....>
            attr: {}
      - type: child
        name: price           <---- this tag will be mapped ad product.price
        tag_name: p           <---- we look for <p class="pricePerUnit">
        attr:
          class_: pricePerUnit


description:                  <---- scenario for the subpage
    type: sibling             <---- type sibling: return the first tag sibling after the tag found
    name: itemHeader
    tag_name: h3              <---- we look for the tag after <h3 class="productDataItemHeader">
    attr:
      class_: productDataItemHeader
    contents: Description     <---- find the tag which contains the word "Description"
    inner:
      - type: child
        name: description      <---- this tag will be mapped itemHeader.description
        tag_name: p
        attr: {}
```

## Installation and dependencies

The file requirements.txt contains the dependencies create with pip. Run pip install -r requirements.txt.
The dependencies are also named in the setup.py file, these should install with the module. This is a Python 2.7.x program.

To run the application: **python ripefruits.py** the ouput is printed out in the standard output.

## Tests

The tests focus on the tag search logic, making sure that exceptions are raised if something is not found and also making sure that tags are found when they are present.
Please see the test files for more information.

In the main directory run **./run_tests.bash**

## Not done

I don't think the library will work if we describe a page with a parent containing parents (list of lists of tags). I decided not to address this at this point, it would be easy to fix.

In this program, the sub-pages are fetched from the main program, it could be good to implement a mechanism in the 'child' class to read the next scenario name to run from a link. It could then concatenate the paths together to access the tags.
