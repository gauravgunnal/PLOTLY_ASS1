'''Q1'''
import seaborn as sns
import plotly.express as px

# Load the "titanic" dataset
titanic_data = sns.load_dataset("titanic")

# Create a scatter plot using Plotly Express
fig = px.scatter(titanic_data, x='age', y='fare', title='Scatter Plot of Age vs. Fare in Titanic Dataset')

# Show the scatter plot
fig.show()

'''Q2'''
import plotly.express as px

# Load the "tips" dataset from Plotly Express
tips_data = px.data.tips

# Create a box plot using Plotly Express
fig = px.box(tips_data, x='day', y='total_bill', title='Box Plot of Total Bill Amount by Day')

# Show the box plot
fig.show()

'''Q3'''
import plotly.express as px

# Load the "tips" dataset from Plotly Express
tips_data = px.data.tips

# Create a histogram using Plotly Express
fig = px.histogram(
    tips_data,
    x="sex",
    y="total_bill",
    color="day",
    pattern_shape="smoker",
    title="Histogram of Total Bill Amount by Sex (with Day and Smoker Information)",
)

# Show the histogram
fig.show()

'''Q4'''
import plotly.express as px

# Load the "iris" dataset from Plotly Express
iris_data = px.data.iris

# Create a scatter matrix plot using Plotly Express
fig = px.scatter_matrix(
    iris_data,
    dimensions=["sepal_length", "sepal_width", "petal_length", "petal_width"],
    color="species",
    title="Scatter Matrix Plot of Iris Dataset",
)

# Show the scatter matrix plot
fig.show()

'''Q5'''
'''A `distplot`, short for "distribution plot," is a type of plot used to visualize the distribution of a single variable or univariate data. It combines a histogram with a kernel density estimate (KDE) to provide a smooth representation of the data's probability density function. Essentially, it shows the data's frequency distribution and an estimate of its probability distribution.

To create a `distplot` using Plotly Express, you can follow these steps:

```python'''
import plotly.express as px

# Sample data for demonstration
data = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4, 5, 5, 6]

# Create a distplot using Plotly Express
fig = px.histogram(data, nbins=10, title='Distplot Example')

