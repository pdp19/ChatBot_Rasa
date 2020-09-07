<!-- ## complete path
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "delhi"}
    - slot{"location": "delhi"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - action_search_restaurants
    - slot{"location": "delhi"}
    - utter_goodbye
    - export

## location specified
* greet
    - utter_greet
* restaurant_search{"location": "delhi"}
    - slot{"location": "delhi"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - action_search_restaurants
* affirm
    - utter_goodbye
    - export

## complete path 2
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "delhi"}
    - slot{"location": "delhi"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "North Indian"}
    - slot{"cuisine": "North Indian"}
    - action_search_restaurants
    - utter_goodbye

## complete path 3
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "italy"}
    - slot{"location": "italy"}
	- utter_ask_cuisine
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - action_search_restaurants
* goodbye
    - utter_goodbye

## complete path 4
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "delhi"}
    - slot{"location": "delhi"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - action_search_restaurants
    - slot{"location": "delhi"}
    - export


## interactive_story_1
* greet
    - utter_greet
* restaurant_search{"location": "mumbai"}
    - slot{"location": "mumbai"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - action_search_restaurants
    - slot{"location": "mumbai"}
* stop

## interactive_story_1
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "mumbai"}
    - slot{"location": "mumbai"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "Italian"}
    - slot{"cuisine": "Italian"}
    - action_search_restaurants
    - slot{"location": "mumbai"}

## interactive_story_1
* greet
    - utter_greet
* restaurant_search{"cuisine": "chinese", "location": "delhi"}
    - slot{"cuisine": "chinese"}
    - slot{"location": "delhi"}
    - action_search_restaurants
    - slot{"location": "delhi"}
* affirm
    - utter_goodbye
    
    
## happy_path
* greet
    - utter_greet
* restaurant_search{"cuisine": "italian", "location": "mumbai"}
    - slot{"cuisine": "italian"}
    - slot{"location": "mumbai"}
    - action_search_restaurants
    - slot{"location": "mumbai"}
* affirm
    - utter_goodbye


## interactive_story_1
* greet
    - utter_greet
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - utter_ask_location
* restaurant_search{"location": "delhi"}
    - slot{"location": "delhi"}
    - action_search_restaurants
    - slot{"location": "delhi"}
* affirm
    - utter_goodbye

## interactive_story_1
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "mumbai"}
    - slot{"location": "mumbai"}
    - action_search_restaurants
    - slot{"location": "mumbai"}
* affirm
    - utter_goodbye
    - utter_goodbye
* goodbye
    - utter_greet

## interactive_story_1
* greet
    - utter_greet
* asking_general_questions
    - utter_asking_general_questions
* affirm{"location": "nayi dilli"}
    - slot{"location": "nayi dilli"}
    - utter_ask_cuisine
* restaurant_search
    - action_search_restaurants
    - slot{"location": "nayi dilli"}
* goodbye
    - utter_goodbye

## interactive_story_1
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "jaipur"}
    - slot{"location": "jaipur"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "South Indian"}
    - slot{"cuisine": "South Indian"}
    - utter_ask_price
* goodbye
    - action_search_restaurants
    - slot{"location": "jaipur"}
* affirm
    - utter_goodbye

## interactive_story_1
* greet
    - utter_greet
* restaurant_search{"location": "delhi"}
    - slot{"location": "delhi"}
    - utter_ask_cuisine
* restaurant_search
    - utter_ask_price
* goodbye
    - action_search_restaurants
    - slot{"location": "delhi"}
* affirm
    - utter_goodbye

## interactive_story_1
    - utter_ask_cuisine
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "noida"}
    - slot{"location": "noida"}
    - utter_ask_price
* goodbye
    - action_search_restaurants
    - slot{"location": "noida"}
* goodbye
    - utter_goodbye

## interactive_story_1
* greet
    - utter_greet
* restaurant_search{"location": "delhi"}
    - slot{"location": "delhi"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - utter_ask_price
* goodbye
    - action_search_restaurants
    - slot{"location": "delhi"}
* affirm
    - utter_goodbye

## interactive_story_1
    - slot{"location": "blore"}
    - slot{"cuisine": "chinese"}
    - slot{"location": "blore"}
* affirm
    - utter_goodbye

## interactive_story_1
* restaurant_search{"location": "delhi"}
    - slot{"location": "delhi"}
    - utter_ask_cuisine
* restaurant_search
    - utter_ask_price
* goodbye
    - action_search_restaurants
    - slot{"location": "delhi"}

## interactive_story_1
* restaurant_search{"location": "jaipur"}
    - slot{"location": "jaipur"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - utter_ask_price
* goodbye
    - action_search_restaurants

## interactive_story_1
* restaurant_search{"cuisine": "north indian", "location": "jaipur"}
    - slot{"cuisine": "north indian"}
    - slot{"location": "jaipur"}
    - action_search_restaurants
    - slot{"location": "jaipur"}

## interactive_story_1
    - slot{"cuisine": "mexica"}
    - slot{"location": "jaipur"}
    - slot{"location": "jaipur"}
* goodbye
    - utter_goodbye

## interactive_story_1
    - slot{"location": "delhi"}
    - slot{"cuisine": "chinese"}
* affirm
    - utter_goodbye
* goodbye

## interactive_story_1
    - slot{"location": "jaipur"}
    - slot{"cuisine": "chinese"}
    - slot{"location": "jaipur"}
    - action_send_email
* affirm
    - utter_goodbye

## interactive_story_1
    - slot{"cuisine": "mexican"}
    - slot{"location": "delhi"}
    - slot{"location": "delhi"}
* affirm
    - utter_goodbye

## interactive_story_1
* ask_for_email
    - utter_ask_for_email
* given_email{"email": "pradeep.comeng@gmail.com"}
    - slot{"email": "pradeep.comeng@gmail.com"}
    - action_send_email

## interactive_story_1
* ask_for_email
    - utter_ask_for_email
* given_email{"email": "pradeep.comeng@gmail.com"}
    - slot{"email": "pradeep.comeng@gmail.com"}
    - action_send_email
* affirm
    - utter_goodbye
* goodbye

## interactive_story_1
* ask_for_email
    - utter_ask_for_email
* given_email{"email": "pradeep.comeng@gmail.com"}
    - slot{"email": "pradeep.comeng@gmail.com"}
    - action_send_email

## interactive_story_1
* ask_for_email
    - utter_ask_for_email
* given_email{"email": "pradeep.comeng@gmail.com"}
    - slot{"email": "pradeep.comeng@gmail.com"}
    - action_send_email
* affirm
    - utter_goodbye

## interactive_story_1
    - slot{"email": "pradeep.comeng@gmail.com"}
* affirm
    - utter_goodbye

## interactive_story_1
* ask_for_email
    - utter_ask_for_email
* given_email{"email": "pradeep.pdp19@gmail.com"}
    - slot{"email": "pradeep.pdp19@gmail.com"}
    - action_send_email
* affirm
    - utter_goodbye

## interactive_story_1
* ask_for_email
    - utter_ask_for_email
* given_email{"email": "pradeep.comeng@gmail.com"}
    - slot{"email": "pradeep.comeng@gmail.com"}
    - action_send_email
* affirm
    - utter_goodbye
* goodbye

## interactive_story_1
* ask_for_email
    - utter_ask_for_email
* given_email{"email": "pradeep.pdp19@gmail.com"}
    - slot{"email": "pradeep.pdp19@gmail.com"}
    - action_send_email
    - action_send_email

## interactive_story_1
* ask_for_email
    - utter_ask_for_email
* given_email{"email": "pradeep.pdp19@gmail.com"}
    - slot{"email": "pradeep.pdp19@gmail.com"}
    - action_send_email

## interactive_story_1
* ask_for_email
    - utter_ask_for_email
* given_email{"email": "pradeep.pdp19@gmail.com"}
    - slot{"email": "pradeep.pdp19@gmail.com"}
    - action_send_email

## interactive_story_1
* ask_for_email
    - utter_ask_for_email
* given_email{"email": "pradeep.pdp19@gmail.com"}
    - slot{"email": "pradeep.pdp19@gmail.com"}
    - action_send_email

## interactive_story_1
* ask_for_email
    - utter_ask_for_email
* given_email{"email": "pradeep.pdp19@gmail.com"}
    - slot{"email": "pradeep.pdp19@gmail.com"}
    - action_send_email

## interactive_story_1
* ask_for_email
    - utter_ask_for_email
* given_email{"email": "pradeep.pdp19@gmail.com"}
    - slot{"email": "pradeep.pdp19@gmail.com"}
    - action_send_email
* affirm
    - utter_goodbye
* goodbye

## interactive_story_1
* ask_for_email
    - utter_ask_for_email
* given_email{"email": "pradeep.comeng@gmail.com"}
    - slot{"email": "pradeep.comeng@gmail.com"}
    - action_send_email

## interactive_story_1
* ask_for_email
    - utter_ask_for_email
* given_email{"email": "pradeep.pdp19@gmail.com"}
    - slot{"email": "pradeep.pdp19@gmail.com"}
    - action_send_email

## interactive_story_1
* ask_for_email
    - utter_ask_for_email
* given_email{"email": "pradeep.pdp19@gmail.com"}
    - slot{"email": "pradeep.pdp19@gmail.com"}
    - action_send_email

## interactive_story_2
* greet
    - utter_greet
* restaurant_search{"location": "jaipur"}
    - slot{"location": "jaipur"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - utter_ask_price
* select_price
    - action_search_restaurants
    - slot{"location": "jaipur"}
    - utter_ask_for_top_10_restaurent
* affirm
    - utter_ask_for_email
* given_email{"email": "pradeep.pdp19@gmail.com"}
    - slot{"email": "pradeep.pdp19@gmail.com"}
    - action_send_email
* affirm
    - utter_goodbye
* goodbye

## interactive_story_1
* restaurant_search{"location": "delhi", "cuisine": "north indian"}
    - slot{"cuisine": "north indian"}
    - slot{"location": "delhi"}
    - utter_ask_price
* select_price
    - action_search_restaurants
    - utter_ask_for_top_10_restaurent
* given_email{"email": "pradeep.pdp19@gmail.com"}
    - slot{"email": "pradeep.pdp19@gmail.com"}
    - action_send_email
* affirm
    - utter_goodbye
* goodbye

## interactive_story_1
* restaurant_search{"cuisine": "south indian", "location": "jaipur"}
    - slot{"cuisine": "south indian"}
    - slot{"location": "jaipur"}
    - action_search_restaurants

## interactive_story_1
* restaurant_search{"cuisine": "south indian", "location": "delhi"}
    - slot{"cuisine": "south indian"}
    - slot{"location": "delhi"}
    - utter_ask_price
* goodbye{"price": "Lesser_300"}
    - slot{"price": "Lesser_300"}
    - action_search_restaurants

## interactive_story_1
* restaurant_search{"location": "delhi", "cuisine": "south indian"}
    - slot{"cuisine": "south indian"}
    - slot{"location": "delhi"}
    - utter_ask_price
* select_price{"price": "Lesser_300"}
    - slot{"price": "Lesser_300"}
    - action_search_restaurants

## interactive_story_1
* restaurant_search{"cuisine": "american", "location": "delhi"}
    - slot{"cuisine": "american"}
    - slot{"location": "delhi"}
    - utter_ask_price
* goodbye{"price": "Lesser_300"}
    - slot{"price": "Lesser_300"}
    - action_search_restaurants

## interactive_story_1
* restaurant_search{"cuisine": "american", "location": "delhi"}
    - slot{"cuisine": "american"}
    - slot{"location": "delhi"}
    - utter_ask_price
* goodbye{"price": "Lesser_300"}
    - slot{"price": "Lesser_300"}
    - action_search_restaurants

## interactive_story_1
* restaurant_search{"cuisine": "indian", "location": "delhi"}
    - slot{"cuisine": "indian"}
    - slot{"location": "delhi"}
    - utter_ask_price
* goodbye{"price": "Lesser_300"}
    - slot{"price": "Lesser_300"}
    - action_search_restaurants

## interactive_story_1
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "jaipur"}
    - slot{"location": "jaipur"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - utter_ask_price
* select_price{"price": "Lesser_300"}
    - slot{"price": "Lesser_300"}
    - action_search_restaurants

## interactive_story_1
* restaurant_search{"location": "delhi"}
    - slot{"location": "delhi"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - utter_ask_price
* goodbye{"price": "Lesser_300"}
    - slot{"price": "Lesser_300"}
    - action_search_restaurants

## interactive_story_1
* restaurant_search{"cuisine": "north indian", "location": "jaipur"}
    - slot{"cuisine": "north indian"}
    - slot{"location": "jaipur"}
    - utter_ask_price
* select_price{"price": "In_Between_300_To_700"}
    - slot{"price": "In_Between_300_To_700"}
    - action_search_restaurants

## interactive_story_1
* restaurant_search{"cuisine": "american"}
    - slot{"cuisine": "american"}
    - utter_ask_location
* restaurant_search{"location": "delhi"}
    - slot{"location": "delhi"}
    - utter_ask_price
* goodbye{"price": "Lesser_300"}
    - slot{"price": "Lesser_300"}
    - action_search_restaurants

## interactive_story_1
* restaurant_search{"cuisine": "chinese", "location": "jaipur"}
    - slot{"cuisine": "chinese"}
    - slot{"location": "jaipur"}
    - utter_ask_price
* goodbye{"price": "Lesser_300"}
    - slot{"price": "Lesser_300"}
    - action_search_restaurants

## interactive_story_1
* restaurant_search{"cuisine": "american", "location": "jaipur"}
    - slot{"cuisine": "american"}
    - slot{"location": "jaipur"}
    - utter_ask_price
* goodbye{"price": "Lesser_300"}
    - slot{"price": "Lesser_300"}
    - action_search_restaurants

## interactive_story_1
* restaurant_search{"cuisine": "north indian", "location": "jaipur"}
    - slot{"cuisine": "north indian"}
    - slot{"location": "jaipur"}
    - utter_ask_price
* select_price{"price": "In_Between_300_To_700"}
    - slot{"price": "In_Between_300_To_700"}
    - action_search_restaurants

## interactive_story_1
* restaurant_search{"location": "chennai"}
    - slot{"location": "chennai"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "South Indian"}
    - slot{"cuisine": "South Indian"}
    - utter_ask_price
* select_price{"price": "In_Between_300_To_700"}
    - slot{"price": "In_Between_300_To_700"}
    - action_search_restaurants
    - slot{"location": "chennai"}

## interactive_story_1
* restaurant_search{"cuisine": "north indian", "location": "jaipur"}
    - slot{"cuisine": "north indian"}
    - slot{"location": "jaipur"}
    - utter_ask_price
* goodbye{"price": "Lesser_300"}
    - slot{"price": "Lesser_300"}
    - action_search_restaurants
    - slot{"location": "jaipur"}

## interactive_story_1
* restaurant_search{"cuisine": "north indain", "location": "bangalore"}
    - slot{"cuisine": "north indain"}
    - slot{"location": "bangalore"}
    - utter_ask_price
* goodbye{"price": "Greater_300"}
    - slot{"price": "Greater_300"}
    - action_search_restaurants
    - slot{"location": "bangalore"}

## interactive_story_1
* restaurant_search{"location": "bangalore", "cuisine": "south indian"}
    - slot{"cuisine": "south indian"}
    - slot{"location": "bangalore"}
    - utter_ask_price
* goodbye{"price": "Greater_300"}
    - slot{"price": "Greater_300"}
    - action_search_restaurants
    - slot{"location": "bangalore"}
* affirm
    - utter_ask_for_top_10_restaurent
* affirm
    - utter_ask_for_email
* given_email{"email": "pradeep.pdp19@gmail.com"}
    - slot{"email": "pradeep.pdp19@gmail.com"}
    - action_send_email
* affirm
    - utter_goodbye
* goodbye

## interactive_story_1
* restaurant_search{"cuisine": "north indain", "location": "bangalore"}
    - slot{"cuisine": "north indain"}
    - slot{"location": "bangalore"}
    - utter_ask_price
* goodbye{"price": "Greater_300"}
    - slot{"price": "Greater_300"}
    - action_search_restaurants

* affirm
    - utter_ask_for_top_10_restaurent
* affirm
    - utter_ask_for_email
* given_email{"email": "pradeep.pdp19@gmail.com"}
    - slot{"email": "pradeep.pdp19@gmail.com"}
    - action_send_email
* affirm
    - utter_goodbye
* goodbye

## interactive_story_1
* restaurant_search{"cuisine": "north indain", "location": "bangalore"}
    - slot{"cuisine": "north indain"}
    - slot{"location": "bangalore"}
    - utter_ask_price
* goodbye{"price": "Greater_300"}
    - slot{"price": "Greater_300"}
    - action_search_restaurants
    - slot{"location": "bangalore"}
* affirm
    - utter_ask_for_top_10_restaurent
* affirm
    - utter_ask_for_email
* given_email{"email": "pradeep.pdp19@gmail.com"}
    - slot{"email": "pradeep.pdp19@gmail.com"}
    - action_send_email

## interactive_story_1
* ask_for_email
    - utter_ask_for_email
* given_email{"email": "pradeep.pdp19@gmail.com"}
    - slot{"email": "pradeep.pdp19@gmail.com"}
    - action_send_email

## interactive_story_1
* restaurant_search{"location": "mumbai"}
    - slot{"location": "mumbai"}
    - utter_ask_cuisine
* restaurant_search
    - utter_ask_price
* goodbye{"price": "Greater_300"}
    - slot{"price": "Greater_300"}
    - action_search_restaurants
    - slot{"location": "mumbai"}
* affirm
    - utter_ask_for_top_10_restaurent
* affirm
    - utter_ask_for_email
* given_email{"email": "pradeep.pdp19@gmail.com"}
    - slot{"email": "pradeep.pdp19@gmail.com"}
    - action_send_email
* affirm
    - utter_goodbye
* goodbye

## interactive_story_1
* ask_for_email
    - utter_ask_for_email
* given_email{"email": "pradeep.pdp19@gmail.com"}
    - slot{"email": "pradeep.pdp19@gmail.com"}
    - action_send_email

## interactive_story_1
* restaurant_search{"location": "delhi"}
    - slot{"location": "delhi"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - utter_ask_price
* goodbye{"price": "Greater_300"}
    - slot{"price": "Greater_300"}
    - action_search_restaurants
* affirm
    - utter_ask_for_top_10_restaurent
* affirm
    - utter_ask_for_email
* given_email{"email": "pradeep.pdp19@gmail.com"}
    - slot{"email": "pradeep.pdp19@gmail.com"}
    - action_send_email
* affirm
    - utter_goodbye
* goodbye

## interactive_story_1
* restaurant_search{"location": "bangalore"}
    - slot{"location": "bangalore"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - utter_ask_price
* goodbye{"price": "Greater_300"}
    - slot{"price": "Greater_300"}
    - action_search_restaurants
* affirm
    - utter_ask_for_top_10_restaurent
* negative
    - utter_goodbye
* goodbye
    - action_restart

## interactive_story_1
* greet
    - utter_greet
* asking_general_questions
    - utter_asking_general_questions
* affirm
    - utter_ask_howcanhelp
* restaurant_search{"location": "hyderabad"}
    - slot{"location": "hyderabad"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "South Indian"}
    - slot{"cuisine": "South Indian"}
    - utter_ask_price
* goodbye{"price": "Greater_300"}
    - slot{"price": "Greater_300"}
    - action_search_restaurants
* affirm
    - utter_ask_for_top_10_restaurent
* negative
    - utter_goodbye
    - action_restart

## interactive_story_1
* asking_general_questions
    - utter_asking_general_questions
* restaurant_search{"location": "mangalore"}
    - slot{"location": "mangalore"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "North Indian"}
    - slot{"cuisine": "North Indian"}
    - action_search_restaurants
* affirm
    - utter_ask_for_top_10_restaurent
* affirm
    - utter_ask_for_email
* given_email{"email": "dfd34434"}
    - slot{"email": "dfd34434"}
    - action_send_email

## interactive_story_1
* greet
    - utter_greet
* restaurant_search{"location": "sikar"}
    - slot{"location": "sikar"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "Italian"}
    - slot{"cuisine": "Italian"}
    - utter_ask_price
* select_price{"price": "In_Between_300_To_700"}
    - slot{"price": "In_Between_300_To_700"}
    - action_search_restaurants
* affirm
    - utter_ask_for_top_10_restaurent
* affirm
    - utter_ask_for_email
* given_email{"email": "pradeppp"}
    - slot{"email": "pradeppp"}
    - action_send_email
* given_email{"email": "pradeep.comeng@gmail.com"}
    - slot{"email": "pradeep.comeng@gmail.com"}
    - action_send_email
* affirm
    - utter_goodbye
* goodbye
    - action_restart

## interactive_story_1
* restaurant_search{"location": "kota"}
    - slot{"location": "kota"}
    - action_check_location
    - slot{"location": "kota"}
    - utter_ask_cuisine
    - utter_ask_price
* select_price{"price": "In_Between_300_To_700"}
    - slot{"price": "In_Between_300_To_700"}
    - utter_ask_price
* select_price{"price": "In_Between_300_To_700"}
    - slot{"price": "In_Between_300_To_700"}
    - action_search_restaurants
* affirm
    - utter_ask_for_top_10_restaurent
* affirm
    - utter_ask_for_email
* given_email{"email": "santhumary@gmail.com"}
    - slot{"email": "santhumary@gmail.com"}
    - action_send_email
* affirm
    - utter_goodbye
    - action_restart

## interactive_story_1
* greet
    - utter_greet
* restaurant_search{"location": "sikar"}
    - slot{"location": "sikar"}
    - action_check_location
    - slot{"location": null}
    - utter_ask_cuisine
    - utter_ask_price
* goodbye{"price": "Lesser_300"}
    - slot{"price": "Lesser_300"}
    - utter_ask_price
* goodbye{"price": "Lesser_300"}
    - slot{"price": "Lesser_300"}
    - action_search_restaurants
* affirm
    - utter_ask_for_top_10_restaurent
* ask_for_email
    - utter_ask_for_email
* given_email{"email": "sdfdfgdfgfdddf"}
    - slot{"email": "sdfdfgdfgfdddf"}
    - action_send_email
* given_email{"email": "bobmusgrav1993@gmail.com"}
    - slot{"email": "bobmusgrav1993@gmail.com"}
    - action_send_email
* affirm
    - utter_goodbye
    - action_restart

## interactive_story_1
* greet
    - utter_greet
* restaurant_search{"location": "srimadhopur"}
    - slot{"location": "srimadhopur"}
    - action_check_location
    - slot{"location": null}
    - action_restart


## interactive_story_1
* greet
    - utter_greet
* restaurant_search{"location": "gachibolli"}
    - slot{"location": "gachibolli"}
    - action_check_location
    - slot{"location": null}
    - action_restart

## interactive_story_1
* greet
    - utter_greet
* ask_for_email
    - utter_ask_for_email
* given_email{"email": "abc.test001@test.com"}
    - slot{"email": "abc.test001@test.com"}
    - action_send_email
* affirm
    - utter_goodbye
* goodbye
    - action_restart

## interactive_story_1
* greet
    - utter_greet
* restaurant_search{"location": "bangalore"}
    - slot{"location": "bangalore"}
    - action_check_location
    - slot{"location": "bangalore"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - utter_ask_price
* select_price{"price": "In_Between_300_To_700"}
    - slot{"price": "In_Between_300_To_700"}
    - action_search_restaurants
* affirm
    - utter_ask_for_top_10_restaurent
* given_email{"email": "abc.test003@gmail.com"}
    - slot{"email": "abc.test003@gmail.com"}
    - action_send_email
* affirm
    - utter_goodbye
    - action_restart -->

<!-- ## interactive_story_1
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "niwai"}
    - slot{"location": "niwai"}
    - action_check_location
    - slot{"location": null}
    - action_restart   -->


## interactive_story_1
* greet
    - utter_greet
* restaurant_search{"location": "delhi"}
    - slot{"location": "delhi"}
    - action_check_location
    - slot{"location": "delhi"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "North Indian"}
    - slot{"cuisine": "North Indian"}
    - utter_ask_price
* select_price{"price": "In_Between_300_To_700"}
    - slot{"price": "In_Between_300_To_700"}
    - action_search_restaurants
    - utter_ask_for_top_10_restaurent
* given_email{"email": "abs.test0034@abc.com"}
    - slot{"email": "abs.test0034@abc.com"}
    - action_send_email
* affirm
    - utter_goodbye
    - action_restart

## interactive_story_1
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "jaipur"}
    - slot{"location": "jaipur"}
    - action_check_location
    - slot{"location": "jaipur"}
    - utter_ask_cuisine
* restaurant_search
    - utter_ask_price
* select_price{"price": "In_Between_300_To_700"}
    - slot{"price": "In_Between_300_To_700"}
    - action_search_restaurants
    - utter_ask_for_top_10_restaurent
* affirm
    - utter_ask_for_email
* given_email{"email": "pradeep.pdp19@gmail.com"}
    - slot{"email": "pradeep.pdp19@gmail.com"}
    - action_valid_email_id
    - slot{"email": "pradeep.pdp19@gmail.com"}
    - action_send_email
* affirm
    - utter_goodbye
    - action_restart

## interactive_story_1
* greet
    - utter_greet
* restaurant_search{"location": "Rishikesh"}
    - slot{"location": "Rishikesh"}
    - action_check_location
    - slot{"location": null}
* restaurant_search{"location": "jaipur"}
    - slot{"location": "jaipur"}
    - action_check_location
    - slot{"location": "jaipur"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - utter_ask_price
* select_price{"price": "In_Between_300_To_700"}
    - slot{"price": "In_Between_300_To_700"}
    - action_search_restaurants
    - utter_ask_for_top_10_restaurent
* affirm
    - utter_ask_for_email
* given_email{"email": "abc.dpdp119@gmail.com"}
    - slot{"email": "abc.dpdp119@gmail.com"}
    - action_valid_email_id
    - action_send_email
* affirm
    - utter_goodbye
    - action_restart

## interactive_story_1
* greet
    - utter_greet
* restaurant_search{"location": "kolkata"}
    - slot{"location": "kolkata"}
    - action_check_location
    - slot{"location": "kolkata"}
    - utter_ask_cuisine
* restaurant_search
    - utter_ask_price
* select_price{"price": "In_Between_300_To_700"}
    - slot{"price": "In_Between_300_To_700"}
    - action_search_restaurants
    - utter_ask_for_top_10_restaurent
* affirm
    - utter_ask_for_email
* given_email{"email": "asdsf@test.com"}
    - slot{"email": "asdsf@test.com"}
    - action_valid_email_id
    - slot{"email": "asdsf@test.com"}
    - action_send_email
* affirm
    - utter_goodbye
    - action_restart

<!-- ## interactive_story_1
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "gurugrram"}
    - slot{"location": "gurugrram"}
    - action_check_location
    - slot{"location": null}
* restaurant_search{"location": "gurugram"}
    - slot{"location": "gurugram"}
    - action_check_location
    - slot{"location": null}
* restaurant_search{"location": "Gurgaon"}
    - slot{"location": "Gurgaon"}
    - action_check_location
    - slot{"location": "Gurgaon"}
    - utter_ask_cuisine
* restaurant_search
    - utter_ask_price
* select_price{"price": "Greater_300"}
    - slot{"price": "Greater_300"}
    - utter_ask_for_top_10_restaurent
* affirm
    - utter_ask_for_email
* given_email{"email": "xuhv.sff@test.com"}
    - slot{"email": "xuhv.sff@test.com"}
    - action_valid_email_id
    - slot{"email": "xuhv.sff@test.com"}
    - action_send_email
* affirm
    - utter_goodbye
    - action_restart -->

## interactive_story_1
* greet
    - utter_greet
* restaurant_search{"cuisine": "chinese", "location": "chandigarh"}
    - slot{"cuisine": "chinese"}
    - slot{"location": "chandigarh"}
    - action_check_location
    - slot{"location": "chandigarh"}
    - utter_ask_price
* select_price{"price": "Greater_300"}
    - slot{"price": "Greater_300"}
    - action_search_restaurants
    - utter_ask_for_top_10_restaurent
* negative
    - utter_goodbye
    - action_restart

## interactive_story_1
* greet
    - utter_greet
* restaurant_search{"location": "jaipur"}
    - slot{"location": "jaipur"}
    - action_check_location
    - slot{"location": "jaipur"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "Italian"}
    - slot{"cuisine": "Italian"}
    - utter_ask_price
* select_price{"price": "Greater_300"}
    - slot{"price": "Greater_300"}
    - action_search_restaurants
    - utter_ask_for_top_10_restaurent
* affirm
    - utter_ask_for_email
* given_email{"email": "fgfg.232@fd"}
    - slot{"email": "fgfg.232@fd"}
    - action_valid_email_id
    - slot{"email": null}
* given_email{"email": "asdftest.com"}
    - slot{"email": "asdftest.com"}
    - action_valid_email_id
    - slot{"email": null}
    - action_valid_email_id
    - slot{"email": null}
* given_email{"email": "praddd.sss@ffdd.com"}
    - slot{"email": "praddd.sss@ffdd.com"}
    - action_valid_email_id
    - slot{"email": "praddd.sss@ffdd.com"}
    - action_send_email
* affirm
    - utter_goodbye
    - action_restart

## interactive_story_1
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "kota"}
    - slot{"location": "kota"}
    - action_check_location
    - slot{"location": "kota"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "South Indian"}
    - slot{"cuisine": "South Indian"}
    - utter_ask_price
* select_price{"price": "In_Between_300_To_700"}
    - slot{"price": "In_Between_300_To_700"}
    - action_search_restaurants
    - utter_ask_for_top_10_restaurent
* negative
    - utter_goodbye
    - action_restart

## interactive_story_1
* greet
    - utter_greet
* asking_general_questions
    - utter_asking_general_questions
* ask_for_email
    - utter_ask_for_email
* given_email{"email": "pradeep.comeng@gmail.com"}
    - slot{"email": "pradeep.comeng@gmail.com"}
    - action_valid_email_id
    - slot{"email": "pradeep.comeng@gmail.com"}
    - action_valid_email_id
    - action_send_email
* affirm
    - utter_goodbye
    - action_restart

## interactive_story_1
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "delhi"}
    - slot{"location": "delhi"}
    - action_check_location
    - slot{"location": "delhi"}
    - utter_ask_cuisine
* restaurant_search
    - utter_ask_price
* select_price{"price": "Lesser_300"}
    - slot{"price": "Lesser_300"}
    - action_search_restaurants
    - utter_ask_for_top_10_restaurent
* negative
    - utter_goodbye
    - action_restart

## interactive_story_1
* greet
    - utter_greet
* restaurant_search{"location": "delhi"}
    - slot{"location": "delhi"}
    - action_check_location
    - slot{"location": "delhi"}
    - utter_ask_cuisine
* restaurant_search
    - utter_ask_price
* select_price{"price": "In_Between_300_To_700"}
    - slot{"price": "In_Between_300_To_700"}
    - action_search_restaurants
    - utter_ask_for_top_10_restaurent
* given_email{"email": "pradeep.pdp19@gmail.com"}
    - slot{"email": "pradeep.pdp19@gmail.com"}
    - action_valid_email_id
    - slot{"email": "pradeep.pdp19@gmail.com"}
    - action_valid_email_id
    - action_send_email
* affirm
    - utter_goodbye
    - action_restart

## interactive_story_1
* greet
    - utter_greet
* asking_general_questions
    - utter_asking_general_questions
* restaurant_search{"cuisine": "american", "location": "bangalore"}
    - slot{"cuisine": "american"}
    - slot{"location": "bangalore"}
    - action_check_location
    - slot{"location": "bangalore"}
    - utter_ask_price
* select_price{"price": "Greater_300"}
    - slot{"price": "Greater_300"}
    - action_search_restaurants
    - utter_ask_for_top_10_restaurent
* negative
    - utter_goodbye
    - action_restart

## interactive_story_1
* greet
    - utter_greet
* asking_general_questions
    - utter_asking_general_questions
* restaurant_search{"cuisine": "north indian"}
    - slot{"cuisine": "north indian"}
    - utter_ask_location
* restaurant_search{"location": "delhi"}
    - slot{"location": "delhi"}
    - action_check_location
    - slot{"location": "delhi"}
    - utter_ask_price
* select_price{"price": "In_Between_300_To_700"}
    - slot{"price": "In_Between_300_To_700"}
    - action_search_restaurants
    - utter_ask_for_top_10_restaurent
* negative
    - utter_goodbye
    - action_restart

## interactive_story_1
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "mumbai"}
    - slot{"location": "mumbai"}
    - action_check_location
    - slot{"location": "mumbai"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "Italian"}
    - slot{"cuisine": "Italian"}
    - utter_ask_price
* select_price{"price": "Lesser_300"}
    - slot{"price": "Lesser_300"}
    - action_search_restaurants
    - utter_ask_for_top_10_restaurent
* affirm
    - utter_ask_for_email
* given_email{"email": "dfdfd@dgfdg.com"}
    - slot{"email": "dfdfd@dgfdg.com"}
    - action_valid_email_id
    - slot{"email": "dfdfd@dgfdg.com"}
    - action_valid_email_id
    - action_send_email
* affirm
    - utter_goodbye
    - action_restart
## interactive_story_1
* greet
    - utter_greet
* restaurant_search{"cuisine": "north indian"}
    - slot{"cuisine": "north indian"}
    - utter_ask_location
* restaurant_search{"location": "delhi"}
    - slot{"location": "delhi"}
    - action_check_location
    - slot{"location": "delhi"}
    - utter_ask_price
* select_price{"price": "In_Between_300_To_700"}
    - slot{"price": "In_Between_300_To_700"}
    - action_search_restaurants
    - utter_ask_for_top_10_restaurent
* affirm
    - utter_ask_for_email
* given_email{"email": "pradee.sds@dfdf.com"}
    - slot{"email": "pradee.sds@dfdf.com"}
    - action_valid_email_id
    - slot{"email": "pradee.sds@dfdf.com"}
    - action_valid_email_id
    - action_send_email
* affirm
    - utter_goodbye
    - action_restart

## interactive_story_1
* greet
    - utter_greet
* restaurant_search{"cuisine": "north indian"}
    - slot{"cuisine": "north indian"}
    - utter_ask_location
* restaurant_search{"location": "delhi"}
    - slot{"location": "delhi"}
    - action_check_location
    - slot{"location": "delhi"}
    - utter_ask_price
* select_price{"price": "In_Between_300_To_700"}
    - slot{"price": "In_Between_300_To_700"}
    - action_search_restaurants
    - utter_ask_for_top_10_restaurent
* affirm
    - utter_ask_for_email
* given_email{"email": "pradee.sds@dfdf.com"}
    - slot{"email": "pradee.sds@dfdf.com"}
    - action_valid_email_id
    - slot{"email": "pradee.sds@dfdf.com"}
    - action_valid_email_id
    - action_send_email
* affirm
    - utter_goodbye
    - action_restart
