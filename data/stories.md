stories:
  - story: greet
    steps:
     - intent: greet
     - action: utter_greet
     
  - story: general info
    steps:
     - intent: greet
     - action: utter_greet
     - intent: general info
     - action: utter_covid_info
     
  - story: ask symptoms
    steps:
     - intent: greet
     - action: utter_greet
     - intent: symptoms
     - action: utter_symptoms
    
  - story: covid spread info
    steps:
     - intent: greet
     - action: utter_greet
     - intent: spread
     - action: utter_spread
    
  - story: general vaccine info
    steps:
     - intent: greet
     - action: utter_greet
     - intent: vaccine info
     - action: utter_pfizer_info
     - action: utter_astrazeneca_info
     - action: utter_moderna_info
    
  - story: Pfizer info
    steps:
     - intent: greet
     - action: utter_greet
     - intent: Pfizer info
     - action: utter_pfizer_info
    
  - story: Astrazeneca info
    steps:
     - intent: greet
     - action: utter_greet
     - intent: Astrazeneca info
     - action: utter_astrazeneca_info
    
  - story: Moderna info
    steps:
     - intent: greet
     - action: utter_greet
     - intent: Moderna info
     - action: utter_moderna_info
    
  - story: vaccine side effects
    steps:
     - intent: greet
     - action: utter_greet
     - intent: side effects
     - action: utter_side_effects
    
  - story: testing
    steps:
     - intent: greet
     - action: utter_greet
     - intent: testing
     - action: utter_testing
    
  - story: social distancing
    steps:
     - intent: greet
     - action: utter_greet
     - intent: social distancing
     - action: utter_social_distancing
    
  - story: vaccine effectiveness
    steps:
     - intent: greet
     - action: utter_greet
     - intent: vaccine effectiveness
     - action: utter_pfizer_effectiveness
     - action: utter_astrazeneca_effectiveness
     - action: utter_moderna_effectiveness
    
  - story: measures to take if infected
    steps:
     - intent: greet
     - action: utter_greet
     - intent: measures if infected
     - action: utter_measures_if_infected
    
  - story: travel info and safety measures
    steps:
     - intent: greet
     - action: utter_greet
     - intent: travel
     - action: utter_travel_safety_measures
    
  - story: general info
    steps:
     - intent: greet
     - action: utter_greet
     - intent: general info
     - action: utter_covid_info
    
  - story: covid spread
    steps:
     - intent: greet
     - action: utter_greet
     - intent: spread
     - action: utter_spread
    
  - story: general info
    steps:
     - intent: greet
     - action: utter_greet
     - intent: general info
     - action: utter_covid_info