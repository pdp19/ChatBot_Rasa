# ChatBot_Rasa

An Indian startup named 'Foodie' wants to build a conversational bot (chatbot) which can help users discover restaurants across several Indian cities.

The main purpose of the bot is to help users discover restaurants quickly and efficiently and to provide a good restaurant discovery experience.

The bot takes the following inputs from the user:

 - City: Take the input from the customer as a text field. For example:
 - Bot: In which city are you looking for restaurants?
 - User: anywhere in Delhi

Chatbot will provide results for tier-1 and tier-2 cities only, while for tier-3 cities, it will reply back with something like "We do not operate in that area yet".

Cuisine Preference: 

 - Bot: What kind of cuisine would you prefer?
Chinese
Mexican
Italian
American
South Indian
North Indian
User: I’ll prefer Italian!
 
Average budget for two people: 

 - Bot: What price range are you looking at?
Lesser than Rs. 300
Rs. 300 to 700
More than 700
User: in range of 300 to 700

While showing the results to the user, the bot will display the top 5 restaurants in a sorted order (descending) of the average Zomato user rating (on a scale of 1-5, 5 being the highest).

Finally, the bot will ask the user whether he/she wants the details of the top 10 restaurants on email. If the user replies 'yes', the bot should ask for user’s email id and then send it over email. Else, just reply with a 'goodbye' message. The mail will have the following details for each restaurant:

Restaurant Name
Restaurant locality address
Average budget for two people
Zomato user rating
