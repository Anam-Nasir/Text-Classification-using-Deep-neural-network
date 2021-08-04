# Codefundo 2018
  
 Implemented a system which can categorize or classify a textual data using Deep Neural Network Model trained using Google Tensorflow.  
 
## Text Classification

Text Classification is the task of assigning the right label to a given piece of text. This text can either be a phrase, a sentence or even a paragraph. Our aim would be to take in some text as input and attach or assign a label to it. Since we will be using tensorFlow Is deep learning library, we can call this the tensorflow text classification system. 

<br>

<p align="center">
 <img src = "txt-classifier2.png">
</p> 

<br>

## Some NLP terminologies

Natural Language Processing (NLP) is heavily being used in our text classification task. So, before we begin, I want to cover a few terms and concepts that we will be using. This will help you understand why a particular function or process is being called or at the very least clear any confusion you might have.

I) Stemming – Stemming is a process applied to a single word to derive its root. Many words that are being used in a sentence are often inflected or derived. To standardize our process, we would like to stem such words and end up with only root words. For example, a stemmer will convert the following words “walking”, “walked”, “walker” to its root word “walk“.

II) Tokenization – Tokens are basically words. This is a process of taking in a piece of text and find out all the unique words in the text. We would get a list of words in the text as the output of tokens.

For example, for the sentence “Python NLP is just going great” we have the token list [ “Python”, “NLP”, ïs”, “just”, “going”, “great”]. So, as you can see, tokenization involves breaking up the text into words.

III) Bag of Words – The Bag of Words model in Text Processing is the process of creating a unique list of words. This model is used as a tool for feature generation.

Eg: consider two sentences:

Star Wars is better than Star Trek.
Star Trek isn’t as good as Star Wars.
For the above two sentences, the bag of words will be: [“Star”, “Wars”, “Trek”, “better”, “good”, “isn’t”, “is”, “as”].

The position of each word in the list is hence fixed. Now, to construct a feature for classification from a sentence, we use a binary array ( an array where each element can either be 1 or 0).

For example, a new sentence, “Wars is good” will be represented as [0,1,0,0,1,0,1,0] . As you can see in the array, position 2 is set to 1 because the word in position 2 is “wars” in the bag of words which is also present in our example sentence. This same holds good for the other words “is” and “good” as well. You can read more about the Bag of Words model [here](https://ongspxm.gitlab.io/blog/2014/12/bag-of-words-natural-language-processing/).

## Step 1: Data Preparation

Before we train a model that can classify a given text to a particular category, we have to first prepare the data. We can create a simple JSON file that will hold the required data for training.

 We are using a dataset of 2014_India_floods which contains tweets from twitter as text and its assigned category. In this dataset we are having 9 different categories regarding natural disaster. We will be having a JSON with 9 categories. For each category, we have a set of sentences which we can use to train our model.

Given this data, we have to classify any given sentence into one of these 9 categories.

## Step 2: Data Load and Pre-processing

We will be creating multiple lists and each list “words” will hold all the unique stemmed words in all the sentences provided for training. Another list “categories” holds all the different categories.

The output of this step is the list which contains the words from each sentence and which category the sentence belongs. An example document is ([“whats”, “your”, “age”], “age”).

## Step 3: Convert the data to Tensorflow Specification

From the previous step, we have documents but they are still in the text form. Tensorflow being a math library accepts the data in the numeric form. So, before we begin with the tensorflow text classification, we take the text form and apply the bag of words model to convert the sentence into a numeric binary array. We then store the labels/category, in the same way, that is a numeric binary array.

## Step 4: Initiate Tensorflow Text Classification

With the documents in the right form, we can now begin the tensorflow text classification. In this step, we build a simple Deep Neural Network and use that for training our model.The code runs for a 100 epochs with a batch size of 20 and it took around 2 hours to finish training.

The size of data and the type of GPU heavily determine the time taken for training.

## Step 5: Testing the Tensorflow Text Classification Model

We can now test the neural network text classification python model. The model was able to correctly classify almost all the sentences. There will definitely be a lot of sentences that might fail to be classified correctly. This is only because the amount of data is less. with more and more data, you can be assured the model will be more confident.

## Conclusion

This is how you can perform tensorflow text classification. You can use this approach and scale it to perform a lot of different classification. You can use it to build chatbots as well.

## How users can get started with the project

NGO's, organisations etc can get categorical tweets from our project which can help them to get different informations like information regarding infrastructure damage, no. of deaths etc. So, this project can help them to figure out current situation and take decision accordingly.

## Dataset used

We are using dataset of the 2014 India Floods.

## Technologies used
1. Python
2. Information Retrieval
3. Natural Language Processing
4. Deep learning
5. Tensorflow
6. NLTK

## Video Link
https://www.youtube.com/watch?v=eoFKlHBbSXo
