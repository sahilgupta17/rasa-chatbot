
conda activate

python -m rasa_nlu.train -c greet_config.yml --data Data/covid_data.md -o models --fixed_model_name covidBot --project Chatbot --verbose

rasa train
rasa run
