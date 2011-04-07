This is an attempt to use Django as a tool to organize and analyze scientific data.

#Why?

Django is a clean web framework written in Python. I've been using it to develop web apps and wondered how useful it could be for managing scientific data. I decided to give it a try with some real (unpublished) data from my master's thesis.

Features that made me do it:

- Store data on a relational database.
- Flexible and powerful querysets to retrieve and combine data.
- Customizable views to perform tasks, layout, and aggregate data the way you want.
- Keep in one place all related files (data, functions, results, etc...) in an organized matter.
- Python powered: freedom to write functions and plug external libraries for stats and plotting (R, SciPy, MatPlotLib).

#Use Case

I am analyzing histological sections of gonadal tissue from an echinoderm (spiny marine invertebrate). I basically have a bunch of photomicrographs which need to be staged (1831 to be precise), information about the collected specimen (date, height, gender), and measurements of gonadal tubules from a different set of photomicrographs.

In order to accomplish my objective I had to: design the database to accomodate original data; import data into the project; create the views/templates to analyze data; create views to process results (stats and plots); _next step_?

##Database Design

_To be written..._

##Data Input

Simple Python script reading CSV files and saving in the database.

##Analysis

Staging is a daunting task where you need to be fully aware of sampling variation in order to trace the arbitrary line between stages. So I need to make observations and take notes for each photo and be able to compile this information. Also, It is better if I do not know the date/identification of the photo I am observing to avoid bias (eg, it is common to have mature gonads on summer, so knowing this could induce an errouneous classification) and make the observations in random order, for the same reason. The regular approach of opening images (typically organized by folder/date) on a regular file browser could undermine the analysis.

For this I build a view which shows a random section screen-wide without any identification visible with a form below to fill with notes, the gonadal stage, and mark if the stage is uncertain or the image is good for publication.

_To be continued..._

##Processing Results

_To be written..._

###Stats

_To be written..._

###Plotting

_To be written..._

#Meta Case

This is also a form of experimenting Git as a scientific tool to share and collectively improve someone's work. Although I am sharing basically code, consider adding the manuscript itself alongside the analysis. Your collaborator or reviewer would be able to just `git clone` your repository and make corrections to your code or text. Everything is stored, everything is tracked.
