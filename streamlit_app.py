# Imported libraries
import streamlit as st
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns
import altair as alt
from wordcloud import WordCloud
from mpl_toolkits.mplot3d import Axes3D
from io import StringIO


#General Information About The Group
st.write("CSS145_BM4_1Q2425")
st.title("Group 2: ")

st.markdown("""
- Aleah Balagao
- Sean Chester Cabantog
- John Daniel Garina
- Gian Carlo Mateo
- Felipe Panugan
""")

#imported datasheet

#The variable df is set to the read csv dataset
df = pd.read_csv("laptop_price - dataset.csv")

#this shows the datasheet
st.markdown("### Laptop_Price DataSheet")
st.dataframe(df)

#Shows information about the data set such as the column, datatype, and other relevant info.
st.markdown("### Info About Datasheet")
buffer = StringIO()
df.info(buf=buffer)
info_str = buffer.getvalue()  
st.text(info_str)

#Shows the null values present.
st.markdown("### Present Null Values in the DataSheet")
st.dataframe(df.isna().sum())

#Shows the generated descriptive statistics of the dataset
st.markdown("### DataSheet Descriptive Statistics")
st.dataframe(df.describe())

#Shows general information about how we used the barchart
st.title("Bar Chart")
st.markdown("Used to accomplish the following: ")
st.markdown("""
1. Show the different amount of unique laptops per company
2. Identify the company with the most amount of unique laptops
3. Identify the company with the least amount of unique laptops
""")

#Creates the appropriate Bar Graph to show the different companies that are selling their respective number of unique laptop devices
def barchart():
  company_count = df['Company'].value_counts()
  plt.bar(company_count.index, company_count.values)
  plt.xticks(rotation=75)
  plt.title("Companies and Their Number of Unique Laptop/s")
  plt.xlabel("Company")
  plt.ylabel("Number of Unique Laptops")
  #syntax to show the chart on streamlit
  st.pyplot(plt)
  #This clears the elements of the previous graph, a must properly run graphs
  plt.clf()

barchart()

#Shows general information about how we used the piechart
st.title("Pie Chart")
st.markdown("Used to accomplish the following: ")
st.markdown("""
1. Show the market share of each of the gpu manufacturers
2. Identify the company with the largest market share
3. Identify the company with the smallest market share
""")

#Creates the appropriate Pie Chart to show the different GPU manufacturers according to their presence in laptop devices
def pie_chart():
  gpuCompany_count = df['GPU_Company'].value_counts()
  plt.pie(gpuCompany_count.values, labels = gpuCompany_count.index, autopct='%1.1f%%')
  plt.title("Laptops and their GPU Manufacturers")
  #syntax to show the chart on streamlit
  st.pyplot(plt)
  #This clears the elements of the previous graph, a must properly run graphs
  plt.clf()

pie_chart()



#Box plot
st.title("Box Plot: Laptop Price Distribution by CPU Company")
st.markdown("Used to accomplish the following:")
st.markdown("""
1. To compare laptop prices (in Euro) sold by different CPU companies
""")

def box_plot():
    plt.figure(figsize=(10, 6))
    sns.boxplot(x='CPU_Company', y='Price (Euro)', data=df)
    plt.title('Laptop Price Distribution by CPU Company')
    plt.xlabel('CPU Company')
    plt.ylabel('Price (Euro)')
    plt.xticks(rotation=45)
    plt.grid(True)
    st.pyplot(plt)
    #This clears the elements of the previous graph, a must properly run graphs
    plt.clf()  

box_plot()

#Scatter Plot
st.title("Scatter Plot: Laptop Price vs. Screen Size")
st.markdown("Used to accomplish the following: ")
st.markdown("""
1. To define the relationship between screen size (in inches) and laptop price.
2. To visualize the distribution of prices across different screen sizes.
""")

def scatter_plot():
    plt.figure(figsize=(10, 6))
    plt.scatter(df['Inches'], df['Price (Euro)'], color='b', alpha=0.5)
    plt.title('Laptop Price vs. Screen Size (Inches)')
    plt.xlabel('Screen Size (Inches)')
    plt.ylabel('Price (Euro)')
    plt.grid(True)
    st.pyplot(plt)
    #This clears the elements of the previous graph, a must properly run graphs
    plt.clf()

scatter_plot()

#Shows general information about how we used the densityplot
st.title("Density Plot")
st.markdown("Used to accomplish the following: ")
st.markdown("""
1. Show the distribution of laptop prices
2. Show the natural trend of laptop prices
""")

# Create a density plot for laptop prices
def density_plot():
  sns.kdeplot(df['Price (Euro)'], fill=True)
  plt.title('Trend of Laptop Prices')
  plt.xlabel('Price (Euro)')
  plt.ylabel('Density')
  plt.show()
  #syntax to show the chart on streamlit
  st.pyplot(plt)
  #This clears the elements of the previous graph, a must properly run graphs
  plt.clf()
  
density_plot()

#Shows general information about how we used the heatmap
st.title("Heat Map")
st.markdown("Used to accomplish the following: ")
st.markdown("""
1. To track the cpu frequency provided by each CPU company
2. To track the the amount of CPUs that provides a certain frequency
""")

#heatmap for CPU company and the CPU frequency
def heatmap():
  cpu_vs_type = pd.crosstab(df['CPU_Company'], df['CPU_Frequency (GHz)'])
  plt.figure(figsize=(12, 8))
  sns.heatmap(cpu_vs_type, annot=True, fmt='d', cmap='viridis')
  plt.title('Heatmap of CPU Company and CPU Frequency')
  plt.xlabel('CPU Frequency (GHz)')
  plt.ylabel('CPU Company')
  plt.show()
  #syntax to show the chart on streamlit
  st.pyplot(plt)
  #This clears the elements of the previous graph, a must properly run graphs
  plt.clf()
  
heatmap()

#Shows general information about how we used the heatmap
st.title("Historgram")
st.markdown("Used to accomplish the following: ")
st.markdown("""
1. Show the distribution of Laptop Prices according to their frequency
2. Identift the most common price point of laptops
""")

def histogram():
  plt.hist(df['Price (Euro)'], bins=20, edgecolor='black')
  plt.xlabel('Price (Euro)')
  plt.ylabel('Frequency')
  plt.title('Histogram of Laptop Prices')
  st.pyplot(plt)
  #This clears the elements of the previous graph, a must properly run graphs
  plt.clf()

histogram()

#Shows general information about how we used the Line Graph
st.title("Line Graph")
st.markdown("Used to accomplish the following: ")
st.markdown("""
1.   Track the fluctuations in the price of laptop RAM
2.   Show the trends in the pricepoints of ram according to the price and RAM
""")
def line_graph():
  # Group data by year and calculate the average price
  price_by_year = df.groupby('RAM (GB)')['Price (Euro)'].mean()

  # Create a line graph
  plt.plot(price_by_year.index, price_by_year.values)

  # Set labels and title
  plt.xlabel('RAM (GB)')
  plt.ylabel('Average Price (Euro)')
  plt.title('Average Laptop Price by RAM (GB)')
  st.pyplot(plt)
  #This clears the elements of the previous graph, a must properly run graphs
  plt.clf()


line_graph()


st.title("Violin Plot")
st.markdown("Used to accomplish the following: ")
st.markdown("""
1. Visualize the distribution of laptop prices across different brands
2. Show the trends of price ranges among different laptop brands
""")

#violin plot for laptop brands and their prices
def violin_plot():
  sns.set(style="darkgrid")
  sns.set_context("notebook")
  plt.gca().xaxis.set_major_locator(plt.MultipleLocator(1000))
  sns.violinplot(data=df, x='Price (Euro)', y='Company', palette="rainbow", hue='Company')
  plt.xlabel('Price (Euro)')
  plt.xticks(rotation=45)
  plt.ylabel('Laptop Brand')
  plt.title('Laptop Prices by Brand')
  plt.show()
  #syntax to show the chart on streamlit
  st.pyplot(plt)
  #This clears the elements of the previous graph, a must properly run graphs
  plt.clf()
  
violin_plot()

st.title("Word Cloud")
st.markdown("Used to accomplish the following: ")
st.markdown("""
1. Visualize the number of unique laptop models across different RAM sizes
2. Show the number of laptop models of different RAM sizes
""")
#word cloud for RAM sizes
def word_cloud():
# width=800 - sets the width of the word cloud image to 800 pixels
# height=400 - sets the height of the word cloud image to 400 pixels
# background_color='white' - sets the background color of the word cloud to white
# interpolation='bilinear' - uses bilinear interpolation to smooth the edges
# of the words in the displayed image.
# plt.axis('off') - hides the axis lines and labels from the plot
  counts = df['RAM (GB)'].value_counts()
  counts.index = counts.index.map(str)
  wordcloud = WordCloud(width=800, height=800, background_color="black", colormap="Pastel1").generate_from_frequencies(counts)
  plt.imshow(wordcloud, interpolation='bilinear')
  plt.axis('off')
  plt.title('Distribution of Unique Laptop Models Across Different RAM Sizes')
  plt.show()
  #syntax to show the chart on streamlit
  st.pyplot(plt)
  #This clears the elements of the previous graph, a must properly run graphs
  plt.clf()
  
word_cloud()




#Conlusions Area
st.markdown("## Conclusions:")
st.write("Insights from our graphs: ")
st.markdown("""
1. CPU Market Share


*   The CPU Company with the biggest market share is Intel with a 55.2% Market Share

2. Frequencies most provided by CPU companies


*   Intel's manufactured cpus tend to fall under the frequencies of 2.5, 2.7-2.8 GHz.

*   AMD's manufactured cpus tend to fall under the frequencies of 2.5 and 3.0 GHz.


3. Company Manufactured Laptops:


*   The company which produced the most amount of unique laptops was DELL, in which they had produced 291 unique laptops

*   There are very few laptops priced above 4000 euros, suggesting that the majority of consumers or manufacturers focus on lower to mid-range pricing.

* Laptops from the Razer manufacturer brand are the most expensive on average at around 3000 Euros, while brands like Chuwi, Vero, Mediacom, and Fujitsu are among the cheapest at the sub-1000 Euro range.

4. Laptop Price Trend

*   Companies tend to price their laptops within the range of 300 to 2000 Euros, with the most common pricing falling between 700-1000 Euros.

* The laptops priced around 6000 euros are extremely rare, suggesting these are premium or specialized models.

5. RAM Trends and Highlights

* There is a clear positive correlation between RAM size and laptop price. As the RAM size increases, the average price of laptops also rises. This suggests that higher RAM is associated with more expensive laptops.

* The price does not increase at a constant rate. There are certain points where the price jumps significantly. For example:

* From 16 GB to 32 GB, there is a sharp rise in average price, indicating that laptops with 32 GB of RAM are priced considerably higher than those with 16 GB.

* A similar steep increase occurs from 8 GB to 16 GB, showing another significant jump in pricing.


* Laptops with very low RAM (e.g., 4 GB or less) are the least expensive, with an average price under 500 euros. This indicates that laptops in this range are likely budget or entry-level models.


* The highest-priced laptops in this dataset appear to have 64 GB of RAM, with prices nearing 4000 euros on average. These would likely be specialized, premium models meant for tasks like high-end gaming, video editing, or scientific computing.

* Laptops models in the market most frequently have 4 to 16 GB of RAM, with 8 GB RAM being the most common of all. 64 GB RAM laptops on the other hand have the least number of unique laptop models.
""")
