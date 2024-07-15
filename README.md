<h1>Intel-Products-Sentiment-Analysis-from-Online-Reviews</h1>

<h2>Team Details: </h2>
<p><b>Team Name: </b>Brainiacs</p>
<b>Team Members: </b>
<ul>
<li>Ananya Dayanand Prabhu</li>
<li>Neha Vithob Nayak</li>
<li>Pooja S Doddagoudar</li>
</ul>
<p><b>Institute Name: </b>Shri Dharmasthala Manjunatheshwara College of Engineering and Technology, Dharwad.</p>
<h3> Problem Statement-11: </h3>
<u><b>Intel-Products-Sentiment-Analysis-from-Online-Reviews</b></u>

<h2> Description: </h2>
<p>Intel Products are reviewed by end users and tech reviewers on various platforms. 
Hence, we scraped the reviews available on different sources in the last 3 - 5 years. Applied
various exploratory data analysis, machine learning, and natural programming techniques to find the 
sentiments of products, clustering of affinity reviews, trends of sentiments over period, features 
and keywords extraction to specific sentiments, recommendation on key improvements based on 
users reviews for future products. Ensuring sentiments and any other analysis is also demonstrated on 
different product category.</p>

<h2> Outcomes: </h2>
<ul>
  <li>Models and outputs for above expected use cases along with performance metrics of each model.</li>
  <li>The data source, train and test data of project.</li>
  <li>Key Summary and Recommendation slides based on analysis and model outcomes .</li>
  <li><b><a href="">Report</a></b></li>
  <li><a href="">PPT</a></li>
</ul>

<h2>Implementation of the Intel Products Sentiment Analysis Project</h2>
<h3>1. Data Collection</h3>
<p>The project begins with collecting user reviews of Intel products from Amazon. Web scraping techniques are used to extract review data from multiple pages. The scraping process involves sending HTTP requests to Amazon pages, rendering JavaScript content using Splash, and parsing the HTML to locate review elements. Key data points such as review ratings and review body text are extracted and stored in a structured format.</p>
<h3>2. Data Preprocessing</h3>
<p>Once the data is collected, it undergoes preprocessing to prepare it for analysis. This includes cleaning the text data by removing HTML tags, special characters, and unnecessary whitespace. Additionally, we convert ratings to a numerical format and handle any missing or incomplete data. This step ensures that the data is in a consistent and usable format for subsequent analysis.</p>
<h3>3. Sentiment Analysis</h3>
<p>We perform sentiment analysis using two models: VADER and RoBERTa.

VADER (Valence Aware Dictionary and sEntiment Reasoner): This lexicon-based model is used for initial sentiment classification. It calculates sentiment scores (positive, negative, neutral, and compound) based on predefined word lists.
RoBERTa (Robustly optimized BERT approach): This transformer-based model is employed for more advanced sentiment analysis. It tokenizes the text and uses a pre-trained model to classify sentiments into categories (negative, neutral, and positive) with associated probabilities.
Both models' sentiment scores are combined to enhance accuracy and reliability. Each review is then assigned a final sentiment label based on the combined scores.</p>
<h3>4. Keyword Abstraction</h3>
<p>To extract important keywords from the reviews, we use two methods:

TF-IDF (Term Frequency-Inverse Document Frequency): Identifies the most significant words in the reviews.
RAKE (Rapid Automatic Keyword Extraction): Extracts key phrases and terms associated with different sentiment clusters.</p>
<h3>5. Exploratory Data Analysis (EDA)</h3>
<p>Exploratory Data Analysis involves visualizing and summarizing the collected data to identify patterns and trends. This includes:

Distribution of Ratings: Visualizing the frequency of each rating (1 to 5 stars) to understand overall customer satisfaction.
Sentiment Distribution: Analyzing the distribution of sentiment scores (positive, neutral, negative) across different ratings.</p>

<h2>Conclusion</h2>
<p>The Intel Products Sentiment Analysis Project successfully leveraged advanced NLP techniques to gain valuable insights from user reviews. By combining sentiment analysis, keyword abstraction, and exploratory data analysis, we provided a comprehensive understanding of customer sentiments and identified key areas for product improvement. The project highlighted the importance of monitoring customer feedback and continuously improving products to enhance customer satisfaction.</p>
