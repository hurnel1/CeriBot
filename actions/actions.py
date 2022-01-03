# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"

from typing import Any, Text, Dict, List
#
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher


#import  actions.sqlite  as sqlite 
import actions.sqlite as sqlite
#from sqlite import select_schedule
#from sqlite import select_description



#import requests , json


#
#
class ActionHelloWorld(Action):

    def name(self) -> Text:
        return "action_hello_world"
#
    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
#
        dispatcher.utter_message(text="Hello World!")
#
        return []


class ActionSchedule(Action):

     def name(self) -> Text:
        return "action_schedule"

     def run(self, dispatcher: CollectingDispatcher,
             tracker: Tracker,
             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        section = tracker.get_slot('section')
        group = tracker.get_slot('group')

        #dispatcher.utter_message(text="/EXAMPLE/ Your next schedule is Math in room S2")
        #dispatcher.utter_message(text="Section = {}  Group = {}".format(section, group))

        print(sqlite.select_schedule(tracker.get_slot("section"),tracker.get_slot("group")))
        text="Votre prochain cours est :{}".format(sqlite.select_schedule(tracker.get_slot("section"),tracker.get_slot("group")))
        dispatcher.utter_message(text)

        """section = tracker.get_slot('section')
        group = tracker.get_slot('group')

        dispatcher.utter_message(text="/EXAMPLE/ Your next schedule is Math in room S2")
        dispatcher.utter_message(text="Section = {}  Group = {}".format(section, group))"""
	
 



        return []



class ActionTeacher(Action):

     def name(self) -> Text:
        return "action_teacher"

     def run(self, dispatcher: CollectingDispatcher,
             tracker: Tracker,
             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        #section = tracker.get_slot('section')
        #group = tracker.get_slot('group')

        #dispatcher.utter_message(text="/EXAMPLE/ Your next schedule is Math in room S2")
        #dispatcher.utter_message(text="Section = {}  Group = {}".format(section, group))
        request_type = tracker.get_slot("request_type")
        data = tracker.get_slot("data")
        print('data : {} request :  {}'.format(data, request_type))
        if request_type and not data : 
                if "nom" in request_type.lower() : 
                        dispatcher.utter_message("Quel est le nom du prof ?")


                elif "cours" in request_type.lower():
                        dispatcher.utter_message("Quel cours ?")
                else:
                        dispatcher.utter_message("j'ai besoin de votre message !")
        else :
                if "nom" in request_type.lower() : 
                        l = sqlite.select_by_name(data)
                        dispatcher.utter_message(display(l)  )

                        

                        

                elif "cours" in request_type.lower():
                        dispatcher.utter_message()
                        l = sqlite.select_by_course(data)

                        dispatcher.utter_message(display(l)  )
                else:
                        dispatcher.utter_message(sqlite.send_message(data))
                        dispatcher.utter_message("Le message envoyé est : {}".format(data))


                

        #print(select_data(tracker.get_slot("section"),tracker.get_slot("group")))

        return []




class ActionRoom(Action):

     def name(self) -> Text:
        return "action_rooms"

     def run(self, dispatcher: CollectingDispatcher,
             tracker: Tracker,
             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        nom_salles = tracker.get_slot('salle')
        #description = tracker.get_slot('description')

        #dispatcher.utter_message(text="/EXAMPLE/ Your next schedule is Math in room S2")
        #dispatcher.utter_message(text="nom_salles = {}".format(nom_salles))

        x = sqlite.select_salle()
        #dispatcher.utter_message(text=text)
        dispatcher.utter_message(display(x))

                

        #text="Les salles du ceri sont {}".format(select_data(tracker.get_slot("salle")))
    


        return []


class ActionRoomdescription(Action):

     def name(self) -> Text:
        return "action_description"

     def run(self, dispatcher: CollectingDispatcher,
             tracker: Tracker,
             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        #section = tracker.get_slot('section')
        #group = tracker.get_slot('group')

        #dispatcher.utter_message(text="/EXAMPLE/ Your next schedule is Math in room S2")
        #dispatcher.utter_message(text="Section = {}  Group = {}".format(section, group))
        #dispatcher.utter_message( "salle :  "+ tracker.get_slot("salle"))

        print(sqlite.select_description(tracker.get_slot("salle")))
        text="D'accord  la salle {} se situe {}".format( tracker.get_slot("salle") , sqlite.select_description(tracker.get_slot("salle")))
        dispatcher.utter_message(text=text)
        #dispatcher.utter_message( "salle :  "+ tracker.get_slot("salle"))



        return []



class ActionFreeRoom(Action):

     def name(self) -> Text:
        return "action_free_room"

     def run(self, dispatcher: CollectingDispatcher,
             tracker: Tracker,
             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        site = tracker.get_slot('site')
        time = tracker.get_slot('time')

        #dispatcher.utter_message(text="/EXAMPLE/ Your next schedule is Math in room S2")
        #dispatcher.utter_message(text="Section = {}  Group = {}".format(section, group))

        s = sqlite.select_free_room(site , time)
        dispatcher.utter_message(display(s))

        
        #dispatcher.utter_message("time = {}  site = {}".format(time, site))

        #text="la salle libre est {}".format(select_data(tracker.get_slot("site"),tracker.get_slot("time")))
        #text = "c'est bon"
        #dispatcher.utter_message(text)


        return []



def display(tab):
        """
        docstring
        """
        return " ".join(tab)
